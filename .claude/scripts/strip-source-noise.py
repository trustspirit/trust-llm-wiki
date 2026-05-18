#!/usr/bin/env python3
"""
Strip HTML-extraction noise from source markdown files.

Usage:
    # Process a single file:
    python3 .claude/scripts/strip-source-noise.py sources/articles/<file>.md

    # Process all sources:
    python3 .claude/scripts/strip-source-noise.py

What it removes (frontmatter preserved):
    - Audio player UI: "Your browser does not support the audio element",
      "0:00/26:21", "0.5x0.75x1.0x...", "Speed Click below to adjust...",
      Play / Pause / Volume / Muted / Download / More / Dismiss / Listen
    - "Click to copy link" / "Speech link copied" / "Full VideoHighlight Video"
    - "PDF generation in progress....."
    - Breadcrumb: "Home > Speeches > ..."
    - Language selector blocks: "DE\n - EN\n - ES\n ..."
    - Image ID bullets: "- BN-AI-Guidelines-Elder-Gong-...jpeg",
      "- 1Y8A6542.jpeg" (uppercase image IDs)
    - "Download Photo" / "Download Photos" stray lines
    - Empty bullets ("- ") and lone "*"/"**" lines
    - Triple-or-more blank lines collapsed to double

Idempotent: running multiple times is safe.

Per CLAUDE.md (sources/ 불변 원칙), this counts as recoverable extraction
error correction, not content modification. User-requested or part of
standard ingest pipeline (see references/ingest-protocols.md §1.7).
"""
import re
import sys
import glob


NOISE_LINE_PATTERNS = [
    r'^\s*Your browser does not support the audio element\s*$',
    r'^\s*Audio\s*$',
    r'^\s*0:00/\d+:\d+\s*$',
    r'^\s*Speed Click below to adjust the playback speed\.\s*$',
    r'^\s*[\d.]+x[\d.]+x[\d.]+x[\d.]+x[\d.]+x[\d.]+x[\d.]+x\s*$',
    r'^\s*0:00Full VideoHighlight Video\s*$',
    r'^\s*Click to copy link\s*$',
    r'^\s*Speech link copied\s*$',
    r'^\s*Speech link copiedDevotional\s*$',
    r'^\s*Click to copy link\s*Speech link copied.*$',
    r'^\s*Play\s*$',
    r'^\s*Pause\s*$',
    r'^\s*-10 secs\s*$',
    r'^\s*\+10 secs\s*$',
    r'^\s*1x\s*$',
    r'^\s*Volume\s*$',
    r'^\s*Muted\s*$',
    r'^\s*Download\s*$',
    r'^\s*More\s*$',
    r'^\s*Dismiss\s*$',
    r'^\s*Your download has started.*$',
    r'^\s*Listen\s*$',
    r'^\s*PDF generation in progress\.+\s*$',
    r'^\s*Home > Speeches > .*$',
    r'^\s*Download Photo[s]?\s*$',
    # Bracketed language selector fragments: "[DE", "EN -", "IT]", "DE]"
    r'^\s*\[?\s*(DE|EN|ES|FR|IT|PL|PT|KO|JA|ZH|RU|JP)\s*-\s*\]?\s*$',
    r'^\s*\[\s*(DE|EN|ES|FR|IT|PL|PT|KO|JA|ZH|RU|JP)\s*\]?\s*$',
    r'^\s*(DE|EN|ES|FR|IT|PL|PT|KO|JA|ZH|RU|JP)\s*\]\s*$',
    # Stray standalone brackets from language selector blocks
    r'^\s*\[\s*$',
    r'^\s*\]\s*$',
]


def strip_lang_selector(text: str) -> str:
    """Remove blocks like 'DE\\n - EN\\n - ES\\n ...' (consecutive language codes)."""
    pattern = re.compile(
        r'\n\s*(DE|EN|ES|FR|IT|PL|PT|KO|JA|ZH|RU)\s*\n'
        r'(\s*-\s*(DE|EN|ES|FR|IT|PL|PT|KO|JA|ZH|RU)\s*\n)+',
        re.MULTILINE,
    )
    return pattern.sub('\n\n', text)


def strip_image_id_bullets(text: str) -> str:
    """Remove '- BN-AI-Guidelines-...jpg' or '- 1Y8A6542.jpeg' style bullets."""
    pattern = re.compile(
        r'^-\s*(BN-AI-Guidelines-|[0-9][A-Z][0-9][A-Z]?\d|IMG_|DSC_)[^\n]*\.(jpe?g|png|JPG|JPEG|PNG)\s*$',
        re.MULTILINE | re.IGNORECASE,
    )
    return pattern.sub('', text)


def strip_empty_bullets(text: str) -> str:
    return re.sub(r'^[ \t]*-[ \t]*$', '', text, flags=re.MULTILINE)


def strip_single_asterisk(text: str) -> str:
    return re.sub(r'^[ \t]*\*+[ \t]*$', '', text, flags=re.MULTILINE)


def collapse_blank(text: str) -> str:
    return re.sub(r'\n{3,}', '\n\n', text)


def normalize_file(path: str):
    with open(path, 'r') as f:
        content = f.read()
    orig_len = len(content)

    # Preserve frontmatter
    fm_match = re.match(r'^(---\n.*?\n---\n)', content, re.DOTALL)
    if fm_match:
        fm = fm_match.group(1)
        body = content[len(fm):]
    else:
        fm = ''
        body = content

    # Line-based removals
    lines = body.split('\n')
    new_lines = []
    for line in lines:
        if any(re.match(pat, line) for pat in NOISE_LINE_PATTERNS):
            continue
        new_lines.append(line)
    body = '\n'.join(new_lines)

    # Multi-line patterns
    body = strip_lang_selector(body)
    body = strip_image_id_bullets(body)
    body = strip_empty_bullets(body)
    body = strip_single_asterisk(body)
    body = collapse_blank(body)
    body = body.strip() + '\n'

    new = fm + body
    if new != content:
        with open(path, 'w') as f:
            f.write(new)
        return orig_len, len(new)
    return None


def main():
    if len(sys.argv) > 1:
        paths = sys.argv[1:]
    else:
        paths = sorted(
            glob.glob('sources/articles/*.md')
            + glob.glob('sources/notes/*.md')
            + glob.glob('sources/transcripts/*.md')
        )

    cleaned = []
    for path in paths:
        result = normalize_file(path)
        if result:
            cleaned.append((path, result))

    for p, (b, a) in cleaned:
        print(f'{p}: {b} → {a} ({b-a} chars removed)')
    print(f'\nTotal files cleaned: {len(cleaned)}')


if __name__ == '__main__':
    main()
