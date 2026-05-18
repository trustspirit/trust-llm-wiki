# Lint Checks & Commands

> 체크 항목 + 자동화 명령어. CLAUDE.md §5에서 pointer (wiki-lint skill 작업 시 Read).

## 1. 체크 항목

SCHEMA.md §Lint 기본 6개에 더해:

- "LDS" 약어 단독 사용 (URL/태그 외)
- "Mormon"이 *Book of Mormon* / 선지자 Mormon / Tabernacle Choir 외 사용
- 사도 호칭에서 "Elder" / "President" 누락
- 칠십인 호칭에서 "of the Seventy" 누락
- 영문 인용을 한국어로 옮길 때 "신" 단독 사용 (compound 제외)
- "도덕 행위성" 사용 (LDS 공식은 "도덕적 선택의지")

## 2. 자동화 명령어

wiki 루트에서 실행.

### 2.1. 용어 위반

```bash
grep -rn '\bLDS\b' wiki/ | grep -v 'tags:'
grep -rn '\bMormon\b' wiki/ | grep -v 'Book of Mormon'
grep -rn '\b신[이은을의과께]' wiki/ | grep -vE '신체|신앙|신뢰|신학|신성|신적|신중|신권|신호|미신|자신'
grep -rn '도덕 행위성\|도덕적 행위성' wiki/
```

### 2.2. 깨진 wikilink

```bash
grep -rohE '\[\[[a-z0-9-]+' wiki/ | sed 's/^\[\[//' | sort -u > /tmp/wl_used.txt
find wiki -name '*.md' -exec basename {} .md \; | sort -u > /tmp/wl_existing.txt
comm -23 /tmp/wl_used.txt /tmp/wl_existing.txt
```

### 2.3. 고아 페이지 (인바운드 링크 없음)

```bash
for f in $(find wiki/ -name '*.md' ! -name 'index.md'); do
  slug=$(basename "$f" .md)
  [ "$(grep -rl "\[\[$slug" wiki/ | grep -v "$f" | wc -l)" -eq 0 ] && echo "ORPHAN: $f"
done
```

### 2.4. 인용 없는 단정문 (bundle-citation-aware)

```bash
python3 .claude/scripts/lint-uncited.py
# 특정 파일만:
python3 .claude/scripts/lint-uncited.py wiki/concepts/<file>.md
```

Script 동작 (`.claude/scripts/lint-uncited.py`):

- 단정문(>40 chars, 마침표·물음표·느낌표 끝, header·table·blockquote 제외) 검출
- **묶음 인용 인식**: 같은 `##` 섹션 안에 (위쪽 30줄 lookback) `[source: ...]`가 있으면 skip — CLAUDE.md §1.4 권장 패턴 (섹션 헤더 lead-in에 source 명시) 대응
- 서브섹션(`###`, `####`)은 상위 `##` 인용을 상속 — boundary로 안 침

Naive grep (`grep -rn -E '[.!?]\s*$' wiki/ | grep -v '\[source:'`)은 false positive가 너무 많아 미사용.

### 2.5. 중복 / 근접 페이지 (frequency-aware)

```bash
python3 .claude/scripts/lint-duplicates.py
# 특정 디렉토리만:
python3 .claude/scripts/lint-duplicates.py wiki/concepts
```

Script 동작 (`.claude/scripts/lint-duplicates.py`):

- 디렉토리별로 title + aliases 토큰을 모음.
- **Frequency-aware stopwords**: 같은 디렉토리 페이지의 ≥30%에 등장하는 토큰은 common topic-vocabulary로 stopword 처리 (예: AI 클러스터의 'artificial', 'intelligence', 'ai').
- 그 후 Jaccard similarity 0.5 이상이면 후보로 surface.
- Source 중복은 ≥6개 공유 시만 flag (1-5개 공유는 자연스러움 — 같은 토픽 클러스터에서 흔함).
- 결과는 후보일 뿐, 실제 합병 여부는 사람 검토.

Naive alias-overlap grep은 도메인 stopword 처리가 없어 false positive 다수 — 미사용.

### 2.6. Source staleness

```bash
grep -rn '^published:' sources/ | sort
```

### 2.7. CONFLICT 마커 (활성만)

```bash
grep -rn 'CONFLICT' wiki/  # CONFLICT RESOLVED 마커는 [ingest-protocols.md §4.1] 위반
```

### 2.8. 중복 reference (frontmatter)

```bash
for f in $(find wiki -name '*.md'); do
  awk '/^sources:/{print FILENAME; gsub(/[][]/,""); n=split($0,a,","); for(i=1;i<=n;i++){gsub(/^ +| +$/,"",a[i]); print a[i]}}' "$f" | sort | uniq -c | awk '$1>1{print}'
done
```
