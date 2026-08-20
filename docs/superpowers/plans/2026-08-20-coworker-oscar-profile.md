# Coworker OSCAR Profile Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Publish a remotely installable OSCAR administrator profile and reusable OSCAR skill tap at `cmetech/coworker-oscar-profile`.

**Architecture:** A repository-root Hermes profile distribution owns a focused `SOUL.md`, minimal configuration, and eight progressive-disclosure skills. Structural tests and a guarded PowerShell smoke test prove packaging and Windows install/info/delete behavior without contacting an OSCAR environment.

**Tech Stack:** Hermes profile distributions, Agent Skills (`SKILL.md`), YAML, Python `unittest`, PowerShell, GitHub Actions.

**Spec:** `docs/superpowers/specs/2026-08-20-coworker-oscar-profile-design.md`

## Global Constraints

- Repository name: `coworker-oscar-profile`; installed profile name: `oscar`.
- Initial version: `0.1.0`.
- Repository visibility is private.
- No secrets, runtime data, post-install hooks, cron activation, or automatic MCP/plugin enablement.
- Glean and Confluence remain optional host capabilities.
- Administrative mutations are drafted and validated by default; live application requires target identification and explicit confirmation.
- Windows removal testing uses only `oscar-install-smoke`.

---

### Task 1: Define scaffold behavior contracts

**Files:**
- Create: `tests/test_scaffold.py`
- Create: `requirements-dev.txt`

**Interfaces:**
- Consumes: the design contract.
- Produces: `python -m unittest discover -s tests -v`, which validates the completed repository without an OSCAR runtime.

- [x] Write structural tests for the manifest, profile assets, skill frontmatter, safety text, forbidden files, README commands, and PowerShell smoke-test guard.
- [x] Run `python -m unittest discover -s tests -v` and confirm it fails because distribution assets do not exist.
- [x] Add only the test dependency declaration needed by local/CI validation.

### Task 2: Create the installable profile distribution

**Files:**
- Create: `distribution.yaml`
- Create: `SOUL.md`
- Create: `config.yaml`
- Create: `.gitignore`
- Create: `LICENSE`
- Create: `README.md`

**Interfaces:**
- Consumes: Hermes `profile install` repository-root manifest contract.
- Produces: an installable profile named `oscar` and human installation/removal documentation.

- [x] Add an explicit distribution-owned allowlist and optional `GLEAN_API_TOKEN` requirement.
- [x] Add the OSCAR evidence, state-distinction, and mutation-safety contract to `SOUL.md`.
- [x] Add minimal configuration that does not select credentials or enable external integrations.
- [x] Document macOS/Linux and Windows install, update, inspection, and removal commands.
- [x] Run the scaffold tests and confirm only missing-skill and smoke-script assertions remain.

### Task 3: Add the OSCAR knowledge and lifecycle skills

**Files:**
- Create: `skills/oscar-admin-qa/SKILL.md`
- Create: `skills/oscar-install-upgrade/SKILL.md`
- Create: `skills/oscar-platform-operations/SKILL.md`
- Create: `skills/oscar-troubleshooting/SKILL.md`

**Interfaces:**
- Consumes: the profile source hierarchy and canonical OSCAR documentation topics.
- Produces: evidence-grounded Q&A, install/upgrade guidance, operations guidance, and diagnostic workflows.

- [x] Use the baseline scenarios to encode missing evidence, state, validation, and safety guidance.
- [x] Give every skill discriminating `Use when...` frontmatter, a bounded workflow, and a safety section.
- [x] Run the skill validator and scaffold tests after each skill is added.

### Task 4: Add the OSCAR artifact-authoring skills

**Files:**
- Create: `skills/oscar-alert-mappings/SKILL.md`
- Create: `skills/oscar-alert-rules/SKILL.md`
- Create: `skills/oscar-correlation-rules/SKILL.md`
- Create: `skills/oscar-vmalert-rules/SKILL.md`

**Interfaces:**
- Consumes: OSCAR mapping, rule, correlation, and self-monitoring contracts.
- Produces: repository-ready drafts, cited assumptions, validation commands, deployment previews, and rollback instructions.

- [x] Use the baseline artifact scenarios to encode required output sections and uncertainty handling.
- [x] Give every skill discriminating frontmatter, an artifact contract, validation requirements, and a live-change safety boundary.
- [x] Run the skill validator and scaffold tests after each skill is added.

### Task 5: Add cross-platform validation and Windows smoke testing

**Files:**
- Create: `scripts/Test-ProfileInstall.ps1`
- Create: `.github/workflows/validate.yml`

**Interfaces:**
- Consumes: a local path or GitHub repository URL and the `hermes` CLI.
- Produces: a guarded disposable install/info/delete check and CI validation on Linux and Windows.

- [x] Add a PowerShell script hard-coded to the disposable `oscar-install-smoke` profile name.
- [x] Ensure cleanup runs in `finally` only when this invocation installed the disposable profile.
- [x] Add Linux and Windows CI jobs for structural tests; keep remote installation opt-in rather than running destructive profile deletion in CI.
- [x] Run the complete local validation suite.

### Task 6: Verify, version, and publish

**Files:**
- Modify: `docs/superpowers/plans/2026-08-20-coworker-oscar-profile.md`

**Interfaces:**
- Consumes: all repository assets and validation results.
- Produces: private GitHub repository `cmetech/coworker-oscar-profile` on `main`, tagged `v0.1.0`.

- [x] Run structural tests, all skill validators, secret scans, manifest parsing through Hermes, and a local temporary-home install/info/delete test.
- [x] Review `git diff --check`, repository status, and the complete tracked-file list.
- [x] Commit the scaffold, create the private GitHub repository, and push `main` plus tag `v0.1.0`.
- [x] Verify remote visibility, default branch, commit SHA, and tag through GitHub.
