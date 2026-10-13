"""Verify every file in contributors/ follows the required template."""

import sys
from pathlib import Path

REQUIRED_FIELDS = [
    "**Name:**",
    "**GitHub username:**",
    "**Fun fact:**",
    "**Favorite Python library:**",
]


def check_file(path: Path) -> list[str]:
    errors = []
    if path.suffix != ".md":
        errors.append(f"{path}: must be a .md file")
        return errors

    text = path.read_text()
    for field in REQUIRED_FIELDS:
        if field not in text:
            errors.append(f"{path}: missing required field {field!r}")

    return errors


def main() -> int:
    contributors_dir = Path(__file__).resolve().parent.parent / "contributors"
    errors = []

    for path in sorted(contributors_dir.iterdir()):
        if path.name == ".gitkeep":
            continue
        errors.extend(check_file(path))

    if errors:
        print("Contributor file check failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print("All contributor files look good.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
