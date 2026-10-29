import type { ExtensionAPI, ExtensionContext } from "@earendil-works/pi-coding-agent";

const STATE = "local-fast-mode";

export default function (pi: ExtensionAPI) {
	let enabled = false;
	const supported = (ctx: ExtensionContext) =>
		ctx.model?.provider === "openai-codex" &&
		ctx.model?.api === "openai-codex-responses";
	const show = (ctx: ExtensionContext) => {
		ctx.ui.setStatus("fast-mode", supported(ctx) ? `Fast: ${enabled ? "on (requested)" : "off"}` : undefined);
	};
	const restore = (_event: unknown, ctx: ExtensionContext) => {
		enabled = false;
		for (const entry of ctx.sessionManager.getBranch()) {
			if (entry.type === "custom" && entry.customType === STATE) {
				const data = entry.data as { enabled?: boolean } | undefined;
				if (typeof data?.enabled === "boolean") enabled = data.enabled;
			}
		}
		show(ctx);
	};
	pi.on("session_start", restore);
	pi.on("session_switch", restore);
	pi.on("session_tree", restore);
	pi.on("session_fork", restore);
	pi.on("model_select", (_event, ctx) => show(ctx));

	pi.registerCommand("fast", {
		description: "ChatGPT Fast mode: /fast [on|off|status]. Separate from thinking level.",
		handler: async (args, ctx) => {
			const action = args.trim().toLowerCase();
			if (!["", "on", "off", "status"].includes(action)) {
				ctx.ui.notify("Usage: /fast [on|off|status]", "warning");
				return;
			}
			if (!supported(ctx)) {
				ctx.ui.notify("Fast mode requires an openai-codex model.", "warning");
				return;
			}
			if (action !== "status") {
				enabled = action === "" ? !enabled : action === "on";
				pi.appendEntry(STATE, { enabled });
			}
			show(ctx);
			ctx.ui.notify(enabled
				? "Fast on: requests priority service; actual availability and usage depend on your plan. Thinking level unchanged."
				: "Fast off. Thinking level unchanged.", "info");
		},
	});
	pi.on("before_provider_request", (event, ctx) => {
		if (!enabled || !supported(ctx) || !event.payload || typeof event.payload !== "object") return;
		return { ...event.payload, service_tier: "priority" };
	});
}
