# Upstream provenance

- Source: https://github.com/cursor/plugins/tree/d1453c11d1dde9714d4c313c97d3a68432265c7f/pstack/skills/create-verification-skill
- Repository revision: `d1453c11d1dde9714d4c313c97d3a68432265c7f`
- Original SKILL.md Git blob: `140d033a001e8d27acd14b06004506c43053b199`
- Installation: user-level `~/.agents/skills/create-verification-skill/`.

## Local adaptations

- Pi invocation syntax `/skill:<name>` and generated project directory `.agents/skills/verify-<app>/`.
- Added Pi integration guidance for repository scope, authorization, available tools, `quiet-test`, redacted durable evidence, and separate verification environments.
- Preserved manual invocation (`disable-model-invocation: true`) and all three upstream feature-map examples unchanged.

## Updating

Fetch the complete skill directory from a pinned upstream revision. Compare changes and reapply the documented local adaptations rather than overwriting this installation blindly. Keep the upstream proof requirement: a generated project skill must be exercised before it is reported as delivered.

Installation validation checks file completeness, source hashes, frontmatter, and local references. It does not execute the generator or verify an application.
