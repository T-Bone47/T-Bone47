#!/usr/bin/env python3
"""Validate the profile README's local image links and SVG assets.

Runs with Python's standard library; no network or third-party packages needed.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path
from xml.etree import ElementTree

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
ASSETS = ROOT / "assets"


def validate() -> list[str]:
    errors: list[str] = []
    content = README.read_text(encoding="utf-8")

    # GitHub README images are primarily embedded with HTML for sizing.
    html_images = re.findall(
        r'<img\b[^>]*?\bsrc\s*=\s*["\']([^"\']+)["\']',
        content,
        flags=re.IGNORECASE | re.DOTALL,
    )
    markdown_images = re.findall(r'!\[[^\]]*\]\(([^\s)]+)', content)
    local_images = [
        uri.split("?", 1)[0].split("#", 1)[0]
        for uri in [*html_images, *markdown_images]
        if not uri.startswith(("https://", "http://", "data:"))
    ]

    for image in local_images:
        candidate = (ROOT / image).resolve()
        if not candidate.is_relative_to(ROOT):
            errors.append(f"Image path escapes repository: {image}")
        elif not candidate.is_file():
            errors.append(f"Missing README image: {image}")

    svg_files = sorted(ASSETS.rglob("*.svg"))
    for path in svg_files:
        try:
            tree = ElementTree.parse(path)
            root = tree.getroot()
            if root.tag.rsplit("}", 1)[-1] != "svg":
                errors.append(f"Not an SVG document: {path.relative_to(ROOT)}")
            if not any(el.tag.rsplit("}", 1)[-1] == "title" for el in root.iter()):
                errors.append(f"SVG missing accessible title: {path.relative_to(ROOT)}")
        except ElementTree.ParseError as exc:
            errors.append(f"Malformed SVG {path.relative_to(ROOT)}: {exc}")

    print(
        f"Checked {len(svg_files)} SVG assets and "
        f"{len(local_images)} local README image references."
    )
    return errors


if __name__ == "__main__":
    failures = validate()
    if failures:
        for failure in failures:
            print(f"ERROR: {failure}", file=sys.stderr)
        raise SystemExit(1)
    print("Profile assets: PASS")
