---
name: oscar-install-upgrade
description: Use when planning or performing an OSCAR installation, deployment, initialization, migration, upgrade, rollback, uninstall, air-gapped setup, or platform-readiness assessment.
---

# OSCAR Installation and Upgrade

Build procedures from the target OSCAR release, topology, and supported host contract. Installation success is not proof that the application is initialized, enabled, healthy, or externally reachable.

## Workflow

1. Establish release/version, environment class, connected versus air-gapped mode, host OS, topology, sizing, DNS/TLS, image source, and rollback objective.
2. Check the release's canonical deployment documentation and live installer scripts. Report contradictions instead of blending them.
3. Produce a preflight that verifies OS support, CPU/RAM/storage, UID/GID and permissions, Docker/Compose versions, time/DNS, ports, certificates, archives, images, and backups.
4. Give the exact initialization and dependency-aware startup/migration order supported by that release. Never transplant an order from another version without verification.
5. Verify three layers separately: files/configuration are present, features are operator-enabled, and services are running/healthy. Include a real API or UI transaction where documented.
6. For upgrades, record the current version/configuration, back up the documented state, identify schema compatibility, stage artifacts, define stop/start order, and provide rollback criteria before execution.
7. For removal, inventory retained data first and explain the scope of cleanup commands. Prefer disposable-host or VM removal when a cleanup command can affect shared container resources.

On a Windows Server host, distinguish installing this coworker from installing OSCAR. Current OSCAR procedures assume supported Linux hosts; recommend an approved Linux guest/topology unless the selected OSCAR release explicitly documents native Windows support. Do not infer Hyper-V, WSL2, Docker Desktop, or Windows-container certification.

## Safety

- Do not run initialization, migration, restart, cleanup, restore, or deletion without the target environment and explicit confirmation.
- Do not recommend force flags as routine removal.
- Never call a procedure supported when only implementation clues exist; cite the release support statement.
- Treat live snapshots as insufficient database backups unless OSCAR documentation explicitly guarantees consistency.
- End with verification, rollback trigger, rollback commands, and remaining uncertainty.
