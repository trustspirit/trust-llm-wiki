#!/usr/bin/env python3
"""
Lint: detect potentially duplicate / near-duplicate wiki pages.

Improvement over naive alias-overlap (which flags every AI page
as duplicate because they all share 'artificial' / 'intelligence'):

- Frequency-aware stopwords: tokens appearing in ≥ 30% of pages
  within a directory are treated as common topic-vocabulary
  and excluded from similarity comparison.
- Jaccard similarity over remaining meaningful tokens.
- Source overlap is reported only when ≥ 6 sources are shared
  (sharing 1-5 sources is natural for related pages in the same
  topic cluster — e.g. all AI pages cite the same Elder Gong
  speech without being duplicates).

Usage:
    python3 .claude/scripts/lint-duplicates.py
    python3 .claude/scripts/lint-duplicates.py wiki/concepts

Exit 0 always. Output: candidate duplicate pairs per directory.
"""
import os
import re
import sys
import glob
from collections import Counter


# Always-stopwords across all domains (English + Korean particles).
GENERIC_STOPWORDS = {
    'a', 'an', 'and', 'or', 'the', 'of', 'to', 'is', 'in', 'for',
    'with', 'on', 'at', 'by', 'as', 'from', 'be', 'this', 'that',
    '은', '는', '이', '가', '을', '를', '의', '에', '과', '와',
}


def tokenize(s: str) -> set:
    """Lowercased word tokens (handles English + Korean)."""
    return set(re.findall(r'\w+', s.lower()))


def parse_page(path: str) -> dict:
    with open(path) as f:
        c = f.read()
    title_m = re.search(r'^title:\s*(.+)$', c, re.M)
    aliases_m = re.search(r'^aliases:\s*\[(.+)\]', c, re.M)
    sources_m = re.search(r'^sources:\s*\[(.+)\]', c, re.M)
    sources = set()
    if sources_m:
        sources = {s.strip() for s in sources_m.group(1).split(',') if s.strip()}
    return {
        'slug': os.path.basename(path)[:-3],
        'title': title_m.group(1).strip() if title_m else '',
        'aliases': aliases_m.group(1).strip() if aliases_m else '',
        'sources': sources,
    }


def get_pages(d: str):
    paths = sorted(glob.glob(os.path.join(d, '*.md')))
    return [parse_page(p) for p in paths if not p.endswith('index.md')]


def compute_stopwords(pages, freq_threshold=0.30):
    """
    Tokens that appear in >= freq_threshold of pages' title+aliases
    are common topic-vocabulary, not distinguishing — treat as stopwords.
    """
    n = len(pages)
    min_count = max(2, int(n * freq_threshold) + 1)
    counter = Counter()
    for p in pages:
        toks = tokenize(p['title']) | tokenize(p['aliases'])
        for t in toks:
            counter[t] += 1
    return {t for t, c in counter.items() if c >= min_count}


def check_dir(d: str, title_overlap_threshold=0.5, source_overlap_min=6):
    pages = get_pages(d)
    if len(pages) < 2:
        return []

    stopwords = compute_stopwords(pages) | GENERIC_STOPWORDS

    findings = []
    for i in range(len(pages)):
        for j in range(i + 1, len(pages)):
            p1, p2 = pages[i], pages[j]

            # Title + aliases similarity (Jaccard, after stopword removal)
            t1 = (tokenize(p1['title']) | tokenize(p1['aliases'])) - stopwords
            t2 = (tokenize(p2['title']) | tokenize(p2['aliases'])) - stopwords
            if t1 and t2:
                shared = t1 & t2
                similarity = len(shared) / min(len(t1), len(t2))
                if similarity >= title_overlap_threshold:
                    findings.append(
                        (p1['slug'], p2['slug'],
                         f'meaningful-token overlap {similarity:.0%}, shared: {shared}')
                    )

            # Source overlap (only flag when substantially overlapping)
            shared_sources = p1['sources'] & p2['sources']
            if len(shared_sources) >= source_overlap_min:
                findings.append(
                    (p1['slug'], p2['slug'],
                     f'shares {len(shared_sources)} sources (high overlap)')
                )
    return findings


def main():
    if len(sys.argv) > 1:
        dirs = sys.argv[1:]
    else:
        dirs = sorted(
            d for d in glob.glob('wiki/*')
            if os.path.isdir(d)
        )

    any_findings = False
    for d in dirs:
        findings = check_dir(d)
        print(f'=== {d} ===')
        if findings:
            any_findings = True
            for slug1, slug2, reason in findings:
                print(f'  {slug1} ↔ {slug2}')
                print(f'    {reason}')
        else:
            print('  (no candidate duplicates)')
        print()

    if not any_findings:
        print('No candidate duplicates detected.')


if __name__ == '__main__':
    main()
