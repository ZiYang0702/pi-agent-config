# Third-party notices

Upstream licenses retrieved using GitHub's public API (`gh api`); original copyright and permission text is preserved in adjacent files. Scope mapping is in [SKILLS.md](../SKILLS.md).

| Source | License file | API evidence (Git blob SHA) |
| --- | --- | --- |
| https://github.com/mattpocock/skills | mattpocock-skills-LICENSE (MIT) | `repos/mattpocock/skills/license`: `f1dd2c09108dde1a5f56097cee8461b3ea834499` |
| https://github.com/vercel-labs/skills | vercel-labs-skills-LICENSE (MIT) | `repos/vercel-labs/skills/license`: `eabe3008f6c0275929faa8b07d406e82717648cc` |
| https://github.com/cursor/plugins/tree/d1453c11d1dde9714d4c313c97d3a68432265c7f/pstack | cursor-pstack-LICENSE (MIT) | `repos/cursor/plugins/contents/pstack/LICENSE?ref=d1453c11d1dde9714d4c313c97d3a68432265c7f`: `6b5400237fdf6545be0b8fae370d6f2fcff8fb25` |
| https://github.com/humanlayer/skills | humanlayer-skills-LICENSE (MIT) | `repos/humanlayer/skills/license`: `f7ad6f4a1d5ed9bbf0589c172c6360587d1530e3` |

The HumanLayer notice supplements the retained `skills/pr/CREDITS.md` attribution for its copied visual-summary guidance. The five pstack-derived skills retain their `UPSTREAM.md` files and in-directory MIT notices (including notices added during export to create-verification-skill and maintain-verification-skill).

`skills/skill-creator/LICENSE.txt` is the complete Apache License 2.0 supplied alongside the synced skill. That skill's text and scripts are unchanged; only its directory location differs. It was selected from the preferred sync bucket; account-specific bucket identifiers and sync metadata are not distributed. No separate NOTICE file was present in that skill directory.

The local subagent extension derives from Pi's subagent example. `pi-LICENSE` retains Pi's MIT notice (https://github.com/earendil-works/pi; GitHub license blob `b0a8e9b81083294360c69b4ec45d3d39a2b28197`). Local adaptations include dispatch model/thinking inheritance and runtime entry resolution. Pi itself and the npm plugins are installed separately, not vendored.

No repository-wide license overrides these upstream terms. Locally maintained material without upstream license evidence is distinguished in SKILLS.md rather than silently assigned one of these licenses.
