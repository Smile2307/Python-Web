#!/usr/bin/env python3
"""Validate local Codex Skill layout and required frontmatter."""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SKILLS = ROOT / "skills"
NAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]*$")


def main() -> int:
    failures: list[str] = []
    for path in sorted(SKILLS.iterdir()):
        if not path.is_dir():
            continue
        if not NAME_RE.fullmatch(path.name):
            failures.append(f"invalid skill directory name: {path.name}")
        skill = path / "SKILL.md"
        if not skill.is_file():
            failures.append(f"missing SKILL.md: {path.name}")
            continue
        text = skill.read_text(encoding="utf-8")
        if not text.lstrip().startswith("# "):
            failures.append(f"SKILL.md must start with a markdown H1: {skill}")

    for required in [ROOT / "AGENTS.md", ROOT / "README.md", ROOT / "INSTALL.md"]:
        if not required.is_file():
            failures.append(f"missing required file: {required.name}")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1
    print(f"OK: {sum(1 for p in SKILLS.iterdir() if p.is_dir())} skills validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
