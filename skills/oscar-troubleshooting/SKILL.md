---
name: oscar-troubleshooting
description: Use when OSCAR is degraded, an alert is not processed or delivered, a component is unhealthy, a command fails, or an administrator needs an evidence package for escalation.
---

# OSCAR Troubleshooting

Trace the failing path before changing it. Preserve evidence and test the smallest discriminating hypothesis first.

## Workflow

1. Define the symptom, first occurrence, last known good state, affected environment/tenants, recent changes, impact, and a reproducible example or correlation identifier.
2. Map the expected path through OSCAR components. Mark each boundary **verified**, **failed**, or **unknown** using timestamps, status, health, logs, metrics, queues, database/audit records, and API responses.
3. Separate code-present, operator-enabled, service-running, dependency-ready, and end-to-end functional evidence.
4. Form one hypothesis tied to the earliest failed boundary. Run the least invasive check that can falsify it.
5. If a reversible fix is requested, state target, blast radius, expected signal, stop condition, verification, and rollback. Get explicit confirmation before execution.
6. Re-run the original reproduction and check adjacent paths after a fix.
7. If escalation is needed, package: timeline, environment/release, impact, sanitized reproduction, topology, state snapshots, relevant logs/metrics, failed boundary, attempted checks, and unresolved hypotheses.

For common “received but not notified” cases, inspect ingress acceptance, mapping/enrichment, persistence, processing/ACL/suppression, routing, notifier selection, delivery, and audit as separate boundaries. Do not jump from receiver logs directly to a notifier restart.

## Safety

- Preserve logs and state before restart, reload, cleanup, replay, migration, or deletion.
- Do not retry a timed-out mutation until read-back proves whether it landed.
- Redact tokens, credentials, customer payloads, and personal data in evidence packages.
- Avoid changing multiple variables at once; that destroys diagnostic evidence.
- Never represent a hypothesis, a present directory, or an enabled flag as proof of runtime cause.
