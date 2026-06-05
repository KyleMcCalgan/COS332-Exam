import hashlib
import re
from dataclasses import dataclass, field
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "ExamAdmin" / "MCQ Table.md"

SOURCES = [
    ("2023", "ST1", ROOT / "Past Papers" / "2023" / "SemTest1.md"),
    ("2023", "ST2", ROOT / "Past Papers" / "2023" / "SemTest2.md"),
    ("2023", "Exam", ROOT / "Past Papers" / "2023" / "Exam.md"),
    ("2024", "ST1", ROOT / "Past Papers" / "2024" / "COS332_ST1_2024_questions.md"),
    ("2024", "ST2", ROOT / "Past Papers" / "2024" / "COS332_ST2_2024_questions.md"),
    ("2024", "Exam", ROOT / "Past Papers" / "2024" / "COS332_FinalExam_2024_questions.md"),
    ("2025", "ST1", ROOT / "Past Papers" / "2025" / "COS332_ST1_2025_questions.md"),
    ("2025", "ST2", ROOT / "Past Papers" / "2025" / "COS332_ST2_2025_questions.md"),
    ("2025", "Exam", ROOT / "Past Papers" / "2025" / "Exam_2025_Question_Paper_questions.md"),
    ("2026", "ST1", ROOT / "Past Papers" / "2026" / "SemTest1.md"),
    ("2026", "ST2", ROOT / "Past Papers" / "2026" / "SemTest2.md"),
]

CURRENT_TEST_SOURCES = {"2026 ST1", "2026 ST2"}


@dataclass
class MCQ:
    year: str
    paper: str
    number: str
    stem: str
    options: list[str]
    source_path: Path
    occurrences: list[str] = field(default_factory=list)


def clean_text(value: str) -> str:
    replacements = {
        "\u2018": "'",
        "\u2019": "'",
        "\u201c": '"',
        "\u201d": '"',
        "\u2013": "-",
        "\u2014": "-",
        "\xa0": " ",
        "â€œ": '"',
        "â€\u009d": '"',
        "â€™": "'",
        "â€“": "-",
        "â€”": "-",
        "â‚": "_1",
        "â‚‚": "_2",
        "â‚ƒ": "_3",
        "â‚„": "_4",
        "â‚…": "_5",
        "â‚†": "_6",
        "â‚‡": "_7",
        "â‚ˆ": "_8",
        "â‚‰": "_9",
        "â‚€": "_0",
    }
    for old, new in replacements.items():
        value = value.replace(old, new)
    return value


def normalize(value: str) -> str:
    value = clean_text(value).lower()
    value = re.sub(r"`([^`]*)`", r"\1", value)
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def markdown_cell(value: str) -> str:
    value = clean_text(value).strip()
    value = value.replace("|", "\\|")
    value = value.replace("\r\n", "\n").replace("\r", "\n")
    value = re.sub(r"\n{3,}", "\n\n", value)
    rendered_lines = []
    for line in value.split("\n"):
        stripped = line.strip()
        if not stripped or stripped.startswith("```"):
            continue
        rendered_lines.append(stripped)
    return "<br>".join(rendered_lines)


def extract_question_one(text: str) -> list[str]:
    lines = text.splitlines()
    start = None
    for index, line in enumerate(lines):
        if re.match(r"^##\s+Question\s+1\b", line.strip(), re.I):
            start = index + 1
            break
    if start is None:
        return []

    end = len(lines)
    for index in range(start, len(lines)):
        if re.match(r"^##\s+Question\s+[2-9]\b", lines[index].strip(), re.I):
            end = index
            break
    return lines[start:end]


def is_heading_start(line: str) -> re.Match[str] | None:
    stripped = line.strip()
    return (
        re.match(r"^###\s+([A-Za-z]|\d+(?:\.\d+)?)[\.)]?\s*(.*)$", stripped)
        or re.match(r"^\*\*([A-Za-z]|\d+(?:\.\d+)?)\)\*\*\s*(.*)$", stripped)
    )


def is_numbered_start(line: str) -> re.Match[str] | None:
    return re.match(r"^(\d+)\.\s+(.+)$", line.strip())


def is_option(line: str) -> re.Match[str] | None:
    return re.match(r"^\s*(?:-\s*)?([A-F])[\.:]\s+(.*)$", line)


def parse_block(block: list[str], year: str, paper: str, number: str, path: Path) -> MCQ | None:
    option_lines: list[str] = []
    stem_lines: list[str] = []
    in_options = False
    current_option = ""

    for raw in block:
        line = raw.rstrip()
        if line.strip() == "---" or re.match(r"^\**\[\d+\]\**$", line.strip()):
            continue
        option_match = is_option(line)
        if option_match:
            in_options = True
            if current_option:
                option_lines.append(current_option.strip())
            current_option = f"{option_match.group(1)}. {option_match.group(2).strip()}"
            continue

        if in_options:
            if line.strip():
                current_option += " " + line.strip()
            continue

        stem_lines.append(line)

    if current_option:
        option_lines.append(current_option.strip())

    stem = "\n".join(stem_lines).strip()
    if not stem or len(option_lines) < 2:
        return None

    source_label = f"{year} {paper} Q1.{number}"
    return MCQ(year, paper, number, stem, option_lines, path, [source_label])


def parse_source(year: str, paper: str, path: Path) -> list[MCQ]:
    text = clean_text(path.read_text(encoding="utf-8"))
    lines = extract_question_one(text)
    questions: list[MCQ] = []
    current_number = ""
    current_block: list[str] = []

    def flush() -> None:
        nonlocal current_number, current_block
        if current_number and current_block:
            mcq = parse_block(current_block, year, paper, current_number, path)
            if mcq:
                questions.append(mcq)
        current_number = ""
        current_block = []

    for line in lines:
        heading_match = is_heading_start(line)
        numbered_match = is_numbered_start(line) if not heading_match else None

        if heading_match:
            flush()
            current_number = heading_match.group(1)
            remainder = heading_match.group(2).strip()
            current_block = [remainder] if remainder else []
            continue

        if numbered_match:
            flush()
            current_number = numbered_match.group(1)
            current_block = [numbered_match.group(2).strip()]
            continue

        if current_number:
            current_block.append(line)

    flush()
    return questions


def dedupe(mcqs: list[MCQ]) -> list[MCQ]:
    by_key: dict[str, MCQ] = {}

    for mcq in mcqs:
        key = normalize(mcq.stem)
        if not key:
            key = hashlib.sha1(mcq.stem.encode("utf-8")).hexdigest()

        existing = by_key.get(key)
        if existing is None:
            by_key[key] = mcq
            continue

        existing.occurrences.extend(mcq.occurrences)
        if len(mcq.options) > len(existing.options):
            existing.options = mcq.options

    return list(by_key.values())


def sortable_number(value: str) -> tuple[int, ...]:
    numbers = re.findall(r"\d+", value)
    if numbers:
        return tuple(int(number) for number in numbers)
    if len(value) == 1 and value.isalpha():
        return (ord(value.lower()) - ord("a") + 1,)
    return (9999,)


def build_table(rows: list[MCQ], source_counts: dict[str, int]) -> str:
    lines = [
        "# COS332 MCQ Table",
        "",
        "This table contains deduplicated multiple-choice questions extracted from available question markdown files in `Past Papers/`. The `Asked in 2026 Sem Tests` column marks questions already asked in the two current semester tests (`2026 ST1` and `2026 ST2`).",
        "",
        "## 2023 Placeholder",
        "",
        "> 2023 question markdown has now been included. Keep this section as an insertion point if extra 2023 material is added later.",
        "",
        "## Extraction Summary",
        "",
        "| Source | Extracted MCQs |",
        "|---|---:|",
    ]

    for source, count in source_counts.items():
        lines.append(f"| {source} | {count} |")

    lines.extend(
        [
            f"| **Unique total** | **{len(rows)}** |",
            "",
            "## Unique MCQs",
            "",
            "| # | Asked in 2026 Sem Tests | Occurrences | First Source | Question | Options | Study Status |",
            "|---:|---|---|---|---|---|---|",
        ]
    )

    for index, row in enumerate(rows, start=1):
        current_hits = [hit for hit in row.occurrences if " ".join(hit.split()[:2]) in CURRENT_TEST_SOURCES]
        asked = ", ".join(hit.split(" Q1.")[0] for hit in current_hits) if current_hits else ""
        status = "Skip for exam review" if current_hits else "Learn / review"
        occurrences = "; ".join(row.occurrences)
        first_source = row.occurrences[0]
        options = "\n".join(row.options)
        lines.append(
            "| {index} | {asked} | {occurrences} | {first_source} | {question} | {options} | {status} |".format(
                index=index,
                asked=markdown_cell(asked),
                occurrences=markdown_cell(occurrences),
                first_source=markdown_cell(first_source),
                question=markdown_cell(row.stem),
                options=markdown_cell(options),
                status=markdown_cell(status),
            )
        )

    lines.append("")
    return "\n".join(lines)


def main() -> None:
    all_mcqs: list[MCQ] = []
    source_counts: dict[str, int] = {}

    for year, paper, path in SOURCES:
        label = f"{year} {paper}"
        if not path.exists():
            source_counts[label] = 0
            continue
        mcqs = parse_source(year, paper, path)
        source_counts[label] = len(mcqs)
        all_mcqs.extend(mcqs)

    unique = dedupe(all_mcqs)
    unique.sort(key=lambda item: (item.year, {"ST1": 0, "ST2": 1, "Exam": 2}.get(item.paper, 9), sortable_number(item.number)))

    OUTPUT.write_text(build_table(unique, source_counts), encoding="utf-8")
    print(f"Wrote {len(unique)} unique MCQs from {sum(source_counts.values())} extracted MCQs to {OUTPUT}")


if __name__ == "__main__":
    main()
