# SMTP Setup for AI Research Watcher

The watcher script sends a daily digest to **ezugho@outlook.com**.
To enable email delivery, you need to supply SMTP credentials via environment variables.

---

## Option A — Outlook / Hotmail (Recommended, since you use @outlook.com)

1. Go to [account.microsoft.com/security](https://account.microsoft.com/security).
2. Enable **two-step verification** if not already on.
3. Under **Advanced security options → App passwords**, generate a new app password (name it `AI Vault Watcher`).
4. Set the following environment variables in your shell profile (`~/.zshrc` or `~/.zprofile`):

```zsh
export SMTP_HOST="smtp-mail.outlook.com"
export SMTP_PORT="587"
export SMTP_USER="ezugho@outlook.com"
export SMTP_PASS="<your-app-password>"
```

5. Reload: `source ~/.zshrc`

---

## Option B — Gmail (alternative sender)

1. Enable 2FA on your Google account.
2. Go to [myaccount.google.com/apppasswords](https://myaccount.google.com/apppasswords) → generate app password.
3. Set:

```zsh
export SMTP_HOST="smtp.gmail.com"
export SMTP_PORT="587"
export SMTP_USER="ezugho@gmail.com"
export SMTP_PASS="<your-16-character-app-password>"
export RECIPIENTS="ezugho@outlook.com,ezugho@gmail.com,hao.zhang@163.com"
```

---

## Verifying It Works

After setting the env vars, open a new terminal and run:

```zsh
python3 Scripts/ai_research_watcher.py
```

Check the log at:

```
Scripts/watcher.log
```

---

## Security Note

App passwords are limited-scope credentials — they cannot access your account settings.
Never put the password directly in the script, documentation, commits, or workflow;
always use environment variables or GitHub Actions secrets.

For the scheduled automation (the daily sidecar), Antigravity passes environment variables
through from your login session when it starts. Make sure to set them in `~/.zprofile`
(not just `~/.zshrc`) so they are available at login time.
