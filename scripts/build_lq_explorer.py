import html
import json
import re
from dataclasses import dataclass, field
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "ExamAdmin" / "Long Questions Explorer.html"

SOURCES = [
    ("2022", "Exam", ROOT / "Past Papers" / "2022" / "Exam.md"),
    ("2022", "ST2",  ROOT / "Past Papers" / "2022" / "ST2.md"),
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

# Topic rules: ordered by specificity. First match wins.
TOPIC_RULES = [
    ("DNS", [
        "zone file", "fqdn", "name resolution", "dns server", "mx record", "ns record",
        "name server", "whois", "registrar", "resource record", "aaaa record",
        "icann", "zadna", "tld ", "gtld", "cctld", "bind", "nslookup", "ptr record",
        "co.za", "resolv", "authoritative",
    ]),
    ("Routing Algorithms", [
        "dijkstra", "bellman-ford", "bellman ford", "routing table", "ospf", "rip ",
        "bgp", "routing algorithm", "next hop", "interior gateway", "exterior gateway",
        "igp", "egp", "distance vector", "link state",
    ]),
    ("IP Addressing & Subnetting", [
        "subnet", "cidr", "netmask", "network address", "broadcast address",
        "supernet", "private address", "class e", "class b address", "class a address",
        "ipv4 address", "ip address", "link-local", "169.254",
    ]),
    ("Network Layer (IP/ICMP/ARP)", [
        "nat box", "nat ", "icmp", "arp ", "traceroute", "tracert", "ttl",
        "fragmentation", "ipv6 address", "routing prefix", "multicast",
        "anycast", "unicast", "tunnel",
    ]),
    ("Transport Layer (TCP/UDP/QUIC)", [
        "tcp ", "udp ", "quic", "segment", "window size", "window advertisement",
        "sequence number", "acknowledgement", "syn flag", "handshake", "retransmit",
        "transport layer", "tcp timer", "persistent timer", "time-wait", "keep-alive",
        "three-way", "flow control", "congestion",
    ]),
    ("Application Protocols", [
        "http", "ftp ", "smtp", "pop3", "imap", "cgi program", "web server",
        "telnet", "snmp", "dhcp", "ldap", "email", "socket", "server code",
    ]),
    ("Encoding & Presentation", [
        "utf-8", "unicode", "base64", "quoted-printable", "mime ", "asn.1",
        "ber ", "ascii", "character encoding", "byte sequence", "hexadecimal",
        "u+", "hamming", "parity",
    ]),
    ("Data Link Layer", [
        "hdlc", "data link", "token ring", "ethernet", "layer 2 frame",
        "bit stuffing", "byte stuffing", "crc", "llc", "mac address",
    ]),
]


def detect_topic(text: str) -> str:
    lower = text.lower()
    for topic, keywords in TOPIC_RULES:
        if any(kw in lower for kw in keywords):
            return topic
    return "General"


def clean_text(value: str) -> str:
    replacements = {
        "‘": "'", "’": "'", "“": '"', "”": '"',
        "–": "-", "—": "-", "\xa0": " ",
    }
    for old, new in replacements.items():
        value = value.replace(old, new)
    return value


@dataclass
class LongQuestion:
    year: str
    paper: str
    number: int
    marks: str
    text: str
    topic: str
    source_label: str
    is_current: bool


def _is_memo_line(line: str) -> bool:
    return bool(re.search(r"(memo|answers?\s*$)", line, re.I))


def parse_source(year: str, paper: str, path: Path) -> list[LongQuestion]:
    raw = clean_text(path.read_text(encoding="utf-8"))
    lines = raw.splitlines()
    questions: list[LongQuestion] = []

    current_num: int | None = None
    current_marks: str = ""
    current_lines: list[str] = []

    def flush() -> None:
        nonlocal current_num, current_marks, current_lines
        if current_num is not None and current_lines:
            body = "\n".join(current_lines).strip()
            if body:
                topic = detect_topic(body)
                source_label = f"{year} {paper} Q{current_num}"
                is_current = f"{year} {paper}" in CURRENT_TEST_SOURCES
                questions.append(LongQuestion(
                    year=year, paper=paper, number=current_num,
                    marks=current_marks, text=body, topic=topic,
                    source_label=source_label, is_current=is_current,
                ))
        current_num = None
        current_marks = ""
        current_lines = []

    in_short_answer_section = False

    for line in lines:
        stripped = line.strip()

        # 2022-style section header
        if re.match(r"^## Short Answer", stripped, re.I):
            in_short_answer_section = True
            flush()
            continue

        # Level-2 or level-3 "Question N" heading
        # Level 2: ## Question N   (used by 2023-2026)
        # Level 3: ### Question N  (used by 2022 inside Short Answer section)
        lvl2 = re.match(r"^## Question\s+(\d+)(.*)", stripped, re.I)
        lvl3 = re.match(r"^### Question\s+(\d+)(.*)", stripped, re.I)
        heading_match = lvl2 or (lvl3 if in_short_answer_section else None)

        if heading_match:
            num = int(heading_match.group(1))
            rest = heading_match.group(2).strip()

            # Stop at memo / answer sections
            if _is_memo_line(rest) or _is_memo_line(stripped):
                flush()
                break

            # Skip Q1 (MCQs)
            if num == 1:
                flush()
                continue

            flush()
            current_num = num
            # Extract marks from heading: [5] or [5 marks] or [10 marks]
            marks_match = re.search(r"\[(\d+)(?:\s*marks?)?\]", rest, re.I)
            current_marks = marks_match.group(1) if marks_match else ""
            current_lines = []
            continue

        # If we hit a level-2 heading that is NOT a question and we are in a
        # 2023 paper (which has answers after questions), stop.
        if re.match(r"^## ", stripped) and current_num is not None:
            if _is_memo_line(stripped):
                flush()
                break

        if current_num is not None:
            current_lines.append(line)

    flush()
    return questions


TOPIC_COLOURS = {
    "DNS": ("#0e7490", "#cffafe"),
    "Routing Algorithms": ("#1d4ed8", "#dbeafe"),
    "IP Addressing & Subnetting": ("#7c3aed", "#ede9fe"),
    "Network Layer (IP/ICMP/ARP)": ("#be185d", "#fce7f3"),
    "Transport Layer (TCP/UDP/QUIC)": ("#d97706", "#fef3c7"),
    "Application Protocols": ("#16a34a", "#dcfce7"),
    "Encoding & Presentation": ("#dc2626", "#fee2e2"),
    "Data Link Layer": ("#0f766e", "#ccfbf1"),
    "General": ("#374151", "#f3f4f6"),
}


def make_rows() -> tuple[list[dict], dict[str, int]]:
    all_questions: list[LongQuestion] = []
    source_counts: dict[str, int] = {}

    for year, paper, path in SOURCES:
        label = f"{year} {paper}"
        if not path.exists():
            source_counts[label] = 0
            continue
        lqs = parse_source(year, paper, path)
        source_counts[label] = len(lqs)
        all_questions.extend(lqs)

    rows = []
    for idx, lq in enumerate(all_questions, start=1):
        tc, tb = TOPIC_COLOURS.get(lq.topic, TOPIC_COLOURS["General"])
        rows.append({
            "id": idx,
            "year": lq.year,
            "paper": lq.paper,
            "number": lq.number,
            "marks": lq.marks,
            "text": lq.text,
            "topic": lq.topic,
            "topicColour": tc,
            "topicBg": tb,
            "sourceLabel": lq.source_label,
            "isCurrent": lq.is_current,
            "studyStatus": "Skip for exam review" if lq.is_current else "Study",
        })

    return rows, source_counts


def build_html(rows: list[dict], source_counts: dict[str, int]) -> str:
    years = sorted({row["year"] for row in rows})
    papers = ["ST1", "ST2", "Exam"]
    topics = sorted({row["topic"] for row in rows})
    sources = [s for s in source_counts if source_counts[s] > 0]
    total_current = sum(1 for r in rows if r["isCurrent"])

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
  <title>COS332 Long Questions Explorer</title>
  <style>
    :root {{
      --bg: #f6f7f9;
      --panel: #ffffff;
      --text: #17202a;
      --muted: #5d6978;
      --line: #d9dee7;
      --accent: #7c3aed;
      --accent-soft: #ede9fe;
      --warn: #b45309;
      --warn-soft: #fef3c7;
      --shadow: 0 10px 30px rgba(23,32,42,0.08);
    }}
    * {{ box-sizing: border-box; }}
    body {{
      margin: 0;
      font-family: Arial, Helvetica, sans-serif;
      background: var(--bg);
      color: var(--text);
    }}
    header {{
      background: #fff;
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
    h1 {{ margin: 0 0 6px; font-size: 28px; line-height: 1.15; }}
    .subtitle {{ margin: 0; color: var(--muted); font-size: 14px; line-height: 1.45; }}
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
    .stat b {{ display: block; font-size: 22px; line-height: 1.1; }}
    .stat span {{ display: block; margin-top: 3px; color: var(--muted); font-size: 12px; }}
    main {{ padding: 18px 0 32px; }}
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
      grid-template-columns: minmax(200px, 1.4fr) minmax(150px, 0.7fr) minmax(150px, 0.7fr) minmax(160px, 0.7fr) minmax(170px, 0.7fr);
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
    input[type="search"], select {{
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
    .check input {{ margin: 0; accent-color: var(--accent); }}
    .filter-row {{
      display: grid;
      grid-template-columns: minmax(200px, 1fr) minmax(200px, 1fr) minmax(150px, 0.5fr);
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
    .view {{ display: grid; gap: 10px; }}
    .lq {{
      background: var(--panel);
      border: 1px solid var(--line);
      border-radius: 8px;
      box-shadow: 0 4px 16px rgba(23,32,42,0.05);
      overflow: hidden;
    }}
    .lq-head {{
      display: grid;
      grid-template-columns: 54px minmax(0,1fr) auto;
      gap: 12px;
      align-items: start;
      padding: 14px;
      cursor: pointer;
      user-select: none;
    }}
    .lq-head:hover {{ background: #f8fafc; }}
    .lq-id {{
      width: 42px;
      height: 32px;
      display: grid;
      place-items: center;
      border-radius: 8px;
      background: #edf1f5;
      color: #344054;
      font-weight: 700;
      font-size: 13px;
      flex-shrink: 0;
    }}
    .lq-meta {{
      min-width: 0;
    }}
    .lq-source {{
      font-size: 13px;
      font-weight: 700;
      color: var(--muted);
      margin-bottom: 4px;
    }}
    .lq-preview {{
      margin: 0;
      font-size: 15px;
      line-height: 1.45;
      color: var(--text);
      /* clamp to 2 lines */
      display: -webkit-box;
      -webkit-line-clamp: 2;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }}
    .lq-head.open .lq-preview {{
      -webkit-line-clamp: unset;
    }}
    .badges {{
      display: flex;
      flex-wrap: wrap;
      gap: 6px;
      justify-content: flex-end;
      align-items: flex-start;
    }}
    .badge {{
      display: inline-flex;
      align-items: center;
      min-height: 24px;
      border-radius: 999px;
      padding: 4px 9px;
      font-size: 12px;
      font-weight: 700;
      white-space: nowrap;
    }}
    .badge.seen {{ background: var(--warn-soft); color: var(--warn); }}
    .badge.study {{ background: var(--accent-soft); color: var(--accent); }}
    .badge.marks {{ background: #f1f5f9; color: #475569; }}
    .badge.expand {{
      background: #f1f5f9;
      color: #475569;
      cursor: pointer;
      border: none;
      font-size: 12px;
      font-weight: 700;
    }}
    .lq-body {{
      border-top: 1px solid var(--line);
      padding: 18px 20px;
      display: none;
    }}
    .lq-body.open {{ display: block; }}
    /* Markdown rendering inside lq-body */
    .lq-body h3, .lq-body h4 {{
      margin: 16px 0 6px;
      font-size: 15px;
    }}
    .lq-body p {{ margin: 0 0 10px; line-height: 1.55; }}
    .lq-body pre {{
      background: #f1f5f9;
      border: 1px solid var(--line);
      border-radius: 6px;
      padding: 12px 14px;
      overflow-x: auto;
      font-size: 13px;
      line-height: 1.5;
      margin: 0 0 12px;
    }}
    .lq-body code {{
      background: #f1f5f9;
      border-radius: 4px;
      padding: 1px 4px;
      font-size: 13px;
    }}
    .lq-body pre code {{ background: none; padding: 0; }}
    .lq-body ul, .lq-body ol {{
      margin: 0 0 10px 20px;
      padding: 0;
      line-height: 1.55;
    }}
    .lq-body li {{ margin-bottom: 3px; }}
    .lq-body table {{
      border-collapse: collapse;
      margin: 0 0 12px;
      font-size: 13px;
      width: 100%;
    }}
    .lq-body th, .lq-body td {{
      border: 1px solid var(--line);
      padding: 6px 10px;
      text-align: left;
    }}
    .lq-body th {{ background: #f8fafc; font-weight: 700; }}
    .lq-body hr {{ border: none; border-top: 1px solid var(--line); margin: 12px 0; }}
    .lq-body blockquote {{
      border-left: 3px solid var(--line);
      margin: 0 0 10px;
      padding: 4px 12px;
      color: var(--muted);
    }}
    .empty {{
      background: var(--panel);
      border: 1px dashed var(--line);
      border-radius: 8px;
      padding: 30px;
      text-align: center;
      color: var(--muted);
    }}
    @media (max-width: 1100px) {{
      .filter-grid {{ grid-template-columns: 1fr 1fr 1fr; }}
    }}
    @media (max-width: 768px) {{
      .topbar {{ flex-direction: column; align-items: stretch; }}
      .stats {{ min-width: 0; grid-template-columns: 1fr 1fr 1fr; }}
      .filter-grid, .filter-row {{ grid-template-columns: 1fr; }}
      .actions {{ justify-content: flex-start; }}
      .lq-head {{ grid-template-columns: 42px minmax(0,1fr); }}
      .badges {{ grid-column: 1 / -1; justify-content: flex-start; }}
    }}
  </style>
</head>
<body>
  <header>
    <div class="wrap topbar">
      <div>
        <h1>COS332 Long Questions Explorer</h1>
        <p class="subtitle">All longer questions (Q2+) extracted from past papers. Filter by topic to see what types repeat. Questions from 2026 ST1/ST2 are flagged low-priority for the upcoming exam.</p>
      </div>
      <div class="stats">
        <div class="stat"><b id="stat-total">{len(rows)}</b><span>total questions</span></div>
        <div class="stat"><b id="stat-visible">{len(rows)}</b><span>visible now</span></div>
        <div class="stat"><b id="stat-current">{total_current}</b><span>in 2026 tests</span></div>
      </div>
    </div>
  </header>

  <main>
    <div class="wrap">
      <section class="filters" aria-label="Filters">
        <div class="filter-grid">
          <div>
            <label for="search">Search</label>
            <input id="search" type="search" placeholder="Search question text or source…">
          </div>
          <div>
            <label for="topicFilter">Topic</label>
            <select id="topicFilter">{topic_options}</select>
          </div>
          <div>
            <label for="seenFilter">2026 status</label>
            <select id="seenFilter">
              <option value="all">All questions</option>
              <option value="unseen">Only study (not in 2026 tests)</option>
              <option value="seen">Only seen in 2026 tests</option>
            </select>
          </div>
          <div>
            <label for="sourceFilter">Specific paper</label>
            <select id="sourceFilter">{source_options}</select>
          </div>
          <div>
            <label for="sortBy">Sort</label>
            <select id="sortBy">
              <option value="source">Source (year/paper)</option>
              <option value="topic">Topic</option>
              <option value="status">Study status first</option>
              <option value="id">Table order</option>
            </select>
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
            <button id="resetBtn" type="button">Reset</button>
            <button id="expandAllBtn" type="button">Expand all</button>
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

    const TOPIC_COLOURS = {json.dumps({t: list(c) for t, c in TOPIC_COLOURS.items()}, ensure_ascii=False)};

    const state = {{
      search: "",
      topic: "all",
      seen: "all",
      source: "all",
      sort: "source",
      years: new Set({json.dumps(years)}),
      papers: new Set({json.dumps(papers)}),
      expandedIds: new Set(),
      allExpanded: false,
    }};

    const els = {{
      search: document.getElementById("search"),
      topicFilter: document.getElementById("topicFilter"),
      seenFilter: document.getElementById("seenFilter"),
      sourceFilter: document.getElementById("sourceFilter"),
      sortBy: document.getElementById("sortBy"),
      yearChecks: document.getElementById("yearChecks"),
      paperChecks: document.getElementById("paperChecks"),
      results: document.getElementById("results"),
      resultText: document.getElementById("resultText"),
      sourceText: document.getElementById("sourceText"),
      statVisible: document.getElementById("stat-visible"),
      resetBtn: document.getElementById("resetBtn"),
      expandAllBtn: document.getElementById("expandAllBtn"),
    }};

    const paperRank = {{ ST1: 0, ST2: 1, Exam: 2 }};

    function selectedValues(container) {{
      return new Set([...container.querySelectorAll("input:checked")].map(i => i.value));
    }}

    function textOf(row) {{
      return [row.text, row.topic, row.sourceLabel, row.studyStatus].join(" ").toLowerCase();
    }}

    function sourceSort(a, b) {{
      const ya = Number(a.year), yb = Number(b.year);
      if (ya !== yb) return ya - yb;
      const pa = paperRank[a.paper] ?? 9, pb = paperRank[b.paper] ?? 9;
      if (pa !== pb) return pa - pb;
      return a.number - b.number;
    }}

    function applyFilters() {{
      state.search = els.search.value.trim().toLowerCase();
      state.topic = els.topicFilter.value;
      state.seen = els.seenFilter.value;
      state.source = els.sourceFilter.value;
      state.sort = els.sortBy.value;
      state.years = selectedValues(els.yearChecks);
      state.papers = selectedValues(els.paperChecks);

      let rows = DATA.filter(row => {{
        if (state.search && !textOf(row).includes(state.search)) return false;
        if (state.topic !== "all" && row.topic !== state.topic) return false;
        if (state.seen === "seen" && !row.isCurrent) return false;
        if (state.seen === "unseen" && row.isCurrent) return false;
        if (state.source !== "all" && row.sourceLabel.split(" Q")[0] !== state.source) return false;
        if (!state.years.has(row.year)) return false;
        if (!state.papers.has(row.paper)) return false;
        return true;
      }});

      rows.sort((a, b) => {{
        if (state.sort === "topic") return a.topic.localeCompare(b.topic) || sourceSort(a, b);
        if (state.sort === "status") return Number(a.isCurrent) - Number(b.isCurrent) || sourceSort(a, b);
        if (state.sort === "id") return a.id - b.id;
        return sourceSort(a, b);
      }});

      render(rows);
      return rows;
    }}

    function escHtml(s) {{
      return String(s)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;");
    }}

    // Minimal markdown-to-HTML renderer
    function mdToHtml(md) {{
      // Protect code blocks
      const blocks = [];
      md = md.replace(/```([\\s\\S]*?)```/g, (_, code) => {{
        const i = blocks.length;
        blocks.push(`<pre><code>${{escHtml(code.trim())}}</code></pre>`);
        return `\\x00BLOCK${{i}}\\x00`;
      }});

      const lines = md.split("\\n");
      const out = [];
      let inTable = false;
      let inList = false;
      let inOl = false;

      function closeList() {{
        if (inList) {{ out.push("</ul>"); inList = false; }}
        if (inOl) {{ out.push("</ol>"); inOl = false; }}
      }}
      function closeTable() {{
        if (inTable) {{ out.push("</tbody></table>"); inTable = false; }}
      }}

      for (let i = 0; i < lines.length; i++) {{
        let line = lines[i];

        // Restore code blocks
        if (line.includes("\\x00BLOCK")) {{
          closeList(); closeTable();
          out.push(line.replace(/\\x00BLOCK(\\d+)\\x00/g, (_, n) => blocks[Number(n)]));
          continue;
        }}

        // HR
        if (/^---+$/.test(line.trim())) {{
          closeList(); closeTable();
          out.push("<hr>");
          continue;
        }}

        // Headings
        const hm = line.match(/^(#{1,4})\\s+(.*)/);
        if (hm) {{
          closeList(); closeTable();
          const level = Math.min(hm[1].length + 2, 6); // shift h1→h3, h2→h4, etc.
          out.push(`<h${{level}}>${{inline(hm[2])}}</h${{level}}>`);
          continue;
        }}

        // Blockquote
        if (/^>/.test(line)) {{
          closeList(); closeTable();
          out.push(`<blockquote>${{inline(line.replace(/^>\\s*/, ""))}}</blockquote>`);
          continue;
        }}

        // Table rows
        if (/^\\|/.test(line.trim())) {{
          const cells = line.split("|").slice(1, -1).map(c => c.trim());
          if (!inTable) {{
            closeList();
            out.push('<table><thead><tr>' + cells.map(c => `<th>${{inline(c)}}</th>`).join("") + '</tr></thead><tbody>');
            inTable = true;
            // skip separator line
            if (i + 1 < lines.length && /^\\|[-:|\\s|]+\\|$/.test(lines[i+1].trim())) i++;
            continue;
          }}
          out.push('<tr>' + cells.map(c => `<td>${{inline(c)}}</td>`).join("") + '</tr>');
          continue;
        }} else if (inTable) {{
          closeTable();
        }}

        // Unordered list
        const ulm = line.match(/^(\\s*[-*]\\s+)(.*)/);
        if (ulm) {{
          if (inOl) {{ out.push("</ol>"); inOl = false; }}
          if (!inList) {{ out.push("<ul>"); inList = true; }}
          out.push(`<li>${{inline(ulm[2])}}</li>`);
          continue;
        }}

        // Ordered list
        const olm = line.match(/^\\s*(\\d+)[.)\\s]+(.+)/);
        if (olm) {{
          if (inList) {{ out.push("</ul>"); inList = false; }}
          if (!inOl) {{ out.push("<ol>"); inOl = true; }}
          out.push(`<li>${{inline(olm[2])}}</li>`);
          continue;
        }}

        closeList(); closeTable();

        // Blank line
        if (!line.trim()) {{
          out.push("");
          continue;
        }}

        out.push(`<p>${{inline(line)}}</p>`);
      }}

      closeList(); closeTable();
      return out.join("\\n");
    }}

    function inline(s) {{
      s = escHtml(s);
      // Bold
      s = s.replace(/\\*\\*([^*]+)\\*\\*/g, "<strong>$1</strong>");
      // Italic
      s = s.replace(/\\*([^*]+)\\*/g, "<em>$1</em>");
      // Inline code
      s = s.replace(/`([^`]+)`/g, "<code>$1</code>");
      return s;
    }}

    function render(rows) {{
      els.statVisible.textContent = rows.length;
      els.resultText.textContent = `${{rows.length}} visible, ${{rows.filter(r => r.isCurrent).length}} in 2026 tests`;
      els.sourceText.textContent = state.source === "all" ? "All sources" : state.source;

      if (!rows.length) {{
        els.results.innerHTML = '<div class="empty">No questions match the current filters.</div>';
        return;
      }}

      els.results.innerHTML = rows.map(row => {{
        const isOpen = state.allExpanded || state.expandedIds.has(row.id);
        const statusClass = row.isCurrent ? "seen" : "study";
        const statusText = row.isCurrent ? "Seen in 2026 tests" : "Study";
        const marksText = row.marks ? `${{row.marks}} marks` : "";
        const preview = row.text.replace(/[\\r\\n]+/g, " ").replace(/#+\\s/g, "").trim().slice(0, 220);
        const [tc, tb] = TOPIC_COLOURS[row.topic] || ["#374151", "#f3f4f6"];

        return `
<article class="lq" data-id="${{row.id}}">
  <div class="lq-head${{isOpen ? " open" : ""}}" onclick="toggleCard(${{row.id}}, this)">
    <div class="lq-id">#${{row.id}}</div>
    <div class="lq-meta">
      <div class="lq-source">${{escHtml(row.sourceLabel)}}</div>
      <p class="lq-preview">${{escHtml(preview)}}…</p>
    </div>
    <div class="badges">
      <span class="badge" style="color:${{tc}};background:${{tb}}">${{escHtml(row.topic)}}</span>
      <span class="badge ${{statusClass}}">${{escHtml(statusText)}}</span>
      ${{marksText ? `<span class="badge marks">${{escHtml(marksText)}}</span>` : ""}}
    </div>
  </div>
  <div class="lq-body${{isOpen ? " open" : ""}}">${{mdToHtml(row.text)}}</div>
</article>`;
      }}).join("");
    }}

    function toggleCard(id, headEl) {{
      const article = headEl.closest(".lq");
      const body = article.querySelector(".lq-body");
      const isOpen = body.classList.contains("open");
      if (isOpen) {{
        body.classList.remove("open");
        headEl.classList.remove("open");
        state.expandedIds.delete(id);
      }} else {{
        body.classList.add("open");
        headEl.classList.add("open");
        state.expandedIds.add(id);
      }}
    }}

    function resetFilters() {{
      els.search.value = "";
      els.topicFilter.value = "all";
      els.seenFilter.value = "all";
      els.sourceFilter.value = "all";
      els.sortBy.value = "source";
      [...document.querySelectorAll(".checks input")].forEach(i => i.checked = true);
      state.expandedIds.clear();
      state.allExpanded = false;
      els.expandAllBtn.textContent = "Expand all";
      applyFilters();
    }}

    function toggleExpandAll() {{
      state.allExpanded = !state.allExpanded;
      els.expandAllBtn.textContent = state.allExpanded ? "Collapse all" : "Expand all";
      // Re-render to apply expansion state
      applyFilters();
    }}

    [els.search, els.topicFilter, els.seenFilter, els.sourceFilter, els.sortBy]
      .forEach(el => el.addEventListener("input", applyFilters));
    [els.yearChecks, els.paperChecks].forEach(el => el.addEventListener("change", applyFilters));
    els.resetBtn.addEventListener("click", resetFilters);
    els.expandAllBtn.addEventListener("click", toggleExpandAll);

    applyFilters();
  </script>
</body>
</html>
"""


def main() -> None:
    rows, source_counts = make_rows()
    OUTPUT.write_text(build_html(rows, source_counts), encoding="utf-8")
    print(f"Wrote {len(rows)} long questions to {OUTPUT}")
    for source, count in source_counts.items():
        if count:
            current = " [2026 current]" if source in CURRENT_TEST_SOURCES else ""
            print(f"  {source}: {count}{current}")


if __name__ == "__main__":
    main()
