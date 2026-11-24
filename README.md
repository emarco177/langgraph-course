# ReAct Agent with LangGraph and Function Calling

Code for **Section 6 — Implementing ReAct AgentExecutor with LangGraph** of the Udemy course [LangGraph- Develop LLM powered AI agents with LangGraph](https://www.udemy.com/course/langgraph/?couponCode=NOV-2026).

The agent reasons with an OpenAI chat model that has tools bound to it (function calling) and acts through LangGraph's prebuilt `ToolNode`:

- `react.py` — the tools (`TavilySearch` and a custom `triple` tool) and the LLM with the tools bound
- `nodes.py` — the reasoning node and the `ToolNode`
- `main.py` — the `StateGraph` over `MessagesState`, with a conditional edge that loops between reasoning and acting

## Lessons → commits

| Lecture | Commit |
|---|---|
| L38 Get Started: Setting Up Your ReAct Agent Project Environment | [`54bda11`](https://github.com/emarco177/langgraph-course/commit/54bda11) |
| L39 Coding the Agent's Brain: Implementing the ReAct Runnable | [`f608c78`](https://github.com/emarco177/langgraph-course/commit/f608c78) |
| L40 Building Blocks: Defining Your Agent's Nodes in LangGraph | [`6ae4adb`](https://github.com/emarco177/langgraph-course/commit/6ae4adb) |
| L41–L42 Connecting the nodes and running the graph | [`83e59d7`](https://github.com/emarco177/langgraph-course/commit/83e59d7) |

## Run it

Create a `.env` file:

```bash
OPENAI_API_KEY=...
TAVILY_API_KEY=...
LANGSMITH_API_KEY=...      # optional, for tracing
LANGSMITH_TRACING=true     # optional
```

Then, with [uv](https://docs.astral.sh/uv/):

```bash
git checkout project/ReAct-Agent-Function-Calling
uv sync
uv run main.py
```

`main.py` also writes the graph to `flow.png` (this uses the mermaid.ink web service, so it needs internet access).
