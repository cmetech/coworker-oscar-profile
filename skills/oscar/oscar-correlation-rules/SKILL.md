---
name: oscar-correlation-rules
description: Use when designing, validating, deploying, reviewing, or debugging OSCAR correlation patterns, grouping windows, synthetic alerts, thresholds, sequences, topology relationships, or correlation rule APIs.
---

# OSCAR Correlation Rules

Choose a correlation pattern from the event relationship the user can prove, not from the desired alert name. Tuning values require workload evidence or explicit operator decisions.

## Workflow

1. Capture source alert identity, relevant labels, desired relationship, grouping keys, window semantics, cardinality/sequence thresholds, late/duplicate behavior, emitted parent behavior, notifier effects, and target release.
2. Retrieve current correlation documentation and inspect the selected pattern's schema, runtime implementation, persistence/API route, reload behavior, and tests.
3. Explain why the chosen pattern fits and why adjacent patterns do not. Account for window boundaries, deduplication/fingerprints, missing labels, state retention, and synthetic-alert loops.
4. Mark every threshold, duration, priority, severity, emission cap, grouping label, and destination as **source-backed**, **operator-supplied**, or **proposed tuning**. Proposed tuning cannot be called production-ready.
5. Produce a schema-valid artifact and an input/output example set covering match, non-match, duplicate, boundary, missing-label, and rate-limit cases.
6. Use the non-persisting validation endpoint or local validator first. Then preview create/update/reload permissions and effects.
7. After confirmed deployment, read back by stable identity, inspect reload acceptance/rejection, inject a controlled source set when authorized, verify the synthetic parent and audit/notifier behavior, and retain the created rule ID for rollback.

## Safety

- Never invent production thresholds, ownership, notifier lists, or grouping labels.
- Validation success does not prove source labels exist or a parent reaches its destination.
- Do not blindly retry a timed-out create/update; read back first because persistence may have succeeded before reload failed.
- Require explicit confirmation before create, update, reload, test injection, or delete.
- Roll back the correlation rule before removing or renaming a source alert on which it depends.
