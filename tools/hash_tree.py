#!/usr/bin/env python3
"""Create a deterministic SHA-256 inventory for a local extracted game tree.

This tool records metadata only. It does not copy or package game files.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Iterable

CHUNK_SIZE = 4 * 1024 * 1024


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(CHUNK_SIZE), b""):
            digest.update(chunk)
    return digest.hexdigest()


def iter_files(root: Path, excluded: Iterable[Path]) -> list[Path]:
    excluded_resolved = {path.resolve() for path in excluded}
    files: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if path.resolve() in excluded_resolved:
            continue
        files.append(path)
    return sorted(files, key=lambda path: path.relative_to(root).as_posix())


def build_manifest(root: Path, label: str, excluded: Iterable[Path]) -> dict:
    records = []
    total_size = 0

    for path in iter_files(root, excluded):
        stat = path.stat()
        total_size += stat.st_size
        records.append({"path": path.relative_to(root).as_posix(), "size": stat.st_size, "sha256": sha256_file(path)})

    return {"schema_version": 1, "root_label": label, "algorithm": "sha256", "file_count": len(records), "total_size": total_size, "files": records}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Hash every file in a local extracted game tree and emit deterministic JSON.")
    parser.add_argument("root", type=Path, help="Root directory to inventory")
    parser.add_argument("--label", default="local-extraction", help="Non-sensitive label stored in the manifest instead of the absolute path")
    parser.add_argument("--output", type=Path, help="Write JSON to this path instead of stdout")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = args.root.expanduser().resolve()
    if not root.is_dir():
        raise SystemExit(f"not a directory: {root}")

    excluded = [args.output] if args.output else []
    manifest = build_manifest(root, args.label, excluded)
    payload = json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=False) + "\n"

    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload, encoding="utf-8")
    else:
        print(payload, end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
