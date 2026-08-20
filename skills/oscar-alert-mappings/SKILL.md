---
name: oscar-alert-mappings
description: Use when creating, reviewing, migrating, or debugging OSCAR alert mappings, enrichment lookups, label normalization, keep/remove behavior, receiver mapping pipelines, or mapping test cases.
---

# OSCAR Alert Mappings

Turn intent into a deterministic mapping draft only after the ingress pipeline and label contract are known. “Repository-ready” means no invented lookup data, routing destination, namespace, or approved-label list.

## Workflow

1. Establish receiver/ingress, selected mapping name and namespace, representative sanitized input, required output, approved-label allowlist, authoritative lookup data/source, missing-lookup behavior, and target OSCAR release.
2. Retrieve current mapping documentation, then inspect the actual receiver pipeline and mapper implementation for operator order and command semantics. If documentation and code conflict, report the conflict and target the selected release's executable behavior.
3. Write a before/after label table. Account for mapper ordering, overwrites, temporary labels, lookup misses, regex anchoring, type conversion, and whether failures continue with partially transformed input.
4. Produce artifacts only with confirmed values. If required inputs are missing, provide a clearly marked parameterized draft and an input checklist; do not insert illustrative production values.
5. Validate syntax, schema, regexes, filename/discovery conventions, and mapper-specific behavior using OSCAR's tests or validator. Include positive, negative, lookup-miss, malformed-input, and unapproved-label cases.
6. Before upload/update, inspect for existing mappings and create-only behavior. Show merge or update strategy rather than assuming upload overwrites.
7. Provide deployment preview, live read-back, one controlled end-to-end input, expected persisted labels, notifier/audit verification, and rollback.

## Safety

- Never test with unsanitized customer payloads or commit secrets/identifiers unnecessarily.
- Do not call invented lookup rows or provisional allowlists repository-ready.
- Mapping success is not proof of persistence, routing, notification, or audit success.
- Require explicit confirmation before upload, update, reload, replay, or deletion.
- If a mapping stage can fail open, make survival of raw/unapproved labels an explicit production test.
