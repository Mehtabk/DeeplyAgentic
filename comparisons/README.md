# Framework Comparisons

> The most comprehensive side-by-side comparison of AI agent frameworks. Updated May 2026.
>
> ⭐ Star this repo if you find it useful — it helps others discover it.

---

## Multi-Agent Orchestration Frameworks (May 2026)

| Feature | CrewAI | AutoGen | LangGraph | OpenAI Agents SDK | Mastra |
|---------|--------|---------|-----------|-------------------|--------|
| **Language** | Python | Python | Python | Python | TypeScript |
| **Stars** | 51K | 58K | 32K | 26K | 24K |
| **Approach** | Role-based crews | Conversations | State machines | Handoffs | Workflows |
| **Multi-agent** | ✅ Native | ✅ Native | ✅ Native | ✅ Native | ✅ Native |
| **MCP Support** | ✅ | ⚠️ Partial | ✅ | ✅ | ✅ |
| **Memory** | ✅ Built-in | ✅ Built-in | ✅ Checkpoints | ⚠️ Basic | ✅ Built-in |
| **Human-in-loop** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Streaming** | ✅ | ✅ | ✅ | ✅ | ✅ |
| **Structured output** | ✅ Pydantic | ✅ | ✅ | ✅ | ✅ Zod |
| **Observability** | ✅ Built-in | ⚠️ Basic | ✅ LangSmith | ⚠️ Basic | ✅ Built-in |
| **Learning curve** | Low | Medium | High | Low | Low |
| **Best for** | Quick prototypes | Research/complex | Production workflows | Simple pipelines | TS/Node teams |
| **Weakness** | Less control at scale | Verbose setup | Steep learning curve | Limited customization | Younger ecosystem |

---

## When to Use What

```
Need it running in 1 hour?           → OpenAI Agents SDK or CrewAI
Building for production scale?       → LangGraph
Research or complex reasoning?       → AutoGen
TypeScript / Node.js team?           → Mastra
Role-based agent teams?              → CrewAI
Need full control over state?        → LangGraph
Want the simplest possible API?      → OpenAI Agents SDK
Enterprise with existing LangChain?  → LangGraph
```

---

## Pricing & Cost

| Framework | License | Hosting | Hidden Costs |
|-----------|---------|---------|--------------|
| CrewAI OSS | MIT | Self-host | Free (AMP platform is paid) |
| AutoGen | MIT | Self-host | Free |
| LangGraph | MIT | Self-host or LangSmith Cloud | LangSmith paid for production tracing |
| OpenAI SDK | MIT | Self-host | Locked to OpenAI models (pay per token) |
| Mastra | MIT | Self-host or Vercel | Free |

**Key insight:** All frameworks are free to use. The real cost is the LLM tokens underneath. OpenAI SDK locks you to OpenAI models. The others let you swap providers.

---

## Architecture Fit (by DeeplyAgentic 4-Layer Stack)

| Layer | CrewAI | AutoGen | LangGraph | OpenAI SDK | Mastra |
|-------|--------|---------|-----------|------------|--------|
| 🎯 Orchestration | Crew manager | GroupChat | Graph router | Handoff logic | Workflow engine |
| 🧠 Agents | Role-based | Conversational | Node-based | Function agents | Step-based |
| 🔌 Tools (MCP) | Native MCP | Custom tools | Native MCP | Native tools | Native MCP |
| 🛡️ Guardrails | Task guardrails | Code execution sandbox | Conditional edges | Input/output guards | Middleware |

---

## Orchestration Patterns

| Pattern | Description | Best Framework | Example |
|---------|-------------|----------------|---------|
| Sequential | A → B → C | OpenAI Agents SDK | Research → Write → Review |
| Fan-out / Fan-in | Split → parallel → merge | LangGraph, AutoGen | Analyze 5 docs simultaneously |
| Hierarchical | Manager delegates to workers | CrewAI | PM assigns tasks to specialists |
| Conversation | Agents discuss until consensus | AutoGen | Debate → agree on answer |
| State machine | Explicit transitions | LangGraph | Draft → Review → Approve → Publish |
| Loop with exit | Retry until quality passes | LangGraph, CrewAI | Generate → Validate → (retry or done) |

---

## Model Support

| Framework | OpenAI | Anthropic | Local/Ollama | Google | AWS Bedrock | Azure |
|-----------|--------|-----------|--------------|--------|-------------|-------|
| CrewAI | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| AutoGen | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| LangGraph | ✅ | ✅ | ✅ | ✅ | ✅ | ✅ |
| OpenAI SDK | ✅ | ❌ | ❌ | ❌ | ❌ | ❌ |
| Mastra | ✅ | ✅ | ✅ | ✅ | ⚠️ | ✅ |

**Verdict:** If model flexibility matters (it should), avoid OpenAI SDK as your primary framework. Use it for prototyping, then migrate to CrewAI or LangGraph for production.

---

## Minimal Code Comparison

### CrewAI — 3 agents in 20 lines

```python
from crewai import Agent, Task, Crew

researcher = Agent(role="Researcher", goal="Find facts")
writer = Agent(role="Writer", goal="Write clearly")
reviewer = Agent(role="Reviewer", goal="Check quality")

task1 = Task(description="Research AI agents", agent=researcher)
task2 = Task(description="Write a summary", agent=writer)
task3 = Task(description="Review the summary", agent=reviewer)

crew = Crew(agents=[researcher, writer, reviewer], tasks=[task1, task2, task3])
result = crew.kickoff()
```

### OpenAI Agents SDK — handoffs in 15 lines

```python
from agents import Agent, Runner

planner = Agent(name="Planner", instructions="Break tasks into steps")
executor = Agent(name="Executor", instructions="Execute the plan")
orchestrator = Agent(name="Orchestrator", instructions="Route tasks", handoffs=[planner, executor])

result = await Runner.run(orchestrator, "Build a landing page")
```

### LangGraph — state machine in 25 lines

```python
from langgraph.graph import StateGraph

def plan(state): return {"plan": "..."}
def execute(state): return {"result": "..."}
def validate(state): return {"valid": True}

graph = StateGraph(dict)
graph.add_node("plan", plan)
graph.add_node("execute", execute)
graph.add_node("validate", validate)
graph.add_edge("plan", "execute")
graph.add_edge("execute", "validate")
app = graph.compile()
```

---

## Common Migration Paths

```
Prototype (CrewAI) → Production (LangGraph)
    Most common. Start fast, migrate when you need state control.

OpenAI SDK → CrewAI or LangGraph
    When you need model flexibility or complex orchestration.

LangChain → LangGraph
    Natural upgrade path. Same ecosystem, more control.

Any Python framework → Mastra
    When your team is TypeScript-native.
```

---

## Decision Matrix

Answer these 4 questions:

| Question | If yes → |
|----------|----------|
| Do I need it working today? | CrewAI or OpenAI SDK |
| Do I need deterministic control over agent flow? | LangGraph |
| Is my team TypeScript-first? | Mastra |
| Am I building a research prototype? | AutoGen |

Still unsure? Start with **CrewAI**. It has the lowest barrier to entry and you can always migrate later.

---

## Links

| Framework | Repo | Docs |
|-----------|------|------|
| CrewAI | [GitHub](https://github.com/crewAIInc/crewAI) | [docs.crewai.com](https://docs.crewai.com) |
| AutoGen | [GitHub](https://github.com/microsoft/autogen) | [microsoft.github.io/autogen](https://microsoft.github.io/autogen) |
| LangGraph | [GitHub](https://github.com/langchain-ai/langgraph) | [langchain-ai.github.io/langgraph](https://langchain-ai.github.io/langgraph) |
| OpenAI SDK | [GitHub](https://github.com/openai/openai-agents-python) | [openai.github.io/openai-agents-python](https://openai.github.io/openai-agents-python) |
| Mastra | [GitHub](https://github.com/mastra-ai/mastra) | [mastra.ai/docs](https://mastra.ai/docs) |

---

## Contributing

Framework missing or info outdated? Open a PR. Keep it factual — no marketing language.

**Rules:**
- Include source links for claims
- Test code examples before submitting
- No subjective "best" claims without context

---

*Last updated: 2026-05-16*
