# Upstream provenance

- Source: https://github.com/cursor/plugins/tree/eb4db2b55b2b7dec3d9282754cddf0a56bf4ff10/pstack/skills/poteto-help
- Revision: `eb4db2b55b2b7dec3d9282754cddf0a56bf4ff10`.
- Complete skill directory downloaded and Git blob hashes verified:
  - `SKILL.md`: `bf430fcd520e94748f1e1dbf93f6799e803d747a`.
  - `references/prompting.md`: `6b72b2e6081fdb78a3261bd77cf7334596d1ee20`.
  - `references/recipes.md`: `048e0750451aa801a4cf7ed59fa9ed4624c0f1ec`.
- The two references and pstack MIT LICENSE are included unchanged.
- Installation: user-level `~/.agents/skills/poteto-help/`.

## Local adaptations

Added a Pi/partial-installation compatibility section, Pi invocation in the description, explicit source-link resolution, and availability checks before routing work. Cursor/Claude Code setup and mode sections are labeled as upstream reference. Preserved the full skill map, close-call distinctions, playbook/principle explanations, troubleshooting, personalization, and prompt references.

Only installed skills may be offered as ready-to-run Pi commands. Same-named skills from other authors must not be attributed to pstack. External sibling skills and guides are read on demand at the pinned revision, not installed automatically. Help requests do not launch engineering work or multi-agent workflows.

## Updating and validation

Compare the complete upstream directory at a fixed revision, then reapply the documented compatibility changes. Do not blindly overwrite the local adapter.

Installation validation checks Pi discovery, manual invocation, bundled reference integrity and upstream link targets. It is not an end-to-end run of every recommended skill, nor installation of the complete pstack plugin.
