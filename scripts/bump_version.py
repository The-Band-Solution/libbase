#!/usr/bin/env python3
"""
Script to automate semantic versioning bumps in pyproject.toml.
Usage: python scripts/bump_version.py [major|minor|patch]
"""

import sys
import re
from pathlib import Path

def bump_version(part: str):
    pyproject_path = Path("pyproject.toml")
    if not pyproject_path.exists():
        print("Error: pyproject.toml not found.")
        sys.exit(1)

    with open(pyproject_path, "r") as f:
        content = f.read()

    match = re.search(r'version = "((\d+)\.(\d+)\.(\d+))"', content)
    if not match:
        print("Error: Could not find version in pyproject.toml.")
        sys.exit(1)

    old_version = match.group(1)
    major, minor, patch = map(int, match.group(2, 3, 4))

    if part == "major":
        major += 1
        minor = 0
        patch = 0
    elif part == "minor":
        minor += 1
        patch = 0
    elif part == "patch":
        patch += 1
    else:
        print("Usage: python scripts/bump_version.py [major|minor|patch]")
        sys.exit(1)

    new_version = f"{major}.{minor}.{patch}"
    new_content = content.replace(f'version = "{old_version}"', f'version = "{new_version}"')

    with open(pyproject_path, "w") as f:
        f.write(new_content)

    print(f"Bumped version from {old_version} to {new_version}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scripts/bump_version.py [major|minor|patch]")
        sys.exit(1)
    
    bump_version(sys.argv[1])
