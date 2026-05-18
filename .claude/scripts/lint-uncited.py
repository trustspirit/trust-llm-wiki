#!/usr/bin/env python3
"""
Lint: detect uncited factual claims in wiki/ pages.

Improvement over naive `grep '[.!?]$' | grep -v '[source:'`:
recognizes the **bundle citation pattern** described in
CLAUDE.md §1.4 — where a section header (or its lead-in line)
carries `[source: ...]` and all bullets in that section inherit
the citation. Such bullets are not flagged.

Usage:
    python3 .claude/scripts/lint-uncited.py
    python3 .claude/scripts/lint-uncited.py wiki/concepts/<file>.md

Exit code 0 always. Output is human-readable.
"""
import re
import sys
import glob


def is_factual_line(line: str) -> bool:
    """Lines that look like declarative factual statements."""
    s = line.rstrip()
    if not s:
        return False
    if s.startswith('#'):     # header
        return False
    if s.startswith('|'):     # table row
        return False
    if s.startswith('>'):     # blockquote / synthesis
        return False
    if s.startswith('('):     # parenthetical
        return False
    if s.startswith('!'):     # image
        return False
    if re.match(r'^\s*\d+\.', s):  # numbered list
        return False
    if not re.search(r'[.!?]\s*$', s):  # must end with terminal punct
        return False
    if '[source:' in s:       # already cited
        return False
    if '[[' in s:             # wikilink line — often navigation
        return False
    if len(s) < 40:           # too short to be substantive
        return False
    return True


def has_bundle_citation(lines, idx, lookback=30):
    """
    Check if the current line (at `idx`) is covered by a bundle
    citation — `[source: ...]` somewhere earlier in the same
    top-level (##) section.

    Sub-section headers (###, ####, ...) inherit their parent ##
    section's citation, so they do NOT count as boundaries.

    Walks backward up to `lookback` lines, returns True if it finds
    `[source: ...]` before hitting a new ## section header.
    """
    for j in range(idx - 1, max(-1, idx - 1 - lookback), -1):
        prev = lines[j].rstrip()
        # Only level-2 (##) headers are boundaries.
        # `re.match('^## [^#]', ...)` matches "## X" but not "### X".
        if re.match(r'^## [^#]', prev):
            return False
        if '[source:' in prev:
            return True
    return False


def check_file(path):
    with open(path) as f:
        lines = f.read().split('\n')

    fm = False
    fm_done = False
    issues = []

    for i, ln in enumerate(lines):
        s = ln.rstrip()
        if s == '---':
            if not fm_done:
                fm = not fm
                if not fm:
                    fm_done = True
            continue
        if fm:
            continue
        if not is_factual_line(ln):
            continue
        if has_bundle_citation(lines, i):
            continue
        issues.append((i + 1, s[:140]))
    return issues


def main():
    if len(sys.argv) > 1:
        paths = sys.argv[1:]
    else:
        paths = sorted(glob.glob('wiki/**/*.md', recursive=True))

    any_issues = False
    for path in paths:
        if path.endswith('index.md'):
            continue
        issues = check_file(path)
        if issues:
            any_issues = True
            print(f'-- {path} --')
            for line_no, text in issues:
                print(f'  L{line_no}: {text}')

    if not any_issues:
        print('No uncited factual claims detected.')


if __name__ == '__main__':
    main()
