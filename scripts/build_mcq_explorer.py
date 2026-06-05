import html
import json
import re
from pathlib import Path

from build_mcq_table import CURRENT_TEST_SOURCES, SOURCES, dedupe, parse_source, sortable_number


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "ExamAdmin" / "MCQ Explorer.html"
ANSWER_KEYS_PATH = ROOT / "ExamAdmin" / "answer_keys.json"
LLM_ANSWERS_PATH = ROOT / "ExamAdmin" / "llm_answers.json"


def load_answer_keys() -> dict:
    if not ANSWER_KEYS_PATH.exists():
        return {}
    return json.loads(ANSWER_KEYS_PATH.read_text(encoding="utf-8"))


def load_llm_answers() -> dict:
    if not LLM_ANSWERS_PATH.exists():
        return {}
    return json.loads(LLM_ANSWERS_PATH.read_text(encoding="utf-8"))


def resolve_answer(occurrences: list[str], answer_keys: dict, llm_answers: dict) -> tuple[str | None, str | None]:
    for occ in occurrences:
        try:
            source, q_num = occ.split(" Q1.", 1)
            answer = answer_keys.get(source, {}).get(q_num)
            if answer:
                return answer, "memo"
        except ValueError:
            pass
    for occ in occurrences:
        try:
            source, q_num = occ.split(" Q1.", 1)
            answer = llm_answers.get(source, {}).get(q_num)
            if answer:
                return answer, "llm"
        except ValueError:
            pass
    return None, None


def source_from_occurrence(occurrence: str) -> str:
    return occurrence.split(" Q1.")[0]


def make_rows():
    all_mcqs = []
    source_counts = {}
    answer_keys = load_answer_keys()
    llm_answers = load_llm_answers()

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

    rows = []
    for index, item in enumerate(unique, start=1):
        source_labels = [source_from_occurrence(occurrence) for occurrence in item.occurrences]
        current_hits = [label for label in source_labels if label in CURRENT_TEST_SOURCES]
        years = sorted({label.split()[0] for label in source_labels})
        papers = sorted({label.split()[1] for label in source_labels}, key=lambda paper: {"ST1": 0, "ST2": 1, "Exam": 2}.get(paper, 9))

        answer, answer_source = resolve_answer(item.occurrences, answer_keys, llm_answers)

        rows.append(
            {
                "id": index,
                "question": item.stem,
                "options": item.options,
                "occurrences": item.occurrences,
                "sourceLabels": source_labels,
                "years": years,
                "papers": papers,
                "firstSource": item.occurrences[0],
                "firstYear": item.year,
                "firstPaper": item.paper,
                "occurrenceCount": len(item.occurrences),
                "askedCurrent": bool(current_hits),
                "askedCurrentSources": sorted(set(current_hits)),
                "studyStatus": "Skip for exam review" if current_hits else "Learn / review",
                "correctAnswer": answer,
                "answerSource": answer_source,
            }
        )

    return rows, source_counts


def build_html(rows, source_counts):
    years = sorted({year for row in rows for year in row["years"]})
    papers = ["ST1", "ST2", "Exam"]
    sources = [source for source in source_counts if source_counts[source] > 0]
    data_json = json.dumps(rows, ensure_ascii=False).replace("</", "<\\/")
    summary_json = json.dumps(source_counts, ensure_ascii=False).replace("</", "<\\/")

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>COS332 MCQ Explorer</title>
  <style>
    :root {{
      --bg: #f6f7f9;
      --panel: #ffffff;
      --text: #17202a;
      --muted: #5d6978;
      --line: #d9dee7;
      --accent: #0f766e;
      --accent-soft: #d7f3ef;
      --warn: #a16207;
      --warn-soft: #fff0c2;
      --shadow: 0 10px 30px rgba(23, 32, 42, 0.08);
    }}

    * {{ box-sizing: border-box; }}

    body {{
      margin: 0;
      font-family: Arial, Helvetica, sans-serif;
      background: var(--bg);
      color: var(--text);
      letter-spacing: 0;
    }}

    header {{
      background: #ffffff;
      border-bottom: 1px solid var(--line);
    }}

    .wrap {{
      width: min(1440px, calc(100% - 32px));
      margin: 0 auto;
    }}

    .topbar {{
      display: flex;
      align-items: flex-end;
      justify-content: space-between;
      gap: 24px;
      padding: 24px 0 18px;
    }}

    h1 {{
      margin: 0 0 6px;
      font-size: 28px;
      line-height: 1.15;
    }}

    .subtitle {{
      margin: 0;
      color: var(--muted);
      font-size: 14px;
      line-height: 1.45;
    }}

    .stats {{
      display: grid;
      grid-template-columns: repeat(3, minmax(110px, 1fr));
      gap: 10px;
      min-width: 380px;
    }}

    .stat {{
      background: #f8fafc;
      border: 1px solid var(--line);
      border-radius: 8px;
      padding: 10px 12px;
    }}

    .stat b {{
      display: block;
      font-size: 22px;
      line-height: 1.1;
    }}

    .stat span {{
      display: block;
      margin-top: 3px;
      color: var(--muted);
      font-size: 12px;
    }}

    main {{
      padding: 18px 0 32px;
    }}

    .filters {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      box-shadow: var(--shadow);
      padding: 14px;
      margin-bottom: 16px;
    }}

    .filter-grid {{
      display: grid;
      grid-template-columns: minmax(220px, 1.4fr) minmax(160px, 0.7fr) minmax(160px, 0.7fr) minmax(180px, 0.8fr);
      gap: 12px;
      align-items: end;
    }}

    label {{
      display: block;
      color: var(--muted);
      font-size: 12px;
      font-weight: 700;
      margin-bottom: 6px;
      text-transform: uppercase;
    }}

    input[type="search"],
    select {{
      width: 100%;
      height: 40px;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: #fff;
      color: var(--text);
      padding: 0 10px;
      font-size: 14px;
    }}

    .checks {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      min-height: 40px;
      align-items: center;
    }}

    .check {{
      display: inline-flex;
      align-items: center;
      gap: 6px;
      border: 1px solid var(--line);
      border-radius: 999px;
      padding: 7px 10px;
      background: #fff;
      font-size: 13px;
      white-space: nowrap;
    }}

    .check input {{
      margin: 0;
      accent-color: var(--accent);
    }}

    .filter-row {{
      display: grid;
      grid-template-columns: minmax(220px, 1fr) minmax(220px, 1fr) minmax(160px, 0.5fr);
      gap: 12px;
      margin-top: 12px;
      align-items: end;
    }}

    .actions {{
      display: flex;
      gap: 8px;
      align-items: center;
      justify-content: flex-end;
    }}

    button {{
      height: 40px;
      border: 1px solid var(--line);
      border-radius: 8px;
      background: #fff;
      color: var(--text);
      padding: 0 12px;
      font-size: 14px;
      cursor: pointer;
    }}

    button.primary {{
      background: var(--accent);
      border-color: var(--accent);
      color: #fff;
    }}

    .result-meta {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 12px;
      margin: 10px 0 12px;
      color: var(--muted);
      font-size: 13px;
    }}

    .view {{
      display: grid;
      gap: 10px;
    }}

    .mcq {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      box-shadow: 0 4px 16px rgba(23, 32, 42, 0.05);
      overflow: hidden;
    }}

    .mcq-head {{
      display: grid;
      grid-template-columns: 54px minmax(0, 1fr) auto;
      gap: 12px;
      align-items: start;
      padding: 14px;
      border-bottom: 1px solid var(--line);
    }}

    .mcq-id {{
      width: 42px;
      height: 32px;
      display: grid;
      place-items: center;
      border-radius: 8px;
      background: #edf1f5;
      color: #344054;
      font-weight: 700;
      font-size: 13px;
    }}

    .question {{
      margin: 0;
      font-size: 15px;
      line-height: 1.48;
    }}

    .badges {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      justify-content: flex-end;
    }}

    .badge {{
      display: inline-flex;
      align-items: center;
      min-height: 24px;
      border-radius: 999px;
      padding: 4px 8px;
      background: #eef2f7;
      color: #344054;
      font-size: 12px;
      font-weight: 700;
      white-space: nowrap;
    }}

    .badge.seen {{
      background: var(--warn-soft);
      color: var(--warn);
    }}

    .badge.review {{
      background: var(--accent-soft);
      color: var(--accent);
    }}

    .mcq-body {{
      display: grid;
      grid-template-columns: minmax(260px, 1fr) minmax(220px, 0.72fr);
      gap: 14px;
      padding: 14px;
    }}

    .options {{
      margin: 0;
      padding-left: 0;
      list-style: none;
      display: grid;
      gap: 7px;
    }}

    .options li {{
      padding: 0;
      background: transparent;
      border: none;
      border-radius: 0;
      font-size: 14px;
      line-height: 1.35;
    }}

    .option-btn {{
      display: block;
      width: 100%;
      text-align: left;
      padding: 8px 10px;
      background: #f8fafc;
      border: 1px solid #e6ebf2;
      border-radius: 8px;
      font-size: 14px;
      line-height: 1.35;
      cursor: pointer;
      color: var(--text);
      font-family: inherit;
      transition: background 0.12s, border-color 0.12s;
    }}

    .option-btn:hover:not(:disabled) {{
      background: #eef2f7;
      border-color: #c5cdd9;
    }}

    .option-btn.correct {{
      background: #d1fae5;
      border-color: #34d399;
      color: #065f46;
      font-weight: 700;
    }}

    .option-btn.incorrect {{
      background: #fee2e2;
      border-color: #f87171;
      color: #991b1b;
    }}

    .option-btn:disabled {{
      cursor: default;
    }}

    .quiz-footer {{
      display: flex;
      align-items: center;
      gap: 10px;
      margin-top: 8px;
    }}

    .quiz-result {{
      font-size: 13px;
      font-weight: 700;
    }}

    .quiz-result.correct {{ color: #065f46; }}
    .quiz-result.incorrect {{ color: #991b1b; }}
    .quiz-result.unknown {{ color: var(--muted); }}

    .reset-btn {{
      height: 28px;
      font-size: 12px;
      padding: 0 10px;
      border: 1px solid var(--line);
      border-radius: 6px;
      background: #fff;
      cursor: pointer;
      color: var(--muted);
      font-family: inherit;
    }}

    .reset-btn:hover {{ background: #f1f5f9; }}

    .detail {{
      display: grid;
      gap: 10px;
      align-content: start;
    }}

    .detail-block {{
      border-left: 3px solid var(--line);
      padding-left: 10px;
    }}

    .detail-title {{
      color: var(--muted);
      font-size: 12px;
      font-weight: 700;
      margin-bottom: 4px;
      text-transform: uppercase;
    }}

    .detail-text {{
      font-size: 13px;
      line-height: 1.4;
    }}

    .empty {{
      background: var(--panel);
      border: 1px dashed var(--line);
      border-radius: 8px;
      padding: 30px;
      text-align: center;
      color: var(--muted);
    }}

    @media (max-width: 960px) {{
      .topbar {{
        align-items: stretch;
        flex-direction: column;
      }}

      .stats {{
        min-width: 0;
      }}

      .filter-grid,
      .filter-row,
      .mcq-body {{
        grid-template-columns: 1fr;
      }}

      .actions {{
        justify-content: flex-start;
      }}
    }}

    @media (max-width: 640px) {{
      .wrap {{
        width: min(100% - 20px, 1440px);
      }}

      .topbar {{
        padding-top: 18px;
      }}

      h1 {{
        font-size: 23px;
      }}

      .stats {{
        grid-template-columns: 1fr;
      }}

      .filters {{
        padding: 12px;
      }}

      .mcq-head {{
        grid-template-columns: 42px minmax(0, 1fr);
      }}

      .badges {{
        grid-column: 1 / -1;
        justify-content: flex-start;
      }}
    }}
  </style>
</head>
<body>
  <header>
    <div class="wrap topbar">
      <div>
        <h1>COS332 MCQ Explorer</h1>
        <p class="subtitle">Filter, sort, and review deduplicated MCQs from the past paper markdown set.</p>
      </div>
      <div class="stats">
        <div class="stat"><b id="stat-total">{len(rows)}</b><span>unique questions</span></div>
        <div class="stat"><b id="stat-visible">{len(rows)}</b><span>visible now</span></div>
        <div class="stat"><b id="stat-seen">0</b><span>seen in 2026 tests</span></div>
      </div>
    </div>
  </header>

  <main>
    <div class="wrap">
      <section class="filters" aria-label="Filters">
        <div class="filter-grid">
          <div>
            <label for="search">Search</label>
            <input id="search" type="search" placeholder="Search question text, options, or source">
          </div>
          <div>
            <label for="seen">Seen status</label>
            <select id="seen">
              <option value="all">All questions</option>
              <option value="unseen">Only learn / review</option>
              <option value="seen">Only seen in 2026 tests</option>
            </select>
          </div>
          <div>
            <label for="sort">Sort</label>
            <select id="sort">
              <option value="source">First source</option>
              <option value="occurrences-desc">Most repeated</option>
              <option value="occurrences-asc">Least repeated</option>
              <option value="status">Study status</option>
              <option value="question">Question text</option>
              <option value="id">Table order</option>
            </select>
          </div>
          <div>
            <label for="source">Specific paper</label>
            <select id="source">
              <option value="all">All papers</option>
              {"".join(f'<option value="{html.escape(source)}">{html.escape(source)} ({source_counts[source]})</option>' for source in sources)}
            </select>
          </div>
        </div>

        <div class="filter-row">
          <div>
            <label>Years</label>
            <div class="checks" id="yearChecks">
              {"".join(f'<label class="check"><input type="checkbox" value="{html.escape(year)}" checked> {html.escape(year)}</label>' for year in years)}
            </div>
          </div>
          <div>
            <label>Paper types</label>
            <div class="checks" id="paperChecks">
              {"".join(f'<label class="check"><input type="checkbox" value="{html.escape(paper)}" checked> {html.escape(paper)}</label>' for paper in papers)}
            </div>
          </div>
          <div class="actions">
            <button id="reset" type="button">Reset</button>
            <button id="copyVisible" class="primary" type="button">Copy visible</button>
          </div>
        </div>
      </section>

      <div class="result-meta">
        <span id="resultText"></span>
        <span id="sourceText"></span>
      </div>

      <section id="results" class="view" aria-live="polite"></section>
    </div>
  </main>

  <script>
    const DATA = {data_json};
    const SOURCE_COUNTS = {summary_json};

    const state = {{
      search: "",
      seen: "all",
      sort: "source",
      source: "all",
      years: new Set({json.dumps(years)}),
      papers: new Set({json.dumps(papers)})
    }};

    const els = {{
      search: document.getElementById("search"),
      seen: document.getElementById("seen"),
      sort: document.getElementById("sort"),
      source: document.getElementById("source"),
      yearChecks: document.getElementById("yearChecks"),
      paperChecks: document.getElementById("paperChecks"),
      results: document.getElementById("results"),
      resultText: document.getElementById("resultText"),
      sourceText: document.getElementById("sourceText"),
      statVisible: document.getElementById("stat-visible"),
      statSeen: document.getElementById("stat-seen"),
      reset: document.getElementById("reset"),
      copyVisible: document.getElementById("copyVisible")
    }};

    const paperRank = {{ ST1: 0, ST2: 1, Exam: 2 }};

    function textOf(row) {{
      return [
        row.question,
        row.options.join(" "),
        row.occurrences.join(" "),
        row.studyStatus
      ].join(" ").toLowerCase();
    }}

    function sourceParts(source) {{
      const parts = source.split(" ");
      return {{ year: parts[0], paper: parts[1] }};
    }}

    function firstSourceSort(a, b) {{
      const aa = sourceParts(a.sourceLabels[0]);
      const bb = sourceParts(b.sourceLabels[0]);
      const yearCompare = Number(aa.year) - Number(bb.year);
      if (yearCompare !== 0) return yearCompare;
      const paperCompare = (paperRank[aa.paper] ?? 9) - (paperRank[bb.paper] ?? 9);
      if (paperCompare !== 0) return paperCompare;
      return a.id - b.id;
    }}

    function selectedValues(container) {{
      return new Set([...container.querySelectorAll("input:checked")].map(input => input.value));
    }}

    function applyFilters() {{
      state.search = els.search.value.trim().toLowerCase();
      state.seen = els.seen.value;
      state.sort = els.sort.value;
      state.source = els.source.value;
      state.years = selectedValues(els.yearChecks);
      state.papers = selectedValues(els.paperChecks);

      let rows = DATA.filter(row => {{
        if (state.search && !textOf(row).includes(state.search)) return false;
        if (state.seen === "seen" && !row.askedCurrent) return false;
        if (state.seen === "unseen" && row.askedCurrent) return false;
        if (state.source !== "all" && !row.sourceLabels.includes(state.source)) return false;
        if (!row.years.some(year => state.years.has(year))) return false;
        if (!row.papers.some(paper => state.papers.has(paper))) return false;
        return true;
      }});

      rows.sort((a, b) => {{
        if (state.sort === "occurrences-desc") return b.occurrenceCount - a.occurrenceCount || firstSourceSort(a, b);
        if (state.sort === "occurrences-asc") return a.occurrenceCount - b.occurrenceCount || firstSourceSort(a, b);
        if (state.sort === "status") return Number(a.askedCurrent) - Number(b.askedCurrent) || firstSourceSort(a, b);
        if (state.sort === "question") return a.question.localeCompare(b.question) || firstSourceSort(a, b);
        if (state.sort === "id") return a.id - b.id;
        return firstSourceSort(a, b);
      }});

      render(rows);
      return rows;
    }}

    function escapeHtml(value) {{
      return String(value)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
    }}

    function render(rows) {{
      const seenCount = rows.filter(row => row.askedCurrent).length;
      els.statVisible.textContent = rows.length;
      els.statSeen.textContent = DATA.filter(row => row.askedCurrent).length;
      els.resultText.textContent = `${{rows.length}} visible, ${{seenCount}} seen in 2026 tests`;
      els.sourceText.textContent = state.source === "all" ? "All sources" : state.source;

      if (!rows.length) {{
        els.results.innerHTML = '<div class="empty">No MCQs match the current filters.</div>';
        return;
      }}

      els.results.innerHTML = rows.map(row => {{
        const statusClass = row.askedCurrent ? "seen" : "review";
        const statusText = row.askedCurrent ? `Seen: ${{row.askedCurrentSources.join(", ")}}` : "Learn / review";
        const correctAttr = row.correctAnswer ? ` data-correct="${{escapeHtml(row.correctAnswer)}}"` : "";
        const sourceAttr = row.answerSource ? ` data-source="${{escapeHtml(row.answerSource)}}"` : "";
        const optionItems = row.options.map(option => {{
          const letter = option.split(".")[0].trim();
          return `<li><button class="option-btn" data-letter="${{escapeHtml(letter)}}" type="button">${{escapeHtml(option)}}</button></li>`;
        }}).join("");
        const occurrenceText = row.occurrences.join("; ");
        const sourceText = row.sourceLabels.join(", ");
        const llmBadge = row.answerSource === 'llm' ? `<span class="badge" style="background:#fef08a;color:#c2410c">LLM Answered</span>` : "";
        
        return `
          <article class="mcq" data-id="${{row.id}}"${{correctAttr}}${{sourceAttr}}>
            <div class="mcq-head">
              <div class="mcq-id">#${{row.id}}</div>
              <p class="question">${{escapeHtml(row.question)}}</p>
              <div class="badges">
                ${{llmBadge}}
                <span class="badge ${{statusClass}}">${{escapeHtml(statusText)}}</span>
                <span class="badge">${{row.occurrenceCount}}x</span>
              </div>
            </div>
            <div class="mcq-body">
              <div>
                <ol class="options">${{optionItems}}</ol>
                <div class="quiz-footer">
                  <span class="quiz-result"></span>
                  <button class="reset-btn" type="button" style="display:none">Try again</button>
                </div>
              </div>
              <div class="detail">
                <div class="detail-block">
                  <div class="detail-title">Occurrences</div>
                  <div class="detail-text">${{escapeHtml(occurrenceText)}}</div>
                </div>
                <div class="detail-block">
                  <div class="detail-title">Papers</div>
                  <div class="detail-text">${{escapeHtml(sourceText)}}</div>
                </div>
                <div class="detail-block">
                  <div class="detail-title">First source</div>
                  <div class="detail-text">${{escapeHtml(row.firstSource)}}</div>
                </div>
              </div>
            </div>
          </article>
        `;
      }}).join("");
    }}

    function resetFilters() {{
      els.search.value = "";
      els.seen.value = "all";
      els.sort.value = "source";
      els.source.value = "all";
      [...document.querySelectorAll('.checks input')].forEach(input => input.checked = true);
      applyFilters();
    }}

    async function copyVisible() {{
      const rows = applyFilters();
      const text = rows.map(row => [
        `#${{row.id}} ${{row.question}}`,
        row.options.join("\\n"),
        `Occurrences: ${{row.occurrences.join("; ")}}`,
        `Status: ${{row.studyStatus}}`
      ].join("\\n")).join("\\n\\n---\\n\\n");

      try {{
        await navigator.clipboard.writeText(text);
        els.copyVisible.textContent = "Copied";
        setTimeout(() => els.copyVisible.textContent = "Copy visible", 1000);
      }} catch {{
        els.copyVisible.textContent = "Copy failed";
        setTimeout(() => els.copyVisible.textContent = "Copy visible", 1400);
      }}
    }}

    [els.search, els.seen, els.sort, els.source].forEach(el => el.addEventListener("input", applyFilters));
    [els.yearChecks, els.paperChecks].forEach(el => el.addEventListener("change", applyFilters));
    els.reset.addEventListener("click", resetFilters);
    els.copyVisible.addEventListener("click", copyVisible);

    function handleOptionClick(btn) {{
      const article = btn.closest("article.mcq");
      const correct = article.dataset.correct || null;
      const source = article.dataset.source || null;
      const chosen = btn.dataset.letter;
      const resultEl = article.querySelector(".quiz-result");
      const resetBtn = article.querySelector(".reset-btn");
      const allBtns = article.querySelectorAll(".option-btn");

      allBtns.forEach(b => b.disabled = true);
      
      const sourceLabel = source === "llm" ? " (LLM)" : "";

      if (!correct) {{
        btn.style.background = "#e0e7ff";
        btn.style.borderColor = "#818cf8";
        resultEl.textContent = "Answer not in memo";
        resultEl.className = "quiz-result unknown";
      }} else if (chosen === correct) {{
        btn.classList.add("correct");
        resultEl.textContent = "Correct!" + sourceLabel;
        resultEl.className = "quiz-result correct";
      }} else {{
        btn.classList.add("incorrect");
        allBtns.forEach(b => {{ if (b.dataset.letter === correct) b.classList.add("correct"); }});
        resultEl.textContent = `Incorrect — answer is ${{correct}}${{sourceLabel}}`;
        resultEl.className = "quiz-result incorrect";
      }}

      resetBtn.style.display = "inline-block";
    }}

    function handleResetClick(resetBtn) {{
      const article = resetBtn.closest("article.mcq");
      const allBtns = article.querySelectorAll(".option-btn");
      const resultEl = article.querySelector(".quiz-result");

      allBtns.forEach(b => {{
        b.disabled = false;
        b.classList.remove("correct", "incorrect");
        b.style.background = "";
        b.style.borderColor = "";
      }});
      resultEl.textContent = "";
      resultEl.className = "quiz-result";
      resetBtn.style.display = "none";
    }}

    els.results.addEventListener("click", e => {{
      const btn = e.target.closest(".option-btn");
      if (btn && !btn.disabled) {{ handleOptionClick(btn); return; }}
      const reset = e.target.closest(".reset-btn");
      if (reset) {{ handleResetClick(reset); }}
    }});

    applyFilters();
  </script>
</body>
</html>
"""


def main():
    rows, source_counts = make_rows()
    OUTPUT.write_text(build_html(rows, source_counts), encoding="utf-8")
    print(f"Wrote {len(rows)} MCQs to {OUTPUT}")


if __name__ == "__main__":
    main()
