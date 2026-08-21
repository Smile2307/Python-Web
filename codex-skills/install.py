#!/usr/bin/env python3
"""Install/sync Smile2307 Codex Skills into a local skills directory.

Usage:
  python install.py --target ~/.agents/skills
  python install.py --target ~/.agents/skills --core-only
  python install.py --target ~/.agents/skills --dry-run
"""
from __future__ import annotations

import argparse
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SKILLS = ROOT / "skills"
CORE = {
    "create-plan",
    "engineering-workflow",
    "embedded-python",
    "github-ci",
    "github-pr-review",
    "repo-search",
}


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", type=Path, required=True)
    parser.add_argument("--core-only", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    names = sorted(CORE if args.core_only else [p.name for p in SKILLS.iterdir() if p.is_dir()])
    for name in names:
        src = SKILLS / name
        dst = args.target / name
        skill_file = src / "SKILL.md"
        if not skill_file.is_file():
            raise SystemExit(f"Invalid skill: {name} (missing SKILL.md)")
        print(f"SYNC {skill_file} -> {dst / 'SKILL.md'}")
        if not args.dry_run:
            dst.mkdir(parents=True, exist_ok=True)
            shutil.copy2(skill_file, dst / "SKILL.md")
    print(f"Installed {len(names)} skill(s) to {args.target}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
