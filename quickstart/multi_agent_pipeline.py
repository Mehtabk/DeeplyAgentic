"""Multi-Agent Pipeline — DeeplyAgentic Quickstart

A minimal Planner → Executor → Validator pipeline using OpenAI Agents SDK.
Demonstrates the 4-layer architecture in ~60 lines.

Usage:
    pip install openai-agents
    export OPENAI_API_KEY=your-key-here
    python multi_agent_pipeline.py
"""

from agents import Agent, Runner
import asyncio

# Layer 1: Guardrails (built into each agent's instructions)
# Layer 2: Tools (agents can call each other)
# Layer 3: Agents (Planner, Executor, Validator)
# Layer 4: Orchestrator (routes the task)

planner = Agent(
    name="Planner",
    instructions="""You are a planning agent. Break down the user's goal into 3-5 concrete steps.
    For each step, specify: what to do, what tool/resource is needed, and how to verify success.
    Output a numbered list. Be specific and actionable.""",
)

executor = Agent(
    name="Executor",
    instructions="""You are an execution agent. You receive a plan and execute it step by step.
    For each step, describe what you did and confirm the result.
    If a step cannot be completed, explain why and suggest an alternative.""",
)

validator = Agent(
    name="Validator",
    instructions="""You are a validation agent. Review the executor's output against the original goal.
    Check for: completeness, accuracy, and quality.
    Output: PASS, PASS WITH NOTES, or FAIL — with a brief explanation.""",
)

orchestrator = Agent(
    name="Orchestrator",
    instructions="""You coordinate a multi-agent pipeline.
    1. Send the task to the Planner for decomposition
    2. Send the plan to the Executor for implementation
    3. Send the result to the Validator for quality check
    4. Return the final validated output to the user
    Always explain which agent you're routing to and why.""",
    handoffs=[planner, executor, validator],
)


async def main():
    task = input("\n🎯 Enter your task: ") or "Create a project README for a Python CLI tool"
    print(f"\n🚀 Running pipeline for: {task}\n")
    print("=" * 50)

    result = await Runner.run(orchestrator, task)
    print("\n" + "=" * 50)
    print("\n✅ Final Output:\n")
    print(result.final_output)


if __name__ == "__main__":
    asyncio.run(main())
