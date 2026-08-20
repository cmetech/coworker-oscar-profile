# Coworker OSCAR Profile Design

## Purpose

`coworker-oscar-profile` is a product-scoped Hermes profile distribution for OSCAR administrators. It installs an isolated `oscar` coworker that answers evidence-grounded OSCAR questions and helps draft, validate, and explain administrative artifacts without silently changing a live platform.

The same repository is also a GitHub skills tap: every OSCAR skill lives under `skills/<name>/SKILL.md` and can be installed independently.

## Distribution contract

- `distribution.yaml` is at the repository root because the current Hermes profile installer requires it there.
- The distribution name is `oscar`, while the repository name is `coworker-oscar-profile`.
- Version `0.1.0` is an installation-test release.
- `distribution_owned` is explicit and limited to `SOUL.md`, `config.yaml`, `skills/`, and `README.md`.
- The repository contains no credentials, user data, runtime state, executable post-install hooks, cron schedules, or automatically enabled MCP connections.
- Glean and Confluence are optional host capabilities. The profile detects and uses them when configured but remains useful with local/canonical OSCAR sources.

## Profile behavior

The `SOUL.md` contract makes OSCAR an administration specialist and requires:

1. Evidence before operational claims.
2. A source hierarchy of Glean, exact Confluence content, canonical OSCAR documentation, and code/runtime evidence.
3. Explicit distinction between code-present, service-running, and operator-enabled states.
4. Draft-and-validate behavior by default for mutations.
5. Explicit target environment and confirmation before applying a live change.
6. Source citations and visible uncertainty.

## Skills

- `oscar-admin-qa`: routes administration and Q&A requests to authoritative evidence.
- `oscar-install-upgrade`: handles prerequisites, deployment, verification, upgrades, rollback, and removal.
- `oscar-platform-operations`: handles health, lifecycle, backup/restore, and operational diagnostics.
- `oscar-alert-mappings`: drafts and validates mappings and enrichment behavior.
- `oscar-alert-rules`: drafts and validates ACL, processing, routing, and suppression rules.
- `oscar-correlation-rules`: drafts and validates correlation patterns and grouping behavior.
- `oscar-vmalert-rules`: drafts and validates Prometheus/VictoriaMetrics alerting rules.
- `oscar-troubleshooting`: performs evidence-first triage and creates escalation packages.

Each skill is concise. It states when it applies, its workflow, evidence requirements, safety boundary, and where to retrieve detailed OSCAR sources. Large or frequently changing OSCAR manuals are not copied into this repository.

## Installation and removal test

The Windows smoke test installs into the disposable profile name `oscar-install-smoke`, verifies the installed manifest, and deletes only that disposable profile. It refuses to run against `default` or `oscar` to avoid removing user data.

The test flow is:

1. Confirm `git` and `hermes` are available.
2. Refuse if the disposable profile already exists unless the operator removes it deliberately.
3. Install from the GitHub URL with `--name oscar-install-smoke --yes`.
4. Run `hermes profile info oscar-install-smoke`.
5. Confirm the expected distribution name/version appear.
6. Delete `oscar-install-smoke --yes` in `finally` cleanup.
7. Verify the profile no longer exists.

## Validation

Repository tests enforce behavior contracts rather than prose snapshots:

- root manifest and explicit ownership;
- required profile assets and focused skill set;
- valid skill frontmatter and discoverable trigger descriptions;
- no unfinished scaffold markers or secret files;
- profile source hierarchy and live-change confirmation boundaries;
- safe Windows smoke-test target and cleanup behavior.

## Deferred work

This scaffold does not implement a Hermes marketplace catalog, install Glean/Confluence plugins, pin profile installs to immutable Git commits, or apply changes to a live OSCAR deployment. Those are separate increments after Windows installation/removal is proven.
