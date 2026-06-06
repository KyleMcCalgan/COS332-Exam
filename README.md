# COS332 Exam Study Hub

This repository is a personal study workspace for the University of Pretoria
COS332 computer networks module. It brings course notes, past papers, extracted
questions, answer data, and browser-based revision tools into one place.

The main goal is to make exam preparation faster by:

- separating Semester Test 1 and Semester Test 2 notes;
- collecting past papers and their Markdown transcriptions by year;
- deduplicating multiple-choice questions across papers;
- grouping long questions by year, paper, and topic;
- highlighting questions already asked in the 2026 semester tests; and
- providing interactive MCQ, long-question, and subnetting practice pages.

## Getting Started

The repository is a static website. No installation is required for normal
study use.

Open `index.html` in a browser, or serve the repository locally:

```powershell
python -m http.server 8000
```

Then visit <http://localhost:8000>.

The landing page links to:

- Semester Test 1 notes;
- Semester Test 2 notes;
- the MCQ Explorer;
- the Long Questions Explorer; and
- the Practical Work hub.

## Repository Structure

```text
.
|-- index.html                 # Main navigation page
|-- Docs/                      # Browser-ready study notes
|   |-- ST1Notes/              # ST1 note website
|   `-- ST2Notes/              # ST2 note website and long-question guide
|-- Markdown/                  # Editable Markdown study-note sources
|   |-- s1/                    # Semester Test 1 material
|   |-- s2/                    # Semester Test 2 material
|   |-- exam/                  # Final-exam material
|   `-- practical work/        # Practical explanations and exercises
|-- Notes/                     # Original or reference PDF notes
|-- Past Papers/               # Papers, scans, memos, and transcriptions
|   |-- 2020/
|   |-- 2022/
|   |-- 2023/
|   |-- 2024/
|   |-- 2025/
|   `-- 2026/
|-- ExamAdmin/                 # Question banks, answer data, and study tools
|   `-- Practical Work/        # Index and focused interactive practical modules
|-- scripts/                   # Python generators and JavaScript validation
`-- .gitignore
```

### `Docs/`

Contains the HTML pages intended for reading in a browser.

- `ST1Notes/` covers the OSI model, user-facing and network-facing application
  layers, the presentation layer, and practical material.
- `ST2Notes/` covers layers 3 through 6 and includes long-question revision.

These pages are the published study interface. The related editable content is
kept under `Markdown/`. There is currently no single script that rebuilds all
note pages from the Markdown sources.

### `Markdown/`

Contains editable study material grouped by assessment:

- `s1/`: Semester Test 1 chapters;
- `s2/`: Semester Test 2 layer notes;
- `exam/`: exam-specific notes, including layers 1 and 2; and
- `practical work/`: practical topics such as UTF-8.

### `Notes/`

Contains the original PDF notes used as source or reference material. These are
useful when checking the accuracy or completeness of the Markdown and HTML
versions.

### `Past Papers/`

Stores source material by year. Depending on the year, a folder may contain:

- original PDF papers and memos;
- photographs or scans of a paper;
- Markdown transcriptions of questions; and
- plain-text memo transcriptions.

The question-generation scripts read the Markdown files listed explicitly in
their source tables. Adding a file to this directory does not automatically
include it in an explorer.

### `ExamAdmin/`

Contains the main revision artifacts:

- `MCQ Table.md`: deduplicated multiple-choice question bank;
- `MCQ Explorer.html`: interactive filtering and MCQ practice;
- `Long Questions Explorer.html`: filterable long-question collection;
- `Practical Work/index.html`: card-based index for interactive practical modules;
- `Practical Work/UTF-8 Explorer.html`: UTF-8 encoding, decoding, stream recovery,
  and generated practice;
- `Subnetting Explorer.html`: shared engine for focused Subnetting,
  Supernetting, Subnet Design, VLSM, Layer 1, Layer 2, and TCP practical pages;
- `answer_keys.json`: memo-backed MCQ answers;
- `llm_answers.json`: fallback generated MCQ answers;
- `long_question_memos.json`: supplemental long-question answer data; and
- `Exam Scope.txt`: working notes about the current exam scope.

Memo-backed answers take priority over generated answers in the MCQ Explorer.
Generated answers and study notes should still be checked against official
course material.

### `scripts/`

Contains standard-library Python scripts used to extract questions and build
study artifacts:

| Script | Purpose | Output |
| --- | --- | --- |
| `build_mcq_table.py` | Extracts and deduplicates MCQs from past-paper Markdown | `ExamAdmin/MCQ Table.md` |
| `build_mcq_explorer.py` | Builds the interactive MCQ page and attaches available answers | `ExamAdmin/MCQ Explorer.html` |
| `build_lq_explorer.py` | Builds the current long-question explorer structure | `ExamAdmin/Long Questions Explorer.html` |
| `build_longq_explorer.py` | Alternative older long-question parser and page builder | `ExamAdmin/Long Questions Explorer.html` |
| `check_mcq_explorer_js.js` | Checks that inline JavaScript in the MCQ Explorer parses | Console result |

Both long-question scripts write to the same output file. The checked-in Long
Questions Explorer also contains embedded memo functionality that is not
currently merged by either generator. Do not rebuild that page without first
preserving or automating the `long_question_memos.json` integration.

## Rebuilding Question Tools

Run commands from the repository root with Python 3:

```powershell
python scripts/build_mcq_table.py
python scripts/build_mcq_explorer.py
python scripts/build_lq_explorer.py
```

Node.js is only needed for the optional MCQ JavaScript syntax check:

```powershell
node scripts/check_mcq_explorer_js.js
```

When a new paper is added:

1. Place the original paper in `Past Papers/<year>/`.
2. Create a consistently structured Markdown transcription.
3. Add its year, paper type, and path to the relevant source list in the build
   scripts.
4. Add official answers to `ExamAdmin/answer_keys.json` when available.
5. Rebuild the affected table or explorer.
6. Open the generated page and check question boundaries, numbering, topics,
   answers, and filters.

## Data Flow

```text
PDFs, scans, and memos
        |
        v
Past-paper Markdown transcriptions
        |
        +--> build_mcq_table.py -----> MCQ Table.md
        |
        +--> build_mcq_explorer.py --> MCQ Explorer.html
        |
        `--> build_lq_explorer.py ---> Long Questions Explorer.html

Markdown study notes -----------> Docs HTML note pages
answer_keys.json / llm_answers.json --> MCQ Explorer answers
```

## Maintenance Notes

- Treat PDFs, scans, and photographs as source material rather than generated
  files.
- Prefer editing Markdown sources instead of generated HTML where a generator
  exists.
- Generated explorers embed their data directly in the HTML, so they can be
  opened without a backend.
- The source lists and parsers expect particular Markdown heading and question
  formats. Formatting changes can alter extraction results.
- Topic classification is keyword-based and should be reviewed after rebuilding.
- The workspace contains study aids, not authoritative course material. Verify
  uncertain answers against official memos, lectures, and prescribed material.
