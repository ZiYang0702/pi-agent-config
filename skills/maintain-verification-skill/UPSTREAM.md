# Upstream provenance

- Source: https://github.com/cursor/plugins/tree/d1453c11d1dde9714d4c313c97d3a68432265c7f/pstack/skills/maintain-verification-skill
- Repository revision: `d1453c11d1dde9714d4c313c97d3a68432265c7f`
- Original SKILL.md Git blob: `a2680b91fead45a0b4963d8c367a854956bea59d`
- Installation: user-level `~/.agents/skills/maintain-verification-skill/`.

## Local adaptations

- Pi invocation syntax `/skill:<name>` and primary discovery in `.agents/skills/verify-*/`; existing Cursor skills remain discoverable without automatic migration.
- Added host-aware read-only delegation, a disclosed sequential fallback, coordinator-only shared UI driving, and explicit opt-in for workflow tools.
- Added authorization and publication boundaries, `quiet-test`, redacted durable evidence, and separate verification environments.
- Preserved manual invocation (`disable-model-invocation: true`), upstream live verification requirements, and the restriction against editing product code during maintenance.

## Updating

Fetch the complete skill directory from a pinned upstream revision. Compare changes and reapply the documented local adaptations rather than overwriting this installation blindly.

Installation validation checks file completeness, source hashes, frontmatter, and local references. It does not execute maintenance or verify an application.
