# Ingest Protocols

> Source 관리 + Wiki 페이지 관리 + 인용 + 충돌·정리 protocols. CLAUDE.md §3에서 pointer.

## 1. Source 관리

### 1.1. 불변 원칙 (SCHEMA §원칙 1)

`sources/` 파일은 절대 수정 금지. 새 정보는 새 source 파일로 추가, `wiki/`만 재작성.

### 1.2. Source 타입 가이드

| 입력 | type | 위치 |
|---|---|---|
| URL (article/blog) | `article` | `sources/articles/` |
| PDF | `pdf` | `sources/pdfs/` (+ pdftotext .txt) |
| YouTube transcript | `transcript` | `sources/transcripts/` |
| 사용자 직접 제공 텍스트 (공식 문서 발췌 포함) | `note` | `sources/notes/`. 머리말에 "Text provided by the user" provenance |
| Re-extraction (정정) | `note` | `-v2` 등 접미사. 이전 버전과 차이 명시 |

파일명: `sources/<type>/<YYYY-MM-DD>-<slug>.md` (date = `ingested:` 오늘). slug 충돌 시 `-2`, `-3` 추가, 절대 overwrite 금지.

### 1.3. Source 삭제 (불변 원칙 override)

다음 모두 충족 시 사용자 명시 요청으로 override 가능:

1. 사용자 명시 삭제 요청 (확인 질문 포함).
2. Replacement source가 동일 정보 포함, 또는 사용자가 정보 손실을 명시 수용.

```bash
rm sources/<path>
for f in $(grep -rl '<deleted-slug>' wiki/); do
  sed -i '' 's|<deleted-path>|<replacement-path>|g' "$f"
done
```

`ingest-log.jsonl`에 `{"event":"source_deletion","deleted":"...","reason":"...","replacement":"...","wiki_changed":[...]}` 기록.

Replacement 없는 경우(스코프 외 정리)는 §4.2 참조.

### 1.4. 다국어 변형 URL

같은 컨텐츠의 다른 언어판(예: `?lang=kor`) 제공 시:

1. 먼저 fetch 후 실제 번역 여부 확인.
2. **동일(미번역)**: 별도 source X. log에 `multilingual_variant` 메모만.
3. **실제 번역**: 별도 source 생성. 영어 source 머리말에 상호 참조.
4. wiki 본문 인용은 영어 권위본 1차, 번역본 보조.

### 1.5. SPA 차단 시 대안

`curl`로 본문 안 잡히는 client-rendered 페이지(예: `churchofjesuschrist.org` 핸드북) 대응:

1. **보도/매거진**: 동일 컨텐츠의 Newsroom 보도, *Liahona*/*Ensign* 재게재 활용.
2. **사용자 직접 제공**: 사용자가 본문 복사·붙여넣기 → §1.2의 `note`로 처리.
3. **추후 후보**: 둘 다 불가하면 `{"event":"ingest_attempt_failed","target":"...","reason":"SPA"}` 로그 + 위키에서 plain prose / 외부 링크.

### 1.6. Published 날짜 추출

- URL 경로 연-월(`/2024/11/`)을 1차 추정.
- 본문 "delivered on ... at ..." 명시가 있으면 우선.
- 끝내 모르면 `published:` 생략 (SCHEMA 허용). `ingested:`는 항상 오늘.

### 1.7. HTML 추출 노이즈 정리 (URL ingest 필수 단계)

URL에서 fetch → markdown 변환 시 HTML UI 요소(audio 플레이어 컨트롤, 언어 셀렉터, 이미지 placeholder, breadcrumb 등)가 본문에 섞여 들어온다. **URL ingest로 source 파일을 저장하기 직전에 반드시 정리**.

**정리 대상**:

- 오디오 플레이어 UI: `Your browser does not support the audio element`, `0:00/26:21`, `0.5x0.75x1.0x...`, Speed/Play/Pause/Volume/Muted/Download/More/Dismiss/Listen
- 네비게이션: `Click to copy link`, `Speech link copied`, `Full VideoHighlight Video`, `Home > Speeches > ...`, `PDF generation in progress.....`
- 언어 셀렉터: `DE\n - EN\n - ES\n ...` (대시 형) 또는 `[DE\n\nEN -\nES -\nIT]` (대괄호 형)
- 이미지 placeholder bullet: `- BN-AI-Guidelines-Elder-Gong-...jpg`, `- 1Y8A6542.jpeg`
- `Download Photo` / `Download Photos` 단독 줄
- 빈 bullet (`- `) 및 단독 `*` 줄
- Triple+ blank line → double

**사용 방법** (재사용 가능 script):

```bash
# 모든 sources 일괄 정리:
python3 .claude/scripts/strip-source-noise.py

# 특정 파일만:
python3 .claude/scripts/strip-source-noise.py sources/articles/<file>.md
```

Script는 idempotent (여러 번 실행 안전), frontmatter 보존, 본문만 정리.

**적용 시점**:

1. **URL ingest 시 권장**: `curl` + markdown 변환 → source 파일 저장 → **즉시** `strip-source-noise.py` 실행 → 그 결과를 commit.
2. **사용자 제공 텍스트(`note`)는 보통 깨끗** — 적용 X.
3. **PDF·transcript 추출본**: noise 패턴이 다르므로 별도 정리 (필요 시 script 보강).

**새 패턴 발견 시**:

- `.claude/scripts/strip-source-noise.py`의 `NOISE_LINE_PATTERNS` 또는 helper 함수에 추가.
- 모든 기존 sources에 재실행 (`python3 .claude/scripts/strip-source-noise.py`) — idempotent하므로 변경 없는 파일은 skip됨.
- `ingest-log.jsonl`에 `{"event":"noise_pattern_added","pattern":"...","files_cleaned":N}` 기록.

**불변 원칙(SCHEMA §1)과의 관계**:

이 정리는 **content modification이 아니라 extraction error correction** — HTML→markdown 변환 과정의 부산물 제거. 사용자가 즐기는 본문은 손상되지 않는다. URL ingest 표준 파이프라인의 일부.

## 2. Wiki 페이지 관리

### 2.1. 페이지 생성 임계값

**Substantive claim 1개 이상**일 때만 인물·개념·토픽 페이지 생성. 그렇지 않은 entity는 본문 산문에 평이 처리.

### 2.2. 임계값 예외 — 현직 인물

다음은 substantive claim 부족해도 stub 페이지 candidate:

- 현 회장 (the President of the Church)
- First Presidency 보좌
- Quorum of the Twelve Apostles 구성원

사유: wikilink가 본문에서 빈번하고, 향후 ingest로 누적 가능성 높음. Stub은 frontmatter + 직함·임명일·핵심 약력만.

### 2.3. 페이지 없는 인물의 본문 표기

- ❌ wikilink 사용 (깨진 링크 발생).
- ✅ 첫 언급은 **풀네임 + 직함**: "Elder John C. Pingree of the Seventy".
- 이후는 약식: "Elder Pingree".

### 2.4. 인물 직함·시점 변동 (Succession)

`sources/`는 그 시점 직함 그대로 immutable. `wiki/`는 현 시점 직함으로 갱신.

**별세·회장직 종료 인물**:

- frontmatter `title:`은 그대로.
- 본문 H1을 `# President <Name> (<birth>–<death>)` 형식으로.
- TL;DR에 "X대 회장 (재임 yyyy-mm-dd ~ yyyy-mm-dd)" 명시.
- `wiki/index.md`의 인물 묘사 갱신.

Historical context가 의미 있으면 "이전 직함으로서 …" 산문으로.

### 2.5. 다년·다무대 시리즈 표 (권장)

동일 인물·개념이 여러 무대에서 반복 다뤄지면 인물·개념 페이지에 **"주요 무대" 표**:

```
| 날짜 | 자리 | 주제 [source: ...] |
```

## 3. 인용

### 3.1. Hierarchy (원전 우선)

같은 명제가 여러 source에 있으면:

| 등급 | 종류 | 예시 |
|---|---|---|
| **1차** | 본인 speech·article·book·핸드북 원문 | Elder Bednar 본인 강연 |
| **2차** | Newsroom·매거진 보도, press release | Newsroom 발표 보도 |
| **3차** | 다른 인물·기자가 1차를 인용 | FSOY 기자가 Bednar 인용 |

규칙:

- 1차 가용하면 우선 인용.
- 1차 없으면 2차/3차 대체. 본문에 "원전 인용: <title>" 명시 + 향후 1차 ingest 후보 표시.
- 동일 인물이 여러 무대에서 같은 명제를 변형 발언한 경우 모두 1차로 시간순 인용 가능.
- **사도→사도 인용**: 두 source 다 인용 가능 (`[source: <원전>, <인용자>]`, 시간순). 원전이 위키에 ingest됐다면 wiki에서 원전만 인용해도 chain 유지.

### 3.2. 인용 위치 부가 표기 (권장)

긴 source에서 특정 위치 지목 시 `[source: ...]` 뒤에 괄호로:

- footnote: `[source: <path>] (footnote vi)`
- 핸드북 절: `[source: <path>] (§38.8.48.3)`
- 동일 인물 다무대 구분: `[source: <path>] (Rome 2025-10)`

## 4. 충돌과 정리

### 4.1. CONFLICT 마커 lifecycle

- ✅ **활성 분쟁**: `<!-- CONFLICT: ... -->` 마커 + 사용자에게 알림 + 본문에 양쪽 해석 보존.
- ✅ **해소 시**: 마커 제거 + 본문 평이 산문화. Audit trail은 `ingest-log.jsonl`의 `{"event":"conflict_resolved","prior_marker":"...","resolution":"..."}`에 보존.
- ❌ `<!-- CONFLICT RESOLVED: ... -->` 같은 후처리 마커 금지 — Lint noise + 이력 중복.

### 4.2. 외부 스코프 cluster 정리

CLAUDE.md §1의 보조 source 정당화 조건("1차 source가 명시적 인용")이 무효해진 cluster 정리. 사용자 요청 또는 분기별 lint로.

절차:

1. Source 파일 삭제.
2. 인물·개념·토픽 페이지 삭제 (`rm wiki/<type>/<slug>.md`).
3. 잔여 reference 정리 — `grep -rln '<keyword>' wiki/` 결과 각 페이지의 (a) frontmatter `sources:` (b) 본문 섹션 (c) See also wikilink 모두.
4. `wiki/index.md`에서 bullet 제거.
5. `ingest-log.jsonl`에 `scope_cleanup` event.
6. **같은 cluster 안에서도 1차 source가 직접 인용한 항목은 유지** (예: *Antiqua et Nova*는 Elder Gong이 직접 인용 → 유지).
