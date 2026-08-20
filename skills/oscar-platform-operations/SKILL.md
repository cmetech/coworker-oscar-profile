---
name: oscar-platform-operations
description: Use when checking OSCAR health, starting or stopping services, reviewing feature status, backing up or restoring state, inspecting logs, or planning routine platform operations.
---

# OSCAR Platform Operations

Operate OSCAR through dependency-aware, observable changes. A container listed as running is only one part of platform health.

## Workflow

1. Identify the environment, OSCAR release, topology, maintenance window, requested outcome, and available access.
2. Capture a before-state: operator-enabled features, service/container status and health, migrations, dependencies, capacity, active alerts, and relevant logs.
3. Use the release's OSCAR CLI and documented API/status surfaces. Confirm exact command syntax with `--help` or source before presenting it.
4. Build a dependency-aware operation plan: preconditions, commands, expected observations, timeout/stop condition, verification, and rollback.
5. For backups, identify configuration, secrets, certificates, databases, object/metric data, retention, encryption, and restore-test evidence separately. Do not call a copy a backup until its restore path is defined.
6. After a change, verify operator intent, process/container health, dependency readiness, and a meaningful end-to-end transaction.
7. Report the before/after delta and any remaining degraded or unknown state.

Use Glean or Confluence for current runbooks and ownership, then corroborate command behavior with canonical documentation and the selected release. For live incidents, runtime output outranks assumptions but does not rewrite documented support policy.

## Safety

- Require explicit confirmation immediately before start, stop, restart, reload, migration, restore, cleanup, or deletion.
- Display the target environment and affected services in that confirmation.
- Never use broad Docker prune/cleanup commands on a shared host without an approved resource inventory and blast-radius review.
- Do not expose secrets from environment files, generated secret files, logs, or command output.
- Stop when observed state differs from the stated precondition; do not continue a memorized runbook blindly.
