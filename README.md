# AI Pedigree

AI Pedigree is an Obsidian knowledge base mapping the people, institutions,
companies, ideas, and evidence behind modern AI. It also includes an automated
research watcher that monitors ArXiv and Hugging Face sources, saves relevant
items as Markdown notes, and emails a daily digest.

## Daily research digest

The workflow in `.github/workflows/daily-research-digest.yml` runs every day at
08:00 Asia/Shanghai (00:00 UTC) and can also be started manually from the
repository's **Actions** tab.

Monitored sources:

- ArXiv: `cs.AI`, `cs.LG`, `cs.CL`, and `cs.NE`
- Hugging Face Daily Papers community feed
- Hugging Face Blog

Relevant items are archived under `Previews/Research Digest/`. Deduplication is
tracked in `Scripts/.watcher_state.json`.

## GitHub Actions secrets

Configure these repository secrets under **Settings → Secrets and variables →
Actions**:

| Secret | Example |
| --- | --- |
| `SMTP_HOST` | `smtp.gmail.com` |
| `SMTP_PORT` | `587` |
| `SMTP_USER` | Gmail sender address |
| `SMTP_PASS` | 16-character Google app password |
| `RECIPIENTS` | Comma-separated recipient addresses |

Never commit SMTP credentials. See `Scripts/SMTP_SETUP.md` for local setup.

## Run locally

Python 3.9 or newer is sufficient; the watcher uses only the standard library.

```bash
export SMTP_HOST="smtp.gmail.com"
export SMTP_PORT="587"
export SMTP_USER="you@example.com"
export SMTP_PASS="your-app-password"
export RECIPIENTS="recipient@example.com"
python Scripts/ai_research_watcher.py
```

Without SMTP credentials, the watcher still fetches sources and writes notes,
but skips email delivery.
