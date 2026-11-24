#!/usr/bin/env python3
"""
AI Research Watcher for the AI Pedigree Vault
===============================================
Monitors HuggingFace Daily Papers and ArXiv RSS feeds for new AI/ML research
relevant to the genealogy tracked in the vault (deep learning, RL, LLMs, etc.).

For each run it:
  1. Fetches new papers/models from the configured sources.
  2. Filters them against a keyword list tuned to the vault's topics.
  3. Checks a state file to skip already-seen items.
  4. Writes new highlights as Obsidian notes under Previews/.
  5. Sends a digest email to the configured address.

Requires: Python 3.9+ (uses only stdlib + optional feedparser/requests).
"""

import json
import html
import os
import re
import smtplib
import ssl
import sys
import textwrap
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path

# ─── Configuration ────────────────────────────────────────────────────────────

VAULT_ROOT = Path(os.environ.get("VAULT_ROOT", Path(__file__).resolve().parents[1]))
PREVIEWS_DIR = VAULT_ROOT / "Previews" / "Research Digest"
STATE_FILE = VAULT_ROOT / "Scripts" / ".watcher_state.json"
LOG_FILE = VAULT_ROOT / "Scripts" / "watcher.log"

RECIPIENT_EMAILS = [
    address.strip()
    for address in os.environ.get(
        "RECIPIENTS",
        "ezugho@outlook.com,ezugho@gmail.com,hao.zhang@163.com",
    ).split(",")
    if address.strip()
]
# SMTP credentials — set via environment variables for security:
#   SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASS
# Example for Gmail: host=smtp.gmail.com, port=587, app-password in SMTP_PASS
# Example for Outlook: host=smtp-mail.outlook.com, port=587
SMTP_HOST = os.environ.get("SMTP_HOST", "smtp-mail.outlook.com")
SMTP_PORT = int(os.environ.get("SMTP_PORT", "587"))
SMTP_USER = os.environ.get("SMTP_USER", "")       # your sender address
# Strip spaces — Google displays app passwords as "xxxx xxxx xxxx xxxx" in the
# UI, but the actual credential must have no spaces when used for auth.
SMTP_PASS = os.environ.get("SMTP_PASS", "").replace(" ", "")

MAX_ITEMS_PER_SOURCE = 15  # limit items fetched per source per run
MAX_EMAIL_ITEMS = 20       # cap items included in the email digest

# ─── Sources ──────────────────────────────────────────────────────────────────

SOURCES = [
    {
        "id": "arxiv_cs_ai",
        "label": "ArXiv – cs.AI",
        "url": "https://rss.arxiv.org/rss/cs.AI",
        "type": "arxiv_rss",
    },
    {
        "id": "arxiv_cs_lg",
        "label": "ArXiv – cs.LG (Machine Learning)",
        "url": "https://rss.arxiv.org/rss/cs.LG",
        "type": "arxiv_rss",
    },
    {
        "id": "arxiv_cs_cl",
        "label": "ArXiv – cs.CL (Computation & Language / NLP)",
        "url": "https://rss.arxiv.org/rss/cs.CL",
        "type": "arxiv_rss",
    },
    {
        "id": "arxiv_cs_ne",
        "label": "ArXiv – cs.NE (Neural & Evolutionary Computing)",
        "url": "https://rss.arxiv.org/rss/cs.NE",
        "type": "arxiv_rss",
    },
    {
        "id": "huggingface_daily",
        "label": "HuggingFace – Daily Papers",
        # Official HF papers page has no native RSS; use community mirror
        # (GitHub Action scraper by huangboming, updates daily)
        "url": "https://raw.githubusercontent.com/huangboming/huggingface-daily-paper-feed/refs/heads/main/feed.xml",
        "type": "hf_rss",
    },
    {
        "id": "huggingface_blog",
        "label": "HuggingFace – Blog",
        "url": "https://huggingface.co/blog/feed.xml",
        "type": "hf_rss",
    },
]

# ─── Keyword Filter ───────────────────────────────────────────────────────────
# Topics relevant to the AI Pedigree Vault (deep learning genealogy,
# key researchers, landmark techniques).

KEYWORDS = [
    # Architecture families
    "transformer", "attention mechanism", "large language model", "LLM",
    "foundation model", "multimodal", "vision-language", "diffusion model",
    "generative model", "reinforcement learning", "deep reinforcement",
    "neural network", "convolutional", "recurrent", "LSTM", "GRU",
    "graph neural", "GNN",
    # Capability areas
    "reasoning", "chain-of-thought", "in-context learning", "few-shot",
    "zero-shot", "instruction tuning", "RLHF", "alignment", "AI safety",
    "interpretability", "mechanistic", "emergent", "scaling law",
    "knowledge distillation", "fine-tuning", "PEFT", "LoRA", "quantization",
    # Modalities & applications
    "protein structure", "AlphaFold", "code generation", "robotics",
    "autonomous agent", "tool use", "retrieval-augmented", "RAG",
    "speech recognition", "image generation", "video generation",
    # Key labs / lineage people (notable mentions)
    "DeepMind", "Google DeepMind", "OpenAI", "Anthropic", "Meta AI", "FAIR",
    "Hinton", "LeCun", "Bengio", "Sutton", "Hassabis", "Silver",
    "Sutskever", "Schmidhuber",
    # Recent breakthroughs worth tracking
    "AGI", "agentic", "long context", "mixture of experts", "MoE",
    "sparse model", "neural scaling", "world model",
]

KEYWORD_RE = re.compile(
    r"\b(" + "|".join(re.escape(k) for k in KEYWORDS) + r")\b",
    re.IGNORECASE,
)

# ─── Helpers ──────────────────────────────────────────────────────────────────

def log(msg: str) -> None:
    ts = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    line = f"[{ts}] {msg}"
    print(line, flush=True)
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(line + "\n")
    except Exception:
        pass


def load_state() -> dict:
    if STATE_FILE.exists():
        try:
            return json.loads(STATE_FILE.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"seen": {}}


def save_state(state: dict) -> None:
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")


def fetch_url(url: str, timeout: int = 20) -> bytes:
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "AI-Pedigree-Vault-Watcher/1.0 (research digest bot)"},
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def parse_rss(xml_bytes: bytes) -> list[dict]:
    """Parse RSS 2.0 / Atom feed, return list of {id, title, link, summary}."""
    items = []
    try:
        root = ET.fromstring(xml_bytes)
    except ET.ParseError:
        return items

    ns = {"atom": "http://www.w3.org/2005/Atom"}

    # RSS 2.0
    for item in root.iter("item"):
        title = (item.findtext("title") or "").strip()
        link = (item.findtext("link") or item.findtext("guid") or "").strip()
        summary = (item.findtext("description") or item.findtext("summary") or "").strip()
        # strip HTML tags from summary
        summary = re.sub(r"<[^>]+>", " ", summary)
        summary = re.sub(r"\s+", " ", summary).strip()
        item_id = link or title
        if item_id:
            items.append({"id": item_id, "title": title, "link": link, "summary": summary})

    # Atom
    for entry in root.findall("atom:entry", ns):
        title = (entry.findtext("atom:title", namespaces=ns) or "").strip()
        link_el = entry.find("atom:link[@rel='alternate']", ns) or entry.find("atom:link", ns)
        link = (link_el.get("href", "") if link_el is not None else "").strip()
        summary_el = entry.find("atom:summary", ns) or entry.find("atom:content", ns)
        summary = (summary_el.text or "" if summary_el is not None else "").strip()
        summary = re.sub(r"<[^>]+>", " ", summary)
        summary = re.sub(r"\s+", " ", summary).strip()
        item_id_el = entry.find("atom:id", ns)
        item_id = (item_id_el.text or link if item_id_el is not None else link).strip()
        if item_id or title:
            items.append({"id": item_id or title, "title": title, "link": link, "summary": summary})

    return items


def is_relevant(item: dict) -> bool:
    text = f"{item['title']} {item['summary']}"
    return bool(KEYWORD_RE.search(text))


def sanitize_filename(s: str) -> str:
    s = re.sub(r'[\\/:*?"<>|]', "-", s)
    return s[:80].strip()


def write_obsidian_note(item: dict, source_label: str, run_date: str) -> Path:
    PREVIEWS_DIR.mkdir(parents=True, exist_ok=True)
    fname = sanitize_filename(item["title"]) + ".md"
    note_path = PREVIEWS_DIR / fname
    if note_path.exists():
        return note_path
    tags = ["research-digest", "auto-import"]
    keywords_found = list({m.group(0).lower() for m in KEYWORD_RE.finditer(
        f"{item['title']} {item['summary']}")})
    content = textwrap.dedent(f"""\
        ---
        title: "{item['title'].replace('"', "'")}"
        source: "{source_label}"
        link: "{item['link']}"
        imported: "{run_date}"
        tags: {json.dumps(tags)}
        keywords: {json.dumps(keywords_found[:8])}
        status: unreviewed
        ---

        # {item['title']}

        **Source:** [{source_label}]({item['link']})
        **Imported:** {run_date}

        ## Abstract / Summary

        {item['summary'] or '_No summary available._'}

        ## Vault Connections

        > [!NOTE] Suggested next steps
        > - Check if any authors appear in [[02 Name Register]]
        > - If a new technique is applicable, consider adding a note to [[03 Evidence and Open Questions]]
        > - Add relationships to relevant people in [[People/]] if authors are tracked

        ## Relevance Notes

        _Keywords matched:_ {', '.join(f'`{k}`' for k in keywords_found[:8])}

        <!-- auto-generated by ai_research_watcher.py — edit freely -->
    """)
    note_path.write_text(content, encoding="utf-8")
    return note_path


# ─── Email ────────────────────────────────────────────────────────────────────

def build_email_html(new_items: list[dict], run_date: str) -> str:
    sections = []
    source_groups: dict[str, list] = {}
    for item in new_items[:MAX_EMAIL_ITEMS]:
        source_groups.setdefault(item["_source_label"], []).append(item)

    for src_label, items in source_groups.items():
        rows = ""
        for it in items:
            kw_badges = " ".join(
                f'<span style="background:#e8f4f8;border-radius:3px;padding:1px 5px;'
                f'font-size:11px;color:#1a6e9a;">{html.escape(k)}</span>'
                for k in it.get("_keywords", [])[:5]
            )
            link = html.escape(it["link"], quote=True)
            title = html.escape(it["title"])
            summary = html.escape((it.get("summary") or "")[:300])
            rows += f"""
            <tr>
              <td style="padding:10px 0;border-bottom:1px solid #eee;">
                <a href="{link}" style="color:#1a6e9a;font-weight:600;font-size:14px;">{title}</a>
                <br><div style="margin-top:4px;color:#555;font-size:12px;">{summary}{'…' if len(it.get('summary',''))>300 else ''}</div>
                <div style="margin-top:5px;">{kw_badges}</div>
              </td>
            </tr>"""
        sections.append(f"""
        <h3 style="color:#2c5f8a;border-bottom:2px solid #d0e8f7;padding-bottom:4px;">{html.escape(src_label)}</h3>
        <table width="100%" cellpadding="0" cellspacing="0">{rows}</table>""")

    body = "\n".join(sections)
    total = len(new_items)
    capped_note = f" (showing first {MAX_EMAIL_ITEMS})" if total > MAX_EMAIL_ITEMS else ""
    return f"""<!DOCTYPE html>
<html>
<head><meta charset="utf-8"></head>
<body style="font-family:Arial,sans-serif;max-width:720px;margin:auto;color:#333;">
  <div style="background:#1a6e9a;padding:20px 24px;border-radius:6px 6px 0 0;">
    <h1 style="margin:0;color:#fff;font-size:20px;">🧠 AI Pedigree Vault — Research Digest</h1>
    <p style="margin:4px 0 0;color:#cce8f7;font-size:13px;">{run_date} · {total} new item{"s" if total != 1 else ""}{capped_note}</p>
  </div>
  <div style="background:#f9f9f9;padding:4px 24px 2px;">
    <p style="font-size:13px;color:#666;">
      These papers and blog posts matched keywords from your AI genealogy vault.
      New notes have been added to <code>Previews/Research Digest/</code> in Obsidian.
    </p>
  </div>
  <div style="padding:12px 24px 24px;">
    {body}
  </div>
  <div style="background:#eee;padding:12px 24px;border-radius:0 0 6px 6px;font-size:11px;color:#999;">
    Sent automatically by AI Pedigree Vault Watcher · 
    Sources: ArXiv (cs.AI, cs.LG, cs.CL, cs.NE) + HuggingFace Daily Papers &amp; Blog
  </div>
</body>
</html>"""


def send_email(subject: str, html_body: str, plain_body: str) -> bool:
    if not SMTP_USER or not SMTP_PASS:
        log("⚠️  SMTP credentials not set — skipping email. Set SMTP_USER and SMTP_PASS env vars.")
        return False
    try:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = SMTP_USER
        msg["To"] = ", ".join(RECIPIENT_EMAILS)
        msg.attach(MIMEText(plain_body, "plain", "utf-8"))
        msg.attach(MIMEText(html_body, "html", "utf-8"))
        ctx = ssl.create_default_context()
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.ehlo()
            server.starttls(context=ctx)
            server.login(SMTP_USER, SMTP_PASS)
            server.sendmail(SMTP_USER, RECIPIENT_EMAILS, msg.as_string())
        log(f"✅ Email sent to {', '.join(RECIPIENT_EMAILS)}")
        return True
    except Exception as e:
        log(f"❌ Email failed: {e}")
        return False


# ─── Main ─────────────────────────────────────────────────────────────────────

def main() -> None:
    run_date = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    log(f"=== AI Research Watcher starting — {run_date} ===")

    state = load_state()
    seen: dict = state.setdefault("seen", {})

    all_new_items: list[dict] = []

    for source in SOURCES:
        log(f"Fetching {source['label']} …")
        try:
            xml_bytes = fetch_url(source["url"])
        except Exception as e:
            log(f"  ⚠️  Fetch error for {source['id']}: {e}")
            continue

        items = parse_rss(xml_bytes)
        log(f"  → {len(items)} items in feed")

        new_count = 0
        for item in items[:MAX_ITEMS_PER_SOURCE]:
            item_id = item["id"]
            if item_id in seen:
                continue
            seen[item_id] = run_date
            if not is_relevant(item):
                continue
            keywords_found = list({m.group(0).lower() for m in KEYWORD_RE.finditer(
                f"{item['title']} {item['summary']}")})
            item["_source_label"] = source["label"]
            item["_keywords"] = keywords_found
            # Write Obsidian note
            try:
                note_path = write_obsidian_note(item, source["label"], run_date)
                item["_note_path"] = str(note_path)
            except Exception as e:
                log(f"  ⚠️  Note write error: {e}")
            all_new_items.append(item)
            new_count += 1

        log(f"  → {new_count} new relevant items from {source['label']}")

    save_state(state)
    log(f"State saved. Total new relevant items this run: {len(all_new_items)}")

    if not all_new_items:
        log("Nothing new — no email sent.")
        return

    # Build and send email
    subject = f"[AI Pedigree Vault] {len(all_new_items)} new research item{'s' if len(all_new_items)!=1 else ''} — {run_date[:10]}"
    html_body = build_email_html(all_new_items, run_date)
    plain_body = "\n\n".join(
        f"{it['title']}\n{it['link']}\n{(it['summary'] or '')[:200]}"
        for it in all_new_items[:MAX_EMAIL_ITEMS]
    )
    send_email(subject, html_body, plain_body)

    log("=== Run complete ===\n")


if __name__ == "__main__":
    main()
