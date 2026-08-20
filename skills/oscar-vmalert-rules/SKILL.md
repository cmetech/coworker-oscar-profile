---
name: oscar-vmalert-rules
description: Use when creating, reviewing, validating, deploying, or debugging OSCAR Prometheus, PromQL, VictoriaMetrics, VMAlert, recording, or self-monitoring alert rules.
---

# OSCAR VMAlert Rules

An alert rule is production-ready only when its metric contract, labels, project conventions, evaluation behavior, deployment path, and ownership are verified for the target release/environment.

## Workflow

1. Establish target symptom/SLO, OSCAR release, environment, existing related rules, metric names/types, observed labels and cardinality, evaluation interval, desired `for`, severity, ownership, runbook/dashboard links, and notification policy.
2. Inspect current OSCAR rule files, scrape/exporter configuration, self-monitoring catalog, and live series when available. Treat existing labels/annotations as project conventions unless a schema or policy makes them mandatory.
3. Check whether modifying an existing rule is safer than adding an overlapping alert. Explain duplicate-page and transition implications.
4. Draft PromQL defensively: handle absent series, zero denominators, resets, label joins, aggregation identity, cardinality, and insufficient sample volume. Mark every threshold/window as source-backed, operator-supplied, or proposed tuning.
5. Produce the full group/rule artifact with verified group metadata, stable alert identity, actionable summary/description, and only known labels/annotations. Do not invent runbook URLs, teams, dashboards, or environment labels.
6. Validate YAML plus the exact project-supported `promtool` or `vmalert -dryRun` path using the deployed/release-matched version. Add expression tests or controlled fixtures for fire, no-fire, absent, reset, and boundary cases.
7. Preview file replacement/addition and reload behavior. After explicit confirmation, deploy, verify the rule through the rules API, observe evaluation state, and test downstream delivery separately. Roll back the exact prior artifact.

## Safety

- Never use an unpinned `latest` validator image as sole evidence of compatibility.
- A successful dry run does not prove metrics or labels exist in production.
- Require explicit confirmation before replacing files, restart/reload, test-series injection, or rollback.
- Preserve the previous rule artifact and record whether a correlation rule depends on the alert name/labels.
- Do not call proposed tuning production-ready without operator approval or workload/SLO evidence.
