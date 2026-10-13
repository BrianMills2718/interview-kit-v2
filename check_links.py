"""Check the guides: every relative .md link resolves, and the named standards keep their parts.

Standard library only; this is the repository's local gate (no hosted CI). Prints one FAIL line
per broken link or missing standard part, then counts and the exit status.
Absolute URLs (http, https, mailto) and pure anchors (#...) are skipped, not checked.
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
# Markdown inline links: [text](target). Regex over Markdown link syntax, not prose meaning.
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")


def relative_md_targets(text: str) -> list[str]:
    """Return the link targets in text that are relative paths to .md files."""
    targets = []
    for target in LINK.findall(text):
        if re.match(r"^[a-z]+:", target) or target.startswith("#"):
            continue
        path = target.split("#", 1)[0]
        if path.endswith(".md"):
            targets.append(path)
    return targets


# Parts each external standard must keep where a guide names it: (file, line marker, required words).
# Zachman's six interrogatives; Nygard's ADR sections; the PRD's core sections.
STANDARD_RULES = [
    ("3-models.md", "Zachman", ["what", "how", "where", "who", "when", "why"]),
    ("2-documents.md", "ADR (architecture decision record)", ["context", "decision", "consequences"]),
    ("2-documents.md", "`docs/PRD.md`", ["goal", "requirements", "assumptions", "risks"]),
]


def standard_failures() -> list[str]:
    """Return one message per standard rule whose marker line is missing or lacks a required word."""
    failures = []
    for name, marker, words in STANDARD_RULES:
        lines = [ln for ln in (ROOT / name).read_text(encoding="utf-8").splitlines() if marker in ln]
        if not lines:
            failures.append(f"{name}: no line names {marker!r}")
            continue
        found = set(re.findall(r"[a-z]+", lines[0].lower()))
        missing = [w for w in words if w not in found]
        if missing:
            failures.append(f"{name}: {marker!r} line lacks {missing}")
    return failures


def main() -> int:
    """Check every .md file under ROOT (skipping .git) and the standard rules; return 0 if all pass, else 1."""
    files = sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts)
    checked = broken = 0
    for md in files:
        for target in relative_md_targets(md.read_text(encoding="utf-8")):
            checked += 1
            if not (md.parent / target).resolve().is_file():
                broken += 1
                print(f"FAIL {md.relative_to(ROOT)} -> {target}")
    standard_fails = standard_failures()
    for msg in standard_fails:
        print(f"FAIL standard {msg}")
    status = 0 if broken == 0 and not standard_fails else 1
    print(f"files={len(files)} links_checked={checked} ok={checked - broken} broken={broken}")
    print(f"standard_rules={len(STANDARD_RULES)} ok={len(STANDARD_RULES) - len(standard_fails)} failed={len(standard_fails)}")
    print(f"exit status {status}")
    return status


if __name__ == "__main__":
    sys.exit(main())
