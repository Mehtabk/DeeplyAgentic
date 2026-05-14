# Framework Comparisons

> Side-by-side comparisons of agent frameworks. Pick the right tool for your use case.

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
| **Learning curve** | Low | Medium | High | Low | Low |
| **Best for** | Quick prototypes | Research/complex | Production workflows | Simple pipelines | TS/Node teams |
| **Weakness** | Less control at scale | Verbose setup | Steep learning curve | Limited customization | Younger ecosystem |

## When to Use What

```
Need it running in 1 hour?       → OpenAI Agents SDK or CrewAI
Building for production scale?   → LangGraph
Research or complex reasoning?   → AutoGen
TypeScript / Node.js team?       → Mastra
Role-based agent teams?          → CrewAI
```

## Orchestration Patterns

| Pattern | Description | Best Framework |
|---------|-------------|----------------|
| Sequential pipeline | A → B → C | OpenAI Agents SDK |
| Fan-out / Fan-in | Split → parallel → merge | LangGraph, AutoGen |
| Hierarchical | Manager delegates to workers | CrewAI |
| Conversation | Agents discuss until consensus | AutoGen |
| State machine | Explicit transitions between states | LangGraph |

## Model Support

| Framework | OpenAI | Anthropic | Local/Ollama | Google | AWS Bedrock |
|-----------|--------|-----------|--------------|--------|-------------|
| CrewAI | ✅ | ✅ | ✅ | ✅ | ✅ |
| AutoGen | ✅ | ✅ | ✅ | ✅ | ✅ |
| LangGraph | ✅ | ✅ | ✅ | ✅ | ✅ |
| OpenAI SDK | ✅ | ❌ | ❌ | ❌ | ❌ |
| Mastra | ✅ | ✅ | ✅ | ✅ | ⚠️ |

---

## Contributing

Framework missing or info outdated? Open a PR. Keep it factual — no marketing language.

---

*Last updated: 2026-05-14*
