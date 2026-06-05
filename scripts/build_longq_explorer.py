import html
import json
import re
from dataclasses import dataclass
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "ExamAdmin" / "Long Questions Explorer.html"

CURRENT_TEST_SOURCES = {"2026 ST1", "2026 ST2"}

# (year, paper, path, heading_level)
# heading_level 2 = "## Question N", 3 = "### Question N"
LONG_SOURCES = [
    ("2022", "Exam", ROOT / "Past Papers" / "2022" / "Exam.md", 3),
    ("2022", "ST2",  ROOT / "Past Papers" / "2022" / "ST2.md", 3),
    ("2023", "ST1",  ROOT / "Past Papers" / "2023" / "SemTest1.md", 2),
    ("2023", "ST2",  ROOT / "Past Papers" / "2023" / "SemTest2.md", 2),
    ("2023", "Exam", ROOT / "Past Papers" / "2023" / "Exam.md", 2),
    ("2024", "ST1",  ROOT / "Past Papers" / "2024" / "COS332_ST1_2024_questions.md", 2),
    ("2024", "ST2",  ROOT / "Past Papers" / "2024" / "COS332_ST2_2024_questions.md", 2),
    ("2024", "Exam", ROOT / "Past Papers" / "2024" / "COS332_FinalExam_2024_questions.md", 2),
    ("2025", "ST1",  ROOT / "Past Papers" / "2025" / "COS332_ST1_2025_questions.md", 2),
    ("2025", "ST2",  ROOT / "Past Papers" / "2025" / "COS332_ST2_2025_questions.md", 2),
    ("2025", "Exam", ROOT / "Past Papers" / "2025" / "Exam_2025_Question_Paper_questions.md", 2),
    ("2026", "ST1",  ROOT / "Past Papers" / "2026" / "SemTest1.md", 2),
    ("2026", "ST2",  ROOT / "Past Papers" / "2026" / "SemTest2.md", 2),
]

# Ordered so the first matching topic wins — put specific before general
TOPIC_KEYWORDS: list[tuple[str, list[str]]] = [
    ("Hamming / Error Coding",  ["hamming", "parity bit", "error correction", "error detect"]),
    ("UTF-8 / Unicode",         ["utf-8", "unicode", "u+0", "u+1", "u+2", "u+3", "u+4", "u+5",
                                  "byte sequence", "utf8", "cyrillic", "emoji", "regional indicator",
                                  "self-synchronis"]),
    ("DNS",                     ["zone file", "nslookup", "fqdn", "root server", "name server",
                                  "registrar", "rir", "afrinic", "arin", "ripe", "apnic", "lacnic",
                                  "tld", "ccTLD", "gtld", "dig ", "whois", "delegation"]),
    ("Routing",                 ["routing table", "bellman-ford", "dijkstra", "ospf", "rip ",
                                  "bgp", "distance vector", "link state", "shortest path",
                                  "routing algorithm", "igp", "egp"]),
    ("TCP / Transport",         ["tcp", "window advertisement", "acknowledgement number",
                                  "sequence number", "syn ", "handshake", "retransmission timer",
                                  "persistent timer", "keepalive", "time-wait", "quic"]),
    ("IP / Subnetting",         ["subnet", "cidr", "netmask", "broadcast address", "network address",
                                  "supernet", "ipv4", "ipv6", "nat box", "prefix length",
                                  "class a", "class b", "class c"]),
    ("Application Layer",       ["smtp", "imap", "pop3", "ftp", "telnet", "http", "snmp",
                                  "mime", "content-transfer", "x11", "email", "mail"]),
    ("Data Link / Layer 2",     ["data link", "frame delineation", "hdlc", "sdlc", "ethernet",
                                  "mac address", "token ring", "aloha", "csma", "layer 2"]),
    ("ASN.1 / BER",             ["asn.1", "ber ", "der ", "ldap"]),
    ("Security",                ["encryption", "ssl", "tls", "x.509", "certificate", "rsa",
                                  "diffie-hellman", "public key"]),
]


def detect_topic(text: str) -> str:
    lower = text.lower()
    for topic, keywords in TOPIC_KEYWORDS:
        if any(kw in lower for kw in keywords):
            return topic
    return "General / Other"


def extract_marks(text: str) -> str:
    m = re.search(r"\[(\d+)\s*(?:marks?)?\]", text, re.I)
    return m.group(1) if m else ""


@dataclass
class LongQuestion:
    year: str
    paper: str
    num: str
    marks: str
    topic: str
    intro: str
    full_text: str
    source_label: str
    in_current: bool


def parse_long_questions(year: str, paper: str, path: Path, heading_level: int) -> list[LongQuestion]:
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError:
        return []

    lines = text.splitlines()
    hashes = "#" * heading_level
    q_pattern = re.compile(rf"^{re.escape(hashes)}\s+Question\s+(\d+)(.*)?$", re.I)
    # Only match question-specific memo/answer headings, not section names like "Short Answer Questions"
    memo_pattern = re.compile(r"^#{1,4}\s+Question\s+\d+\s*[-—]\s*(memo|answer)", re.I)
    memo_top = re.compile(r"^#{1,3}\s+MEMO\b", re.I)

    questions: list[LongQuestion] = []
    current_num: str | None = None
    current_marks_heading = ""
    current_lines: list[str] = []
    in_memo = False

    def flush() -> None:
        nonlocal current_num, current_lines, current_marks_heading
        if current_num is None:
            return
        body = "\n".join(current_lines).strip()
        if not body:
            current_num = None
            current_lines = []
            current_marks_heading = ""
            return

        marks = current_marks_heading or extract_marks(body)

        # Intro: first non-trivial line, stripped of markdown decorators
        intro = ""
        for ln in current_lines:
            stripped = ln.strip()
            if stripped and stripped not in ("---", "***") and not re.match(r"^\*\*\[\d+\]\*\*", stripped):
                intro = re.sub(r"[*_`#]", "", stripped)[:150].strip()
                if intro:
                    break

        topic = detect_topic(body)
        source_label = f"{year} {paper}"
        in_current = source_label in CURRENT_TEST_SOURCES

        questions.append(LongQuestion(
            year=year,
            paper=paper,
            num=current_num,
            marks=marks,
            topic=topic,
            intro=intro,
            full_text=body,
            source_label=f"{source_label} Q{current_num}",
            in_current=in_current,
        ))
        current_num = None
        current_lines = []
        current_marks_heading = ""

    for line in lines:
        if memo_top.match(line) or memo_pattern.match(line):
            flush()
            in_memo = True
            continue
        if in_memo:
            continue

        m = q_pattern.match(line)
        if m:
            qnum = int(m.group(1))
            flush()
            if qnum == 1:
                continue
            current_num = str(qnum)
            current_marks_heading = extract_marks(m.group(2) or "")
            current_lines = []
            continue

        if current_num is not None:
            current_lines.append(line)

    flush()
    return questions


def make_rows() -> tuple[list[dict], dict[str, int]]:
    all_questions: list[LongQuestion] = []
    source_counts: dict[str, int] = {}

    for year, paper, path, level in LONG_SOURCES:
        label = f"{year} {paper}"
        qs = parse_long_questions(year, paper, path, level)
        source_counts[label] = len(qs)
        all_questions.extend(qs)

    rows = []
    for idx, q in enumerate(all_questions, start=1):
        rows.append({
            "id": idx,
            "year": q.year,
            "paper": q.paper,
            "num": q.num,
            "marks": q.marks,
            "topic": q.topic,
            "intro": q.intro,
            "fullText": q.full_text,
            "sourceLabel": q.source_label,
            "inCurrent": q.in_current,
            "studyStatus": "Skip — asked in 2026 test" if q.in_current else "Study for exam",
        })

    return rows, source_counts


def build_html(rows: list[dict], source_counts: dict[str, int]) -> str:
    years = sorted({r["year"] for r in rows})
    papers = sorted({r["paper"] for r in rows}, key=lambda p: {"ST1": 0, "ST2": 1, "Exam": 2}.get(p, 9))
    topics = sorted({r["topic"] for r in rows})
    sources = [s for s in source_counts if source_counts[s] > 0]
    data_json = json.dumps(rows, ensure_ascii=False).replace("</", "<\\/")
    summary_json = json.dumps(source_counts, ensure_ascii=False).replace("</", "<\\/")

    year_checks = "".join(
        f'<label class="check"><input type="checkbox" value="{html.escape(y)}" checked> {html.escape(y)}</label>'
        for y in years
    )
    paper_checks = "".join(
        f'<label class="check"><input type="checkbox" value="{html.escape(p)}" checked> {html.escape(p)}</label>'
        for p in papers
    )
    topic_options = '<option value="all">All topics</option>' + "".join(
        f'<option value="{html.escape(t)}">{html.escape(t)}</option>' for t in topics
    )
    source_options = '<option value="all">All papers</option>' + "".join(
        f'<option value="{html.escape(s)}">{html.escape(s)} ({source_counts[s]})</option>'
        for s in sources
    )

    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>COS332 Long Question Explorer</title>
  <style>
    :root {{
      --bg: #f6f7f9; --panel: #ffffff; --text: #17202a; --muted: #5d6978;
      --line: #d9dee7; --accent: #0f766e; --accent-soft: #d7f3ef;
      --warn: #a16207; --warn-soft: #fff0c2; --shadow: 0 10px 30px rgba(23,32,42,.08);
    }}
    * {{ box-sizing: border-box; }}
    body {{ margin:0; font-family: Arial, Helvetica, sans-serif; background: var(--bg); color: var(--text); }}
    header {{ background:#fff; border-bottom:1px solid var(--line); }}
    .wrap {{ width: min(1440px, calc(100% - 32px)); margin: 0 auto; }}
    .topbar {{ display:flex; align-items:flex-end; justify-content:space-between; gap:24px; padding:24px 0 18px; }}
    h1 {{ margin:0 0 6px; font-size:28px; line-height:1.15; }}
    .subtitle {{ margin:0; color:var(--muted); font-size:14px; }}
    .stats {{ display:grid; grid-template-columns:repeat(3, minmax(110px,1fr)); gap:10px; min-width:380px; }}
    .stat {{ background:#f8fafc; border:1px solid var(--line); border-radius:8px; padding:10px 12px; }}
    .stat b {{ display:block; font-size:22px; line-height:1.1; }}
    .stat span {{ display:block; margin-top:3px; color:var(--muted); font-size:12px; }}
    main {{ padding:18px 0 32px; }}
    .filters {{ background:var(--panel); border:1px solid var(--line); border-radius:8px; box-shadow:var(--shadow); padding:14px; margin-bottom:16px; }}
    .filter-grid {{ display:grid; grid-template-columns:minmax(200px,1.4fr) minmax(160px,.7fr) minmax(160px,.7fr) minmax(180px,.8fr); gap:12px; align-items:end; }}
    label {{ display:block; color:var(--muted); font-size:12px; font-weight:700; margin-bottom:6px; text-transform:uppercase; }}
    input[type="search"], select {{ width:100%; height:40px; border:1px solid var(--line); border-radius:8px; background:#fff; color:var(--text); padding:0 10px; font-size:14px; }}
    .filter-row {{ display:grid; grid-template-columns:minmax(200px,1fr) minmax(200px,1fr) minmax(160px,.5fr); gap:12px; margin-top:12px; align-items:end; }}
    .checks {{ display:flex; flex-wrap:wrap; gap:8px; min-height:40px; align-items:center; }}
    .check {{ display:inline-flex; align-items:center; gap:6px; border:1px solid var(--line); border-radius:999px; padding:7px 10px; background:#fff; font-size:13px; white-space:nowrap; }}
    .check input {{ margin:0; accent-color:var(--accent); }}
    .actions {{ display:flex; gap:8px; align-items:center; justify-content:flex-end; }}
    button {{ height:40px; border:1px solid var(--line); border-radius:8px; background:#fff; color:var(--text); padding:0 12px; font-size:14px; cursor:pointer; }}
    button.primary {{ background:var(--accent); border-color:var(--accent); color:#fff; }}
    .result-meta {{ display:flex; justify-content:space-between; align-items:center; gap:12px; margin:10px 0 12px; color:var(--muted); font-size:13px; }}
    .view {{ display:grid; gap:10px; }}
    .lq {{ background:var(--panel); border:1px solid var(--line); border-radius:8px; box-shadow:0 4px 16px rgba(23,32,42,.05); overflow:hidden; }}
    .lq-head {{ display:grid; grid-template-columns:54px minmax(0,1fr) auto; gap:12px; align-items:start; padding:14px; border-bottom:1px solid var(--line); cursor:pointer; user-select:none; }}
    .lq-head:hover {{ background:#fafbfc; }}
    .lq-id {{ width:42px; height:32px; display:grid; place-items:center; border-radius:8px; background:#edf1f5; color:#344054; font-weight:700; font-size:13px; flex-shrink:0; }}
    .lq-intro {{ margin:0; font-size:15px; line-height:1.48; }}
    .lq-intro small {{ display:block; margin-top:4px; font-size:12px; color:var(--muted); }}
    .badges {{ display:flex; flex-wrap:wrap; gap:6px; justify-content:flex-end; }}
    .badge {{ display:inline-flex; align-items:center; min-height:24px; border-radius:999px; padding:4px 8px; background:#eef2f7; color:#344054; font-size:12px; font-weight:700; white-space:nowrap; }}
    .badge.skip {{ background:var(--warn-soft); color:var(--warn); }}
    .badge.study {{ background:var(--accent-soft); color:var(--accent); }}
    .badge.topic {{ background:#f0eeff; color:#5b21b6; }}
    .lq-body {{ display:none; padding:14px; border-top:1px solid var(--line); }}
    .lq-body.open {{ display:block; }}
    .lq-body pre {{ margin:0; white-space:pre-wrap; word-break:break-word; font-family:monospace; font-size:13px; line-height:1.6; background:#f8fafc; border:1px solid var(--line); border-radius:6px; padding:12px; overflow-x:auto; }}
    .lq-md {{ font-size:14px; line-height:1.7; color:var(--text); }}
    .lq-md p {{ margin:0 0 8px; }}
    .lq-md ul {{ margin:0 0 8px; padding-left:22px; }}
    .lq-md li {{ margin-bottom:5px; }}
    .lq-md li > ul {{ margin-top:4px; margin-bottom:0; }}
    .lq-md code {{ font-family:monospace; font-size:13px; background:#f0f3f7; border:1px solid var(--line); border-radius:4px; padding:1px 5px; }}
    .lq-md strong {{ font-weight:700; }}
    .lq-md em {{ font-style:italic; }}
    .empty {{ background:var(--panel); border:1px dashed var(--line); border-radius:8px; padding:30px; text-align:center; color:var(--muted); }}
    .chevron {{ font-size:10px; color:var(--muted); margin-left:4px; transition:transform .15s; }}
    .lq-head.expanded .chevron {{ transform:rotate(180deg); }}
    @media(max-width:960px) {{
      .topbar {{ flex-direction:column; align-items:stretch; }}
      .stats {{ min-width:0; }}
      .filter-grid, .filter-row {{ grid-template-columns:1fr; }}
      .actions {{ justify-content:flex-start; }}
    }}
  </style>
</head>
<body>
<header>
  <div class="wrap topbar">
    <div>
      <h1>COS332 Long Question Explorer</h1>
      <p class="subtitle">All structured questions from past papers — filter by topic, year, and paper type.</p>
    </div>
    <div class="stats">
      <div class="stat"><b id="stat-total">{len(rows)}</b><span>total questions</span></div>
      <div class="stat"><b id="stat-visible">{len(rows)}</b><span>visible now</span></div>
      <div class="stat"><b id="stat-skip">0</b><span>skip (asked 2026)</span></div>
    </div>
  </div>
</header>
<main>
  <div class="wrap">
    <section class="filters" aria-label="Filters">
      <div class="filter-grid">
        <div>
          <label for="search">Search</label>
          <input id="search" type="search" placeholder="Search question text, topic, or source">
        </div>
        <div>
          <label for="topic">Topic</label>
          <select id="topic">{topic_options}</select>
        </div>
        <div>
          <label for="status">Study status</label>
          <select id="status">
            <option value="all">All questions</option>
            <option value="study">Only study for exam</option>
            <option value="skip">Only asked in 2026 tests</option>
          </select>
        </div>
        <div>
          <label for="source">Specific paper</label>
          <select id="source">{source_options}</select>
        </div>
      </div>
      <div class="filter-row">
        <div>
          <label>Years</label>
          <div class="checks" id="yearChecks">{year_checks}</div>
        </div>
        <div>
          <label>Paper types</label>
          <div class="checks" id="paperChecks">{paper_checks}</div>
        </div>
        <div class="actions">
          <button id="reset" type="button">Reset</button>
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
    search: "", topic: "all", status: "all", source: "all",
    years: new Set({json.dumps(years)}),
    papers: new Set({json.dumps(papers)})
  }};

  const els = {{
    search: document.getElementById("search"),
    topic: document.getElementById("topic"),
    status: document.getElementById("status"),
    source: document.getElementById("source"),
    yearChecks: document.getElementById("yearChecks"),
    paperChecks: document.getElementById("paperChecks"),
    results: document.getElementById("results"),
    resultText: document.getElementById("resultText"),
    sourceText: document.getElementById("sourceText"),
    statVisible: document.getElementById("stat-visible"),
    statSkip: document.getElementById("stat-skip"),
    reset: document.getElementById("reset"),
  }};

  function selectedValues(container) {{
    return new Set([...container.querySelectorAll("input:checked")].map(i => i.value));
  }}

  function textOf(row) {{
    return [row.intro, row.fullText, row.sourceLabel, row.topic, row.studyStatus].join(" ").toLowerCase();
  }}

  function applyFilters() {{
    state.search = els.search.value.trim().toLowerCase();
    state.topic = els.topic.value;
    state.status = els.status.value;
    state.source = els.source.value;
    state.years = selectedValues(els.yearChecks);
    state.papers = selectedValues(els.paperChecks);

    let rows = DATA.filter(row => {{
      if (state.search && !textOf(row).includes(state.search)) return false;
      if (state.topic !== "all" && row.topic !== state.topic) return false;
      if (state.status === "study" && row.inCurrent) return false;
      if (state.status === "skip" && !row.inCurrent) return false;
      if (state.source !== "all" && row.sourceLabel !== state.source) return false;
      if (!state.years.has(row.year)) return false;
      if (!state.papers.has(row.paper)) return false;
      return true;
    }});

    render(rows);
    return rows;
  }}

  function esc(s) {{
    return String(s).replace(/&/g,"&amp;").replace(/</g,"&lt;").replace(/>/g,"&gt;").replace(/"/g,"&quot;");
  }}

  function inline(s) {{
    return esc(s)
      .replace(/\\*\\*(.+?)\\*\\*/g, "<strong>$1</strong>")
      .replace(/`([^`]+)`/g, "<code>$1</code>");
  }}

  function md(src) {{
    const lines = (src || "").split(/\\n/);
    const out = [];
    let inUl = false;
    for (let i = 0; i < lines.length; i++) {{
      const line = lines[i].trimEnd();
      const li = line.match(/^[\\*\\-]\\s+([\\s\\S]*)/);
      if (li) {{
        if (!inUl) {{ out.push("<ul>"); inUl = true; }}
        out.push(`<li>${{inline(li[1])}}</li>`);
      }} else {{
        if (inUl) {{ out.push("</ul>"); inUl = false; }}
        if (line.trim()) out.push(`<p>${{inline(line)}}</p>`);
      }}
    }}
    if (inUl) out.push("</ul>");
    return out.join("");
  }}

  function render(rows) {{
    const skipCount = rows.filter(r => r.inCurrent).length;
    els.statVisible.textContent = rows.length;
    els.statSkip.textContent = DATA.filter(r => r.inCurrent).length;
    els.resultText.textContent = `${{rows.length}} visible, ${{skipCount}} asked in 2026 tests`;
    els.sourceText.textContent = state.source === "all" ? "All sources" : state.source;

    if (!rows.length) {{
      els.results.innerHTML = '<div class="empty">No questions match the current filters.</div>';
      return;
    }}

    els.results.innerHTML = rows.map(row => {{
      const statusClass = row.inCurrent ? "skip" : "study";
      const statusText = row.inCurrent ? "Skip — asked 2026" : "Study for exam";
      const marksText = row.marks ? `${{row.marks}} marks` : "";
      return `
        <article class="lq">
          <div class="lq-head" onclick="toggleBody(this)" data-id="${{row.id}}">
            <div class="lq-id">${{esc(row.sourceLabel.replace(/ Q[0-9]+$/, ""))}}<br><small>Q${{esc(row.num)}}</small></div>
            <p class="lq-intro">
              ${{esc(row.intro || "(no intro)")}}
              <small>${{esc(row.sourceLabel)}}${{marksText ? " · " + esc(marksText) : ""}}</small>
            </p>
            <div class="badges">
              <span class="badge topic">${{esc(row.topic)}}</span>
              <span class="badge ${{statusClass}}">${{esc(statusText)}}</span>
              <span class="chevron">▼</span>
            </div>
          </div>
          <div class="lq-body" id="body-${{row.id}}">
            <div class="lq-md">${{md(row.fullText)}}</div>
          </div>
        </article>`;
    }}).join("");
  }}

  function toggleBody(head) {{
    const id = head.dataset.id;
    const body = document.getElementById("body-" + id);
    const open = body.classList.toggle("open");
    head.classList.toggle("expanded", open);
  }}

  function resetFilters() {{
    els.search.value = "";
    els.topic.value = "all";
    els.status.value = "all";
    els.source.value = "all";
    [...document.querySelectorAll(".checks input")].forEach(i => i.checked = true);
    applyFilters();
  }}

  [els.search, els.topic, els.status, els.source].forEach(el => el.addEventListener("input", applyFilters));
  [els.yearChecks, els.paperChecks].forEach(el => el.addEventListener("change", applyFilters));
  els.reset.addEventListener("click", resetFilters);

  applyFilters();
</script>
</body>
</html>
"""


def main() -> None:
    rows, source_counts = make_rows()
    OUTPUT.write_text(build_html(rows, source_counts), encoding="utf-8")
    skip = sum(1 for r in rows if r["inCurrent"])
    print(f"Wrote {len(rows)} long questions ({skip} from 2026 tests) to {OUTPUT}")
    print()
    print("By source:")
    for label, count in source_counts.items():
        if count:
            print(f"  {label}: {count}")


if __name__ == "__main__":
    main()
