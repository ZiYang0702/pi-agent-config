# Upstream provenance

- Source: https://github.com/cursor/plugins/tree/eb4db2b55b2b7dec3d9282754cddf0a56bf4ff10/pstack/skills/maintain-formal-verification-skill
- Repository revision: `eb4db2b55b2b7dec3d9282754cddf0a56bf4ff10`.
- Original SKILL.md Git blob (verified before adaptation): `5d2f7f2228a3b771ca5b03124fc265ddfc53c5fc`.
- Complete upstream skill directory contains one file, SKILL.md. The pstack MIT LICENSE is included unchanged.
- Installation: user-level `~/.agents/skills/maintain-formal-verification-skill/`.

## Local adaptations

Pi `/skill:<name>` invocation and project discovery under `.agents/skills/`. Added explicit application/version selection, quiet-test and durable redacted evidence, isolated scratch mutations, authorization boundaries, and honest fallback/blocked reporting. Preserved manual invocation, all six upkeep steps, sync-commit rules, and the distinction between verification drift and product bugs.

## Updating and validation

Fetch the complete directory at a fixed upstream revision, verify its source hashes, and compare before reapplying these adaptations. Do not blindly overwrite local changes.

Installation validation covers Pi discovery, frontmatter, source completeness and preserved upstream instructions. It does not run a verifier, prove application properties, or install TLA+/SMT/proof tools.
