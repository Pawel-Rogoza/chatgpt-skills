"""Packaging invariants: independent skills, privacy boundary, drift and reproducibility."""
import importlib.util
import json
import shutil
import tempfile
import unittest
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("package", ROOT / "scripts/package.py")
package = importlib.util.module_from_spec(spec)
spec.loader.exec_module(package)


class PackageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in ("plugins", "source-policy", ".agents"):
            shutil.copytree(ROOT / name, self.root / name)

    def test_standalone_archive_and_reproducibility(self):
        (self.root / "private").mkdir()
        (self.root / "private/client.txt").write_text("synthetic-private-marker")
        (self.root / "source-policy/internal.txt").write_text("synthetic-internal-marker")
        first = package.build(self.root).read_bytes()
        target = package.build(self.root)
        self.assertEqual(first, target.read_bytes())
        with zipfile.ZipFile(target) as z:
            self.assertEqual(set(z.namelist()), {p.relative_to(package.plugin_root(self.root)).as_posix() for p in package.package_files(self.root)})
            self.assertFalse(any(b"synthetic-private-marker" in z.read(n) or b"synthetic-internal-marker" in z.read(n) for n in z.namelist()))
            for name in package.SKILLS:
                for ref in package.SHARED:
                    self.assertIn(f"skills/{name}/references/{ref}", z.namelist())

    def test_stale_reference_blocks_build_until_synced(self):
        source = self.root / "source-policy/source-policy.md"
        source.write_text(source.read_text() + "\nUpdated policy.\n")
        with self.assertRaisesRegex(ValueError, "Stale"):
            package.build(self.root)
        package.sync(self.root)
        package.validate(self.root)

    def test_missing_reference_blocks_build(self):
        path = package.plugin_root(self.root) / "skills/pl-criminal-appeal/references/appeal-method.md"
        path.unlink()
        with self.assertRaisesRegex(ValueError, "Missing"):
            package.build(self.root)

    def test_reference_outside_standalone_skill_is_rejected(self):
        skill = package.plugin_root(self.root) / "skills/pl-criminal-appeal/SKILL.md"
        skill.write_text(skill.read_text() + "\n[External](../../../../README.md)\n")
        with self.assertRaisesRegex(ValueError, "escapes"):
            package.validate(self.root)

    def test_extra_plugin_file_cannot_silently_enter_archive(self):
        (package.plugin_root(self.root) / "client-notes.md").write_text("synthetic")
        with self.assertRaisesRegex(ValueError, "Unexpected plugin files"):
            package.build(self.root)

    def test_symlink_cannot_import_external_file(self):
        outside = self.root / "outside.md"
        outside.write_text("synthetic")
        path = package.plugin_root(self.root) / "skills/pl-criminal-appeal/references/appeal-method.md"
        path.unlink()
        path.symlink_to(outside)
        with self.assertRaisesRegex(ValueError, "Symlink"):
            package.build(self.root)

    def test_cachebuster_preserves_release_but_real_version_drift_fails(self):
        path = package.plugin_root(self.root) / ".codex-plugin/plugin.json"
        manifest = json.loads(path.read_text())
        manifest["version"] = "0.1.0+codex.test"
        path.write_text(json.dumps(manifest))
        self.assertIn("0.1.0+codex.test", package.build(self.root).name)
        manifest["version"] = "0.2.0+codex.test"
        path.write_text(json.dumps(manifest))
        with self.assertRaisesRegex(ValueError, "Version drift"):
            package.validate(self.root)


if __name__ == "__main__":
    unittest.main()
