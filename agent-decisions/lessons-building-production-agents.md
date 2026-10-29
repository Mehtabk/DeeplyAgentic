# Lessons from Building Production Agents

> Field notes from building the same agent end-to-end on two independent stacks
> (AWS Bedrock AgentCore and Azure AI Foundry, 2026). Recorded because every lesson
> held *identically* on both — which is what makes them architecture principles, not
> vendor trivia. See also ADR-005 (keyless deploy) and ADR-006 (grounding + gating).

---

## 1. Agents are built on interfaces, not implementations

The agent code should know only contracts — a `Model`, a `Credentials` source, a
`Tool` — never the concrete service behind them. When that holds, the *same code*
runs on your laptop and deploys unchanged to a hosted runtime; the only thing that
changes at deploy is where the credential comes from.

- Model choice is configuration, not code (a model ID in `.env`, swappable).
- The credential source swaps at the boundary (local login → execution role), the
  agent never sees it.
- This is the practical reason the model comparison below is a *snapshot*, not a
  dependency: a well-built agent treats the model as replaceable.

## 2. Tool engineering is metadata engineering

The model obeys a tool's `name`, `description`, `inputSchema`, and result shape —
sent with every call — and never sees your callback code. So the tool's *metadata*
is the control plane, not its implementation.

- Write the description as *when to use this*, not *what it does*. Two tools with
  opposing descriptions let the model disambiguate on its own.
- Keep the result shape compact: tool results stay in context on every subsequent
  turn, so every extra field costs tokens on all following steps.
- An empty-result path should return a *note* that suggests a next step ("try a
  shorter query"), not a dead end — a bare "nothing found" makes the model invent.

## 3. Grounding is a property of the tool set, not the model

Same model, same question, same connection: with only a weak tool bound, the agent
fabricated specifics from a bare numeric score. Bind the right data tool and the
fiction is replaced by real, verifiable facts. Grounding is decided when you choose
which tools the agent can call — not by the model's "quality".

> A corollary learned the hard way: a multi-source answer can be *partly* grounded —
> numeric fields faithfully grounded while free-text prose is embroidered. A fluent
> answer is not a grounded one. Verify field-by-field, not by overall fluency.

## 4. Safety is a removed or gated capability, not a prompt

A prompt instruction ("never write without approval") lives exactly where the model
reads — and a crafted input can argue against it. A human-in-the-loop *gate* in the
code path blocks the action even when the model is fully compromised.

- Proven deterministically: no gate → the injected prompt triggered a write;
  gate on → the same prompt was stopped before the tool call.
- The three edges that together make an agent dangerous: untrusted input, a secret
  in context, and an external action. Defenses *break an edge* (remove the tool,
  gate the action), they don't filter the input.
- Content leakage and write actions are separate risks — a model can read a secret
  out loud without ever calling a write tool. Guard both.

## 5. Keyless identity is a chain, not a key

The strongest deploy model carries no long-lived key: a login yields short-lived
scoped credentials, those sign every request, and a model/permission allowlist is
enforced server-side (not bypassable from the client). One login can serve both the
model path and the tool/data path. See ADR-005.

---

## The meta-lesson

None of these are about a particular model or cloud. They are about **where control
lives**: in the tool metadata, in the code-level gate, in the credential boundary.
Get those right and the model underneath becomes a swappable detail — which is
exactly what you want when three new frontier models can ship in a single week.

---

*Recorded: 2026-10-29*
