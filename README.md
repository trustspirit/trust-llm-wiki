# LLM Wiki

Karpathy의 [LLM Wiki 패턴](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f) 기반 개인 지식베이스. Claude Code skills로 운영.

## 구조

```
.
├── SCHEMA.md                # ⭐ 작업 규칙 (LLM이 ingest/query/lint 시 반드시 읽음)
├── sources/                 # Raw, append-only
│   ├── articles/            # 웹 아티클·블로그
│   ├── pdfs/                # 논문·책
│   ├── transcripts/         # 유튜브·강연 자막
│   └── notes/               # 직접 쓴 노트
├── wiki/                    # LLM이 관리하는 합성 페이지
│   ├── index.md             # 토픽 허브
│   ├── people/
│   ├── concepts/
│   └── topics/
├── .meta/
│   ├── ingest-log.jsonl     # ingest 기록
│   └── backlinks.json       # 링크 그래프 (lint가 갱신)
└── .claude/skills/
    ├── wiki-ingest/         # 새 source 흡수
    ├── wiki-query/          # 위키에서 질문 답변
    └── wiki-lint/           # 품질 점검
```

## 사용

이 디렉토리에서 Claude Code를 띄우면 세 skill이 자동 로드됩니다.

```
cd ~/Documents/Workspace/llm-wiki
claude
```

- **ingest**: `이 URL 위키에 넣어줘 https://...` / `이 PDF ingest해줘 ./paper.pdf`
- **query**: `위키에서 RAG에 대해 알고 있는 거 알려줘`
- **lint**: `위키 점검해줘`

## 외부 도구

- `pdftotext` — PDF 텍스트 추출 (`brew install poppler`)
- `yt-dlp` — 유튜브 자막 (`brew install yt-dlp`)

## 첫 시작

1. SCHEMA.md를 한 번 정독 — 페이지 형식·인용 규약 확인
2. 첫 source 1개 ingest (예: Karpathy gist 자체) — 스키마가 현실에서 어떻게 깨지는지 확인
3. SCHEMA.md 다듬은 뒤 다음 source 들 흡수
4. 10~20개쯤 쌓이면 `wiki-lint` 한 번 돌려서 그래프 점검
