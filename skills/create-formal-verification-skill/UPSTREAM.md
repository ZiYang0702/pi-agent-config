# Upstream provenance

- Source: https://github.com/cursor/plugins/tree/eb4db2b55b2b7dec3d9282754cddf0a56bf4ff10/pstack/skills/create-formal-verification-skill
- Repository revision: `eb4db2b55b2b7dec3d9282754cddf0a56bf4ff10`.
- Original SKILL.md Git blob (verified before adaptation): `b97609fd2649e95ea2960e720b3b581a6c2cb75a`.
- Complete upstream skill directory contains one file, SKILL.md. The pstack MIT LICENSE is included unchanged.
- Installation: user-level `~/.agents/skills/create-formal-verification-skill/`.

## Local adaptations

Pi `/skill:<name>` invocation; generated project skills go in the selected application's `.agents/skills/`. Added explicit target/version selection, quiet-test and durable redacted evidence, isolated scratch mutations, authorization boundaries, and honest fallback/blocked reporting. Preserved manual invocation, original verification procedure, mutation checks, and scope limitations.

## Updating and validation

Fetch the complete directory at a fixed upstream revision, verify its source hashes, and compare before reapplying these adaptations. Do not blindly overwrite local changes.

Installation validation covers Pi discovery, frontmatter, source completeness and preserved upstream instructions. It does not run a verifier, prove application properties, or install TLA+/SMT/proof tools.
