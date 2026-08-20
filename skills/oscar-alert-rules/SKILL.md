---
name: oscar-alert-rules
description: Use when creating, reviewing, importing, testing, or debugging OSCAR ACL, processing, routing, suppression, label-action, or rule-expression behavior.
---

# OSCAR Alert Rules

Treat rule authoring as a policy change. Resolve the rule stage, namespace, evaluation semantics, and failure behavior before drafting syntax.

## Workflow

1. Establish rule kind/stage, namespace and order, representative sanitized input, required match/non-match behavior, actions, routing destinations, ownership, and target release.
2. Retrieve canonical rule documentation and inspect the current schemas, evaluator, route permissions, and call path. Document whether the relevant path fails open, fails closed, skips, or returns partial results.
3. Convert intent into a truth table covering positive, negative, missing-field, casing/type, and conflicting-rule cases.
4. Confirm destination names, label values, suppression behavior, and precedence from authoritative configuration. Missing production values remain required inputs, not examples embedded in a final artifact.
5. Draft the smallest rule that satisfies the truth table. Keep enrichment/ownership labels separate from notifier-routing controls unless the documented path couples them.
6. Run static YAML/schema/expression validation, then OSCAR's non-persisting evaluate/test surface when available. Verify both applied actions and absence of unintended actions.
7. Inspect current installed rules and determine create, merge, update, or versioned replacement behavior. Provide deployment/read-back, controlled end-to-end verification, audit evidence, and rollback.

Output sections: target and assumptions, artifact, truth table, validation commands with expected results, deployment preview, live verification, rollback, and unresolved inputs.

## Safety

- Do not invent namespaces, forwarder/notifier names, support teams, or approved labels.
- A rule that parses is not proven safe; validate non-match and failure paths.
- Treat broad suppression, deletion, exclusive routing, and ACL changes as high blast-radius.
- Require explicit confirmation before import, update, reload, evaluation against sensitive live payloads, or deletion.
- After a timed-out mutation, read back by stable identity before retrying.
