# Coworker OSCAR Profile

An installable OSCAR administration expert for LOOP24 Coworker. The repository is both a complete profile distribution and a GitHub skills tap.

Version `0.1.0` is an installation-test scaffold. It provides the profile behavior contract and focused administration skills; it does not connect to or modify an OSCAR environment by itself.

## What it provides

- Evidence-grounded OSCAR administration Q&A.
- Installation, upgrade, operations, and troubleshooting guidance.
- Drafting workflows for alert mappings, processing rules, correlation rules, and VMAlert rules.
- Optional use of host-provided Glean and Confluence capabilities.
- Explicit verification, rollback, and live-change confirmation boundaries.

## Requirements

- LOOP24 `0.12.0` or newer.
- Git, with network access to the public `cmetech/coworker-oscar-profile` repository.
- A configured model/provider in LOOP24 or during profile setup.
- Optional: the host's Glean MCP and Confluence capabilities.

No GitHub login is required because the repository is public. You can optionally verify access before installation:

```powershell
git ls-remote https://github.com/cmetech/coworker-oscar-profile.git HEAD
```

## Install the complete profile

PowerShell, Command Prompt, macOS, and Linux use the same LOOP24 command:

```text
loop24 profile install github.com/cmetech/coworker-oscar-profile --alias
loop24 profile info oscar
oscar setup
oscar chat
```

The installed profile name and optional command alias are `oscar`; the GitHub repository name remains `coworker-oscar-profile`. `oscar setup` configures this profile, while `oscar chat` starts a command-line chat with it. In the desktop app, select the OSCAR profile and chat normally instead.

LOOP24 creates its profile directories during installation. The default OSCAR profile location is:

- Windows: `%LOCALAPPDATA%\loop24\profiles\oscar` (normally `C:\Users\<user>\AppData\Local\loop24\profiles\oscar`).
- macOS/Linux: `~/.loop24/profiles/oscar`.

Windows uses `%LOCALAPPDATA%` because LOOP24 follows the operating system's standard per-user application-data convention; it does not store runtime application data directly under `%USERPROFILE%`.

## Update

```text
loop24 profile update oscar
loop24 profile info oscar
```

LOOP24 preserves user configuration on update unless the operator explicitly requests a configuration overwrite.

## Install one skill instead

The repository follows the GitHub tap layout:

```text
loop24 skills tap add cmetech/coworker-oscar-profile
loop24 skills inspect cmetech/coworker-oscar-profile/skills/oscar-vmalert-rules
loop24 skills install cmetech/coworker-oscar-profile/skills/oscar-vmalert-rules
```

## Removal warning

Profile deletion permanently removes that profile's configuration, credentials, memories, sessions, skills, and runtime data. Inspect the target name before continuing:

```text
loop24 profile info oscar
loop24 profile delete oscar
```

Do not use the real `oscar` profile for installation/removal testing. Use the guarded disposable smoke test instead.

## Windows Server smoke test

From PowerShell:

```powershell
Set-ExecutionPolicy -Scope Process Bypass
.\scripts\Test-ProfileInstall.ps1
```

The script installs the distribution as `oscar-install-smoke`, verifies it with `loop24 profile info`, and deletes only that disposable profile. If the disposable profile already exists, the script stops without deleting it.

To test a local clone before pushing:

```powershell
.\scripts\Test-ProfileInstall.ps1 -Source (Get-Location).Path
```

## OSCAR runtime on Windows Server

Installing this coworker on Windows does not mean OSCAR itself is supported as a native Windows workload. Current OSCAR installation and runtime procedures assume a supported Linux host. For a Windows Server evaluation host, use an approved Linux VM/topology and verify the applicable OSCAR release documentation before deployment.

## Development validation

```text
python -m unittest discover -s tests -v
```

The design and executable plan are under `docs/superpowers/`.
