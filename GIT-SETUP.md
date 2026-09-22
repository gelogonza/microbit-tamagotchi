# Git authentication — one-time setup

**Goal:** authenticate once, then `git push` works without prompting — including
when Codex runs it for you.

The credential is held by your operating system, not by the agent, not by this
repository, and not in any file. The agent runs `git push`; your OS supplies the
credential; the agent never sees it. That is the whole design.

Do this once per machine. It survives restarts.

---

## Option A — Git Credential Manager (recommended)

Works with IU single sign-on. HTTPS, browser login, credential stored in Windows
Credential Manager or the macOS Keychain.

**Windows:** already installed with Git for Windows. Confirm:

```
git config --global credential.helper manager
```

**macOS:** install via Homebrew, or use the built-in keychain helper:

```
git config --global credential.helper osxkeychain
```

Then clone or push once over HTTPS. A browser window opens, you sign in with IU
SSO and Duo, and that is the last time you do it.

```
git push
```

---

## Option B — SSH key

Good if you already use SSH, or if HTTPS is blocked.

```
ssh-keygen -t ed25519 -C "your-iu-email@iu.edu"
```

Accept the default path. **Set a passphrase.** Then add the public key
(`~/.ssh/id_ed25519.pub`) to your IU GitHub Enterprise account under
Settings → SSH and GPG keys, and authorize it for SSO if prompted.

Use the SSH remote URL rather than HTTPS when you clone.

---

## Option C — GitHub CLI

If `gh` is available and configured for IU's Enterprise host:

```
gh auth login --hostname [IU GHE hostname]
```

It writes a credential helper entry for you.

---

## Verify it worked

```
git config --get credential.helper     # should print a helper name
git push                               # should not prompt
```

If it prompts every time, no helper is configured — go back to Option A.

---

## What not to do

**Do not put a token in a file.** Not in `.env`, not in `AGENTS.md`, not in a
note "just for now." Tokens in files get committed. This is the most common way
credentials leak and it happens to careful people.

**Do not embed a token in the remote URL.** `https://TOKEN@host/...` writes the
token into `.git/config` in plaintext and into every log line that prints the
remote.

**Do not paste a token to Codex or any LLM.** Anything in the agent's context
goes to the vendor. Your IU token is tied to your IU identity — a leaked one is
an account problem, not a repository problem.

**Do not share a credential with a teammate.** Every student authenticates as
themselves. Shared credentials make the commit history meaningless, which
matters here because your commit history is part of what you submit.

---

## If a credential leaks

Assume it is compromised the moment it lands somewhere it should not — a
commit, a chat window, a screenshot, a shared file. Deleting the file is not
enough; git keeps history and the chat log still exists.

1. Revoke it immediately in IU GitHub Enterprise → Settings → Developer settings
   → Personal access tokens. Revocation is the fix. Nothing else is.
2. Generate a new one, or switch to Option A so there is no token to leak.
3. Tell the instructional team. This is not a disciplinary matter — an
   unrevoked token on an IU account is a security issue and they would rather
   know within the hour.

---

## IU-specific details

Hostname, SSO behavior, and whether `gh` is configured for IU's Enterprise
instance are in the *INFO-I 341 GitHub and Codex Setup Guide* in Canvas. If
something here conflicts with that guide, the guide wins — ask the instructional
team rather than guessing or working around it.
