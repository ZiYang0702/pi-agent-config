# Core export / installer interface

Target: Pi **1.4.0**. This is configuration and source, not a runtime or credential backup.

## Placement

| Export | Destination |
| --- | --- |
| `config/agent/` | `~/.pi/agent/` |
| `global/AGENTS.md` | `~/AGENTS.md` (explicit opt-in; preserve any existing file) |
| `docs/做票.md`, `docs/子Agent.md` | `~/.pi/docs/` |
| `bin/quiet-test` | `~/.local/bin/quiet-test`, executable, with `~/.local/bin` on PATH |
| `config/mcp.example.json` | Optional `~/.pi/agent/mcp.json`, after review |

No `__HOME__` substitution is needed in these core files. Pi 1.4.0's installed `docs/mcp.md` explicitly supports leading `~/` in stdio commands, arguments and cwd; browser profile/output arguments therefore use it. Workflow pointers use `~/.pi/docs`. The home-parent rules apply only beneath the home directory, whereas agent-directory rules apply across working directories. Preserve both layers; their inherited delegation/context-budget guidance is not reconciled by this export.

## Packages and extensions

Keep **both** local `extensions/subagent/{index.ts,agents.ts}` and `npm:@tintinweb/pi-subagents@0.22.0`; they are intentionally not deduplicated. Also retain `npm:pi-token-speed@0.12.0` and local `extensions/fast-mode.ts`. Install/reconcile the pinned npm declarations using Pi's package commands; the source tree alone does not install npm dependencies. Review third-party code before loading it. No runtime smoke test of both subagent implementations was performed by this export.

The local subagent sources import Pi-provided packages and `typebox`. The four roles are `scout`, `planner`, `reviewer`, `worker`; none pins its own model. The local implementation inherits the dispatching session's model/thinking settings. `long-task.toml` is omitted as inactive legacy: local role discovery accepts `.md` only. Subagent README and runtime artifacts are not needed for loading and are omitted.

`/fast` only requests priority service for `openai-codex` / `openai-codex-responses`; availability and billing depend on the account.

## Authentication and portable defaults

- No credentials are exported. `VOLCENGINE_PLAN_API_KEY` supplies the custom `volcengine-plan` subscription provider; its retained Ark endpoint is public. `DEEPSEEK_API_KEY` supplies DeepSeek. `models.json` uses Pi-supported `${NAME}` interpolation for API keys, not presumed interpolation of arbitrary fields.
- Original `openai-codex/gpt-6-astra` startup selection, model cycle, thinking levels, SSE transport and model metadata are preserved. They depend on catalog/account availability; they are not a universal working default. Authenticate using `/login`, then select an available model with `/model` and save it; adjust `/scoped-models` as needed. A new installation without matching credentials/models must make this choice before use. Do not silently substitute another provider or claim these IDs work for every account.
- Private `httpProxy` and the personal synchronized-skill exclusion are removed. Configure any needed local proxy separately. No skill directories are included in this core batch.

## Optional MCP

Both examples are disabled (`enabled: false`), preserving their exposure/tool-exposure settings for deliberate activation. Commands resolve through PATH:

- `peekaboo`: separately install a compatible Peekaboo CLI on macOS; grant required Screen Recording / Accessibility permissions. No executable or permissions are bundled.
- `npx`: Node/npm plus Google Chrome; downloads pinned `@playwright/mcp@0.0.83`. The dedicated `~/.pi/browser-profile` and `~/.pi/browser-output` directories hold local sign-ins/artifacts; do not publish them. Existing browser data is not copied.

Review prerequisites and consent before enabling either. Run `pi mcp list` only after opting in; it connects to enabled servers. No MCP connections were made during export.

## Logging and exclusions

`quiet-test` retains full logs under `${QUIET_TEST_LOG_DIR:-/tmp/quiet-test-logs}`, reports exit status/log path, and returns the wrapped command's status. On failure it also prints the last 18 log lines. Logs are local and may contain sensitive data.

No auth, model store, sessions, trust records, installation tree, backups or binaries are exported. The current source `做票.md` contains no organization/project IDs or private URLs; no fabricated IDs were inserted. Future ticket examples must use placeholders such as `<ORG_ID>` / `<PROJECT_ID>` instead of real identifiers. No git operations are part of this export.

Reference semantics were checked against the installed 1.4.0 documentation: `configuration.md`, `settings.md`, `models.md`, `models-configuration.md`, `providers.md`, `packages.md`, and `mcp.md`.
