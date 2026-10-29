# Skills inventory

48 skills: 47 local directories and one deduplicated synced skill. Source installations were not changed.

## Included

### mattpocock/skills (38)

`ask-matt`, `chief-of-staff`, `claude-handoff`, `code-review`, `codebase-design`, `diagnosing-bugs`, `domain-modeling`, `git-guardrails-claude-code`, `grill-me`, `grill-with-docs`, `grilling`, `handoff`, `implement`, `implement-spec`, `improve-codebase-architecture`, `loop-me`, `migrate-to-shoehorn`, `pr`, `prototype`, `research`, `retro`, `scaffold-exercises`, `setup-matt-pocock-skills`, `setup-pre-commit`, `setup-ts-deep-modules`, `tdd`, `teach`, `to-questionnaire`, `to-spec`, `to-tickets`, `triage`, `wait-what`, `wayfinder`, `wizard`, `writing-beats`, `writing-for-agents`, `writing-fragments`, `writing-shape`

### cursor/plugins (pstack) (5)

`create-formal-verification-skill`, `create-verification-skill`, `maintain-formal-verification-skill`, `maintain-verification-skill`, `poteto-help`

### Locally maintained; user-authorized export (3)

`figma-diagram`, `lark-cli`, `source-command-reflect`

### vercel-labs/skills (1)

`find-skills`

### Apache-2.0 synced copy (1)

`skill-creator`

## Omitted

- `deep-research`, `docs`, `google-workspace`, `import-memory`, `morning`, `setup-writing-style`: no license granting redistribution of the skill content was found in the synced directories. Font-only OFL notices in `morning` do not license its instructions. User authorization alone does not establish third-party redistribution rights.
- `weekly-usage-report`: omitted rather than publish a superficially sanitized tool. Its SSH/sudo deployment, scheduled-task prompt harvesting, workspace-name attribution, private filesystem layout, and historical personal usage require a configurable collector and synthetic-fixture tests. None of its files are included.
- Seven restricted synced skills are excluded entirely; see the repository README for their names.
- Duplicate sync buckets, manifests, sync markers, caches and bytecode are excluded by selection. No binaries are included.

## Export changes

- `figma-diagram/SKILL.md`: replaced the fixed team plan key with an instruction to select the current authorized Figma team, asking the user when unset.
- `source-command-reflect/SKILL.md`: replaced two personal absolute home paths in examples with `~`.
- Added upstream MIT notices to the two verification skills that did not contain them locally. Retained existing notices and upstream provenance files.
- Flattened the selected synced `skill-creator` into `skills/skill-creator`; retained its Apache-2.0 license unchanged. No source script needed a home-path substitution after the usage-report omission.

## Licensing and dependencies

See [third-party/NOTICES.md](third-party/NOTICES.md) for upstream sources and license evidence. These are preserved local copies, not a claim that every local adaptation matches today's upstream. Locally maintained instructions are exported with the user's authorization; no additional upstream license is inferred for them. In particular, the diagram guide identifies Figma documentation as an influence, and the reflection guide identifies a migrated command.

Skills are instructions, not bundled service integrations. Depending on the selected workflow they require Pi/Claude-compatible tools, git, GitHub `gh` or GitLab `glab`, a project-specific test runner, and optional subagent support. Verification skills refer to `quiet-test` and browser/application harnesses; formal verification requires independently installed verifier tools. `lark-cli` needs its CLI and authenticated account; `figma-diagram` needs the Figma MCP diagram tool and a user-selected team. The reflection guide expects the user's own `~/.Codex/memory` layout.

`skill-creator` scripts require Python 3; validation uses PyYAML and evaluation/description optimization use the Claude CLI. Its viewer loads Google Fonts and a public SheetJS CDN resource. The architecture report template loads Tailwind and Mermaid from public CDNs. No CDN payloads, credentials, or private account configuration are bundled. Node/npm and project tooling are needed by the TypeScript/setup workflows; shell templates use Bash.

Export validation checks text-only files, exclusions, known private identifiers, syntax, skill headers and copy integrity. It does not execute service integrations, remote collectors, model evaluations, generated workflows, or prove absence of every possible secret.
