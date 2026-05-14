# Agent System Launch Checklist

> Don't ship an agent system without checking these. Like a pilot's preflight — but for AI.

---

## ✈️ Pre-Launch

### Architecture
- [ ] Each agent has a single, clear responsibility
- [ ] Agent boundaries are defined (what each agent can and cannot do)
- [ ] Orchestration logic is explicit (not implicit in prompts)
- [ ] Failure modes are documented for each agent
- [ ] Escalation paths exist (agent → human) for every critical flow

### Prompts & Instructions
- [ ] System prompts are versioned and stored in code (not hardcoded in app)
- [ ] Output formats are specified (not "do your best")
- [ ] Each prompt has been tested with adversarial inputs
- [ ] Token limits are accounted for in long conversations

### Tools & Connections
- [ ] All tool connections are authenticated and scoped (least privilege)
- [ ] Tool failures are handled gracefully (retry → fallback → escalate)
- [ ] Rate limits are respected and monitored
- [ ] Sensitive data is never logged or exposed in agent outputs

### Guardrails
- [ ] Input validation exists (reject malformed/malicious inputs)
- [ ] Output validation exists (check before delivering to user)
- [ ] PII detection is in place
- [ ] Cost limits are set (max tokens per request, per session, per day)
- [ ] Human-in-the-loop triggers are defined for high-stakes actions

---

## 🚀 Launch Day

### Observability
- [ ] All agent calls are logged (input, output, latency, cost)
- [ ] Error rates are monitored with alerts
- [ ] Token usage is tracked per agent and per user
- [ ] Session traces are available for debugging

### Testing
- [ ] Happy path tested end-to-end
- [ ] Edge cases tested (empty input, very long input, conflicting instructions)
- [ ] Multi-agent handoff tested (context preserved across agents)
- [ ] Failure recovery tested (what happens when an agent fails mid-task)

### Documentation
- [ ] Architecture diagram exists and is current
- [ ] ADRs written for key design decisions
- [ ] Runbook exists for common failures
- [ ] On-call knows how to restart/debug agent pipelines

---

## 📈 Post-Launch (Week 1)

- [ ] Review error logs — any unexpected failures?
- [ ] Check cost — is token usage within budget?
- [ ] Gather user feedback — are outputs meeting expectations?
- [ ] Identify top 3 failure patterns → fix or add guardrails
- [ ] Update prompts based on real-world edge cases

---

## Quick Reference

| Phase | Key Question |
|-------|-------------|
| Architecture | "If this agent fails, what happens?" |
| Prompts | "Would a new team member understand this instruction?" |
| Tools | "What's the blast radius if this tool call goes wrong?" |
| Guardrails | "What's the worst output this could produce?" |
| Observability | "If something breaks at 3am, can we diagnose it?" |

---

*Use this checklist for every agent system you ship. Copy it into your project repo.*
