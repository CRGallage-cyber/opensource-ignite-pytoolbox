"""Create GitHub issues from ISSUES.md using the `gh` CLI.

Usage:
    python scripts/create_issues.py owner/repo
    python scripts/create_issues.py owner/repo --dry-run
"""

import argparse
import re
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

ISSUES_FILE = Path(__file__).resolve().parent.parent / "ISSUES.md"

LABEL_COLORS = {
    "bug": "d73a4a",
    "feature": "a2eeef",
    "add-on": "fbca04",
    "good first issue": "7057ff",
    "beginner": "0e8a16",
    "intermediate": "fbca04",
}

ISSUE_HEADING_RE = re.compile(r"^## #(\d+) — (.+)$")
LABELS_LINE_RE = re.compile(r"^\*\*Labels:\*\*\s*(.+)$")


@dataclass
class Issue:
    number: int
    title: str
    labels: list[str] = field(default_factory=list)
    body_lines: list[str] = field(default_factory=list)

    @property
    def body(self) -> str:
        return "\n".join(self.body_lines).strip() + "\n"


def parse_issues(text: str) -> list[Issue]:
    lines = text.splitlines()
    issues: list[Issue] = []
    current: Issue | None = None

    for line in lines:
        heading_match = ISSUE_HEADING_RE.match(line)
        if heading_match:
            if current is not None:
                issues.append(current)
            current = Issue(number=int(heading_match.group(1)), title=heading_match.group(2))
            continue

        if current is None:
            continue

        # Stop collecting a given issue's body once the next top-level
        # section heading ("# Bugs", "# Features", ...) appears, or a
        # horizontal rule that separates issues.
        if line.startswith("# ") and not line.startswith("## "):
            issues.append(current)
            current = None
            continue

        labels_match = LABELS_LINE_RE.match(line)
        if labels_match:
            raw_labels = labels_match.group(1)
            current.labels = [label.strip("` ") for label in raw_labels.split(",")]
            continue

        if line.strip() == "---":
            continue

        current.body_lines.append(line)

    if current is not None:
        issues.append(current)

    return issues


def collect_labels(issues: list[Issue]) -> set[str]:
    labels: set[str] = set()
    for issue in issues:
        labels.update(issue.labels)
    return labels


def ensure_labels(repo: str, labels: set[str], dry_run: bool) -> None:
    for label in sorted(labels):
        color = LABEL_COLORS.get(label, "ededed")
        cmd = [
            "gh",
            "label",
            "create",
            label,
            "--repo",
            repo,
            "--color",
            color,
            "--force",
        ]
        if dry_run:
            print(f"[dry-run] {' '.join(cmd)}")
            continue
        subprocess.run(cmd, check=False)


def create_issue(repo: str, issue: Issue, dry_run: bool) -> None:
    cmd = [
        "gh",
        "issue",
        "create",
        "--repo",
        repo,
        "--title",
        f"#{issue.number} {issue.title}",
        "--body",
        issue.body,
    ]
    for label in issue.labels:
        cmd += ["--label", label]

    if dry_run:
        print(f"[dry-run] Would create issue #{issue.number}: {issue.title}")
        print(f"          Labels: {', '.join(issue.labels)}")
        print(f"          Body length: {len(issue.body)} characters")
        return

    subprocess.run(cmd, check=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", help="GitHub repo in owner/repo form")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would be created without calling gh",
    )
    args = parser.parse_args()

    if not ISSUES_FILE.exists():
        print(f"Could not find {ISSUES_FILE}", file=sys.stderr)
        return 1

    text = ISSUES_FILE.read_text()
    issues = parse_issues(text)

    if not issues:
        print("No issues parsed from ISSUES.md", file=sys.stderr)
        return 1

    print(f"Parsed {len(issues)} issues from ISSUES.md")

    labels = collect_labels(issues)
    ensure_labels(args.repo, labels, args.dry_run)

    for issue in issues:
        create_issue(args.repo, issue, args.dry_run)

    return 0


if __name__ == "__main__":
    sys.exit(main())
