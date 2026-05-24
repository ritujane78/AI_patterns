<!-- @format -->

# AI Agentic Design Patterns

Welcome to the AI Agentic Design Patterns project! This repository demonstrates practical AI agentic design patterns using Python, Ollama, and OpenAI integrations.

---

# Overview

This repository explores how Large Language Models (LLMs) can be orchestrated using different agentic design patterns.

The project mainly focuses on:

- Multi-Agent Collaboration
- Reflection Pattern
- ReAct (Reason + Act) Pattern
- Tool Usage Pattern
- Local LLM execution using Ollama
- OpenAI-based agent workflows

The implementations are lightweight, educational, and beginner-friendly while still showcasing important concepts used in modern AI systems.

---

# AI Patterns Implemented

## 1. Reflection Pattern

The Reflection Pattern allows an AI agent to:

- Generate an answer
- Critique or review its own response
- Improve the output iteratively

This mimics how humans revise their work.

### Files

- `reflection_pattern_ollama.py`
- `reflection_pattern_openai.py`

### What These Files Demonstrate

These scripts create a workflow where:

1. One agent generates content.
2. Another agent reflects on the generated output.
3. Improvements are suggested or regenerated.

The Ollama version runs locally using open-source models.

The OpenAI version demonstrates the same workflow using OpenAI APIs.

### Key Learning Concepts

- Self-critique loops
- Iterative response improvement
- Agent collaboration
- LLM evaluation workflows

## 2. ReAct Pattern (Reason + Act)

The ReAct Pattern combines:

- Reasoning
- Decision-making
- Tool execution

Instead of only generating text, the AI can think step-by-step and perform actions.

### File

- `reAct_ollama.py`

### What This File Demonstrates

The script showcases:

- Chain-of-thought style reasoning
- Decision making before tool execution
- Action-based AI workflows
- Interactive agent behaviour

The agent alternates between:

```text
Thought → Action → Observation → Final Response
```

### Key Learning Concepts

- Autonomous reasoning
- Agent planning
- External action execution
- Sequential decision workflows


---

## 3. Multi-Agent Pattern

The Multi-Agent Pattern demonstrates how multiple AI agents can collaborate together to solve tasks.

Instead of relying on a single LLM response, responsibilities are divided across specialized agents.

### File

- `multi_agent_pattern_ollama.py`

### What This File Demonstrates

The script includes:

- Multiple conversational agents
- Task delegation
- Collaborative problem solving
- Agent-to-agent communication

Each agent can perform a separate responsibility such as:

- Planning
- Reviewing
- Generating
- Coordinating

### Key Learning Concepts

- Distributed AI systems
- Collaborative intelligence
- Specialized AI agents
- Agent orchestration

## Additional Pattern: Tool Usage Pattern

Although the repository mainly focuses on the three major patterns above, it also explores AI tool integration.


### Key Learning Concepts

- Function calling
- Tool invocation
- AI extensibility
- Agent capabilities enhancement


# Technologies Used

## Core Technologies

- Python
- Ollama
- OpenAI APIs
- AutoGen Framework


Typical libraries include:

```bash
pyautogen
openai
python-dotenv
```

# Running the Project

## Clone the Repository

```bash
git clone https://github.com/ritujane78/AI_patterns.git
cd AI_patterns
```

## Create a Virtual Environment

### Windows

```bash
python -m venv .venv
.venv\Scripts\activate
```
## Install Dependencies

```bash
pip install -r requirements.txt
```
# Screenshots

The `screenshots/` folder contains outputs and execution previews from different experiments.
