---
name: oscar-admin-qa
description: Use when answering how OSCAR works, locating OSCAR administration guidance, comparing conflicting OSCAR sources, or explaining whether a capability exists, is enabled, or is running.
---

# OSCAR Administration Q&A

Answer OSCAR questions from evidence, not product intuition. A concise answer with visible uncertainty is better than a complete-looking answer built from assumptions.

## Workflow

1. Classify the request: documented procedure, implementation behavior, configured intent, observed runtime, or design guidance.
2. Search Glean when available using the OSCAR component, command, error, and requested operation. Retrieve the exact Confluence page when wording, revision, or comments matter.
3. Corroborate operational claims against canonical OSCAR documentation. For implementation claims, inspect the relevant schema, script, compose file, API route, or test.
4. If sources conflict, identify each source and prefer current executable code for present implementation behavior. Do not silently rewrite documented support policy from code inference.
5. Label conclusions as **documented**, **code-verified**, **runtime-verified**, **inferred**, or **unknown**.
6. Separate **code-present**, **operator-enabled**, and **service-running** evidence.
7. Answer with: conclusion, evidence/citations, procedure or example, verification, assumptions, and unresolved questions.

Useful retrieval terms include the exact OSCAR command, service directory, API path, alert field, configuration key, and headings such as Administration, Configuration, Deployment, Security, Observability, Alert Mappings, Alert Rules, Correlation, Backup and Restore, Upgrades, and Troubleshooting.

## Safety

- Treat a source file, compose service, feature flag, and healthy container as four different kinds of evidence.
- Never invent commands, configuration fields, defaults, ports, supported platforms, credentials, or current runtime state.
- Redact secrets and customer data from searches and answers.
- For a state-changing answer, provide a read-only preflight and rollback first; obtain explicit confirmation before execution.
- If current evidence is unavailable, say what an administrator must inspect rather than claiming the state.
