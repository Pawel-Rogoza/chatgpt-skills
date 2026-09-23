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
        for name in ("plugins", "source-policy", ".agents", "config"):
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
            for skill in package.load_config(self.root):
                name = skill["name"]
                for ref in skill["shared_references"]:
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
        release = manifest["version"].split("+", 1)[0]
        manifest["version"] = release + "+codex.test"
        path.write_text(json.dumps(manifest))
        self.assertIn(release + "+codex.test", package.build(self.root).name)
        manifest["version"] = "99.0.0+codex.test"
        path.write_text(json.dumps(manifest))
        with self.assertRaisesRegex(ValueError, "Version drift"):
            package.validate(self.root)

    def config(self):
        return json.loads((self.root / package.CONFIG).read_text())

    def save_config(self, data):
        (self.root / package.CONFIG).write_text(json.dumps(data))

    def test_new_skill_with_two_local_references_and_subset_of_shared(self):
        data = self.config()
        name = "pl-test-analysis"
        data["skills"].append({
            "name": name,
            "local_files": ["SKILL.md", "agents/openai.yaml", "references/a.md", "references/b.md"],
            "shared_references": ["case-record.md"],
        })
        self.save_config(data)
        folder = package.plugin_root(self.root) / "skills" / name
        (folder / "references").mkdir(parents=True)
        (folder / "agents").mkdir()
        manifest = json.loads((package.plugin_root(self.root) / ".codex-plugin/plugin.json").read_text())
        version = manifest["version"].split("+", 1)[0]
        (folder / "SKILL.md").write_text(
            f'---\nname: {name}\ndescription: Synthetic extension test.\nmetadata:\n  version: "{version}"\n---\n'
            '[A](references/a.md) [B](references/b.md) [Record](references/case-record.md)\n')
        (folder / "agents/openai.yaml").write_text('interface:\n  display_name: "Test"\n')
        (folder / "references/a.md").write_text("Synthetic A.\n")
        (folder / "references/b.md").write_text("Synthetic B.\n")
        package.sync(self.root)
        with zipfile.ZipFile(package.build(self.root)) as z:
            prefix = f"skills/{name}/"
            self.assertEqual({n[len(prefix):] for n in z.namelist() if n.startswith(prefix)}, {
                "SKILL.md", "agents/openai.yaml", "references/a.md", "references/b.md", "references/case-record.md"})

    def test_invalid_configuration_fails_before_sync_writes(self):
        import copy
        initial = self.config()
        variants = []
        for key in ("schema_version", "skills"):
            data = copy.deepcopy(initial)
            del data[key]
            variants.append(data)
        for value in (2, True, "1", None):
            data = copy.deepcopy(initial)
            data["schema_version"] = value
            variants.append(data)
        data = copy.deepcopy(initial)
        data["unknown"] = []
        variants.append(data)
        data = copy.deepcopy(initial)
        data["skills"].append(data["skills"][0])
        variants.append(data)
        for key, value in (("name", "../escape"), ("unknown", []), ("local_files", []),
                           ("shared_references", "case-record.md"),
                           ("shared_references", ["case-record.md", "case-record.md"]),
                           ("shared_references", ["../case-record.md"])):
            data = copy.deepcopy(initial)
            data["skills"][0][key] = value
            variants.append(data)
        for filename in ("../private.txt", "/tmp/private.txt", "references/../../private.txt",
                         "references//a.md", "references/./a.md", "references\\a.md", "*.md",
                         "SKILL.md", "skill.md", "references/case-record.md", "references"):
            data = copy.deepcopy(initial)
            data["skills"][0]["local_files"].append(filename)
            variants.append(data)
        destination = package.plugin_root(self.root) / "skills/pl-criminal-appeal/references/source-policy.md"
        before = destination.read_bytes()
        (self.root / "source-policy/source-policy.md").write_text("changed canonical source")
        for data in variants:
            with self.subTest(config=data):
                self.save_config(data)
                with self.assertRaises(ValueError):
                    package.sync(self.root)
                with self.assertRaises(ValueError):
                    package.build(self.root)
                self.assertEqual(destination.read_bytes(), before)

    def test_duplicate_json_keys_rejected(self):
        path = self.root / package.CONFIG
        path.write_text(path.read_text().replace('"schema_version": 1', '"schema_version": 1, "schema_version": 1'))
        with self.assertRaisesRegex(ValueError, "Duplicate JSON key"):
            package.validate(self.root)

    def test_unknown_or_missing_declared_reference_rejected(self):
        data = self.config()
        data["skills"][0]["shared_references"].append("does-not-exist.md")
        self.save_config(data)
        with self.assertRaises((ValueError, OSError)):
            package.sync(self.root)
        with self.assertRaisesRegex(ValueError, "Missing"):
            package.build(self.root)

    def test_missing_configuration_is_not_implicitly_discovered(self):
        (self.root / package.CONFIG).unlink()
        with self.assertRaises(FileNotFoundError):
            package.build(self.root)

    def test_symlinked_configuration_and_shared_source_rejected(self):
        for relative in (package.CONFIG, "source-policy/case-record.md"):
            with self.subTest(path=relative):
                path = self.root / relative
                original = path.read_bytes()
                replacement = self.root / "replacement"
                replacement.write_bytes(original)
                path.unlink()
                path.symlink_to(replacement)
                with self.assertRaisesRegex(ValueError, "Symlink"):
                    package.sync(self.root)
                with self.assertRaisesRegex(ValueError, "Symlink"):
                    package.build(self.root)
                path.unlink()
                path.write_bytes(original)

    def test_directory_symlink_and_dangling_symlink_rejected(self):
        folder = package.plugin_root(self.root) / "skills/pl-criminal-appeal/references"
        moved = self.root / "moved-references"
        folder.rename(moved)
        folder.symlink_to(moved, target_is_directory=True)
        with self.assertRaisesRegex(ValueError, "Symlink"):
            package.sync(self.root)
        with self.assertRaisesRegex(ValueError, "Symlink"):
            package.build(self.root)
        folder.unlink()
        moved.rename(folder)
        (package.plugin_root(self.root) / "dangling").symlink_to(self.root / "missing")
        with self.assertRaisesRegex(ValueError, "Symlink"):
            package.build(self.root)

    def test_check_is_read_only_and_sync_preflights_all_sources(self):
        destination = package.plugin_root(self.root) / "skills/pl-criminal-appeal/references/source-policy.md"
        before = destination.read_bytes()
        (self.root / "source-policy/source-policy.md").write_text("changed canonical source")
        with self.assertRaisesRegex(ValueError, "Stale"):
            package.validate(self.root)
        self.assertEqual(before, destination.read_bytes())
        (self.root / "source-policy/foreign-national.md").unlink()
        with self.assertRaises(FileNotFoundError):
            package.sync(self.root)
        self.assertEqual(before, destination.read_bytes())


if __name__ == "__main__":
    unittest.main()
