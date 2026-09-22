#!/usr/bin/env python3
"""Sync shared references, validate the pilot, and build a scoped plugin ZIP."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml

PLUGIN = "legal-ai-pl"
SKILLS = ("pl-criminal-appeal", "pl-legal-document-review")
SHARED = ("source-policy.md", "case-record.md", "temporal-law.md", "foreign-national.md")
SPECIFIC = {"pl-criminal-appeal": "appeal-method.md",
            "pl-legal-document-review": "appeal-review.md"}


def plugin_root(root: Path) -> Path:
    return root / "plugins" / PLUGIN


def ensure_local(path: Path, boundary: Path) -> None:
    if not path.resolve().is_relative_to(boundary.resolve()):
        raise ValueError(f"Path escapes package: {path}")
    current = path
    while current != boundary:
        if current.is_symlink():
            raise ValueError(f"Symlink is not allowed in package input: {current}")
        current = current.parent


def sync(root: Path) -> None:
    for name in SKILLS:
        for filename in SHARED:
            source = root / "source-policy" / filename
            destination = plugin_root(root) / "skills" / name / "references" / filename
            ensure_local(source, root)
            ensure_local(destination, root)
            destination.parent.mkdir(parents=True, exist_ok=True)
            destination.write_bytes(source.read_bytes())


def package_files(root: Path) -> list[Path]:
    base = plugin_root(root)
    paths = [base / ".codex-plugin" / "plugin.json"]
    for name in SKILLS:
        folder = base / "skills" / name
        paths.extend([folder / "SKILL.md", folder / "agents" / "openai.yaml"])
        paths.extend(folder / "references" / f for f in (*SHARED, SPECIFIC[name]))
    return sorted(paths)


def validate(root: Path) -> list[Path]:
    base = plugin_root(root)
    paths = package_files(root)
    for path in paths:
        ensure_local(path, root)
        if not path.is_file():
            raise ValueError(f"Missing package file: {path}")
    actual = set()
    for path in base.rglob("*"):
        ensure_local(path, root)
        if path.is_file():
            actual.add(path)
    if actual != set(paths):
        raise ValueError(f"Unexpected plugin files; update the explicit allowlist intentionally: {actual - set(paths)}")
    manifest = json.loads(paths[0].read_text(encoding="utf-8"))
    if manifest.get("name") != PLUGIN or manifest.get("skills") != "./skills/":
        raise ValueError("Plugin name or skills path does not match the package")
    version = manifest.get("version", "")
    if not re.fullmatch(r"(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:\+[0-9A-Za-z-]+(?:\.[0-9A-Za-z-]+)*)?", version):
        raise ValueError("Expected a three-part release version with optional build metadata")
    if any(k in manifest for k in ("apps", "mcpServers", "hooks")):
        raise ValueError("The pilot package must remain instruction-only")
    catalog = json.loads((root / ".agents/plugins/marketplace.json").read_text(encoding="utf-8"))
    matches = [p for p in catalog["plugins"] if p["name"] == PLUGIN]
    if len(matches) != 1 or matches[0]["source"] != {"source": "local", "path": f"./plugins/{PLUGIN}"}:
        raise ValueError("Marketplace must resolve this repository's plugin exactly once")
    policy = matches[0].get("policy", {})
    if policy.get("installation") != "AVAILABLE" or policy.get("authentication") != "ON_INSTALL":
        raise ValueError("Unexpected pilot installation policy")
    for name in SKILLS:
        folder = base / "skills" / name
        text = (folder / "SKILL.md").read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
        if not match:
            raise ValueError(f"Missing frontmatter: {name}")
        front = yaml.safe_load(match.group(1))
        if front.get("name") != name or not front.get("description") or len(front["description"]) > 1024:
            raise ValueError(f"Invalid discovery metadata: {name}")
        if front.get("metadata", {}).get("version") != version.split("+", 1)[0]:
            raise ValueError(f"Version drift: {name}")
        ui = yaml.safe_load((folder / "agents/openai.yaml").read_text(encoding="utf-8"))
        if ui.get("policy", {}).get("allow_implicit_invocation", True) is not True:
            raise ValueError(f"Implicit discovery unexpectedly disabled: {name}")
        for filename in SHARED:
            source = root / "source-policy" / filename
            ensure_local(source, root)
            if source.read_bytes() != (folder / "references" / filename).read_bytes():
                raise ValueError(f"Stale shared reference: {name}/{filename}; run sync")
        for path in folder.rglob("*.md"):
            content = path.read_text(encoding="utf-8")
            if "[TODO:" in content:
                raise ValueError(f"Unfinished scaffold: {path}")
            for target in re.findall(r"\]\(([^)]+)\)", content):
                parsed = urlsplit(target)
                if parsed.scheme or target.startswith("#"):
                    continue
                resolved = path.parent / unquote(parsed.path)
                ensure_local(resolved, folder)
                if not resolved.is_file():
                    raise ValueError(f"Broken skill reference: {path}: {target}")
        # The standalone skill must explicitly route to all its references.
        for ref in folder.joinpath("references").glob("*.md"):
            if f"references/{ref.name}" not in text:
                raise ValueError(f"Unreachable reference from entrypoint: {ref}")
    return paths


def build(root: Path, output_dir: Path | None = None) -> Path:
    paths = validate(root)
    base = plugin_root(root)
    manifest = json.loads((base / ".codex-plugin/plugin.json").read_text(encoding="utf-8"))
    output_dir = output_dir or root / "dist"
    output_dir.mkdir(parents=True, exist_ok=True)
    target = output_dir / f"{PLUGIN}-{manifest['version']}.zip"
    with zipfile.ZipFile(target, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in paths:
            info = zipfile.ZipInfo(path.relative_to(base).as_posix(), date_time=(2026, 1, 1, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())
    digest = hashlib.sha256(target.read_bytes()).hexdigest()
    target.with_suffix(".zip.sha256").write_text(f"{digest}  {target.name}\n", encoding="utf-8")
    return target


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("sync", "check", "build"))
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    root = args.root.resolve()
    try:
        if args.command == "sync":
            sync(root)
            print("Shared references synchronized; run check before packaging.")
        elif args.command == "check":
            print(f"Package structure OK: {len(validate(root))} files. Legal quality is not assessed.")
        else:
            print(build(root))
    except (ValueError, OSError, KeyError, TypeError, yaml.YAMLError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
