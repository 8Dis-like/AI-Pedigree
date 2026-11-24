# AI Pedigree

AI Pedigree is an Obsidian knowledge base mapping the people, institutions,
companies, ideas, and evidence behind modern AI. It also includes an automated
research watcher that monitors ArXiv and Hugging Face sources, saves relevant
items as Markdown notes, and emails a daily digest.

## Repository map

| Path | Contents |
| --- | --- |
| `People/`, `Companies/`, `Institutions/`, `Labs/` | Linked entity notes |
| `Sources/` | Evidence notes and source references |
| `Data/` | Structured entities, relationships, coverage, and validation data |
| `*.canvas` | Obsidian lineage and organization maps |
| `Scripts/ai_research_watcher.py` | Feed fetcher, filter, note writer, and mailer |
| `Previews/Research Digest/` | Archived research highlights |
| `.github/workflows/` | Daily GitHub Actions automation |

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

The watcher uses only Python's standard library. It filters feed titles and
summaries against a curated set of architecture, capability, lab, researcher,
and safety terms. If email delivery fails, it exits with an error without
advancing the state file, allowing the next run to retry the same digest.

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

For Gmail, use an app password rather than the account password. Repository
secrets are exposed only to the workflow runtime and are not written to the
generated Markdown archive or logs committed by the workflow.

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
but exits before advancing state so the same items can be retried after SMTP is
configured.

## Operating the workflow

- Daily execution: 08:00 Asia/Shanghai / 00:00 UTC.
- Manual execution: **Actions → AI Research Daily Digest → Run workflow**.
- Successful runs commit new notes and the deduplication state to `main`.
- Runs with no new relevant items send no email and make no archive commit.
- SMTP failures fail the workflow and preserve the previous state for retry.

Review failed runs in the repository's **Actions** tab. GitHub automatically
redacts configured secret values from normal workflow logs.

## License and source material

The repository contains original knowledge-base notes and links to external
sources. Referenced source PDFs and local application artifacts are intentionally
excluded from version control; follow the linked publishers' terms when using
underlying material.
