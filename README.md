# Agentic RAG with LangGraph 🦜🔍

Implementation of Reflective RAG, Self-RAG & Adaptive RAG tailored towards developers and production-oriented applications for learning LangGraph🦜🕸️.

This repository contains a refactored version of the original [LangChain's Cookbook](https://github.com/mistralai/cookbook/tree/main/third_party/langchain),

See Original YouTube video:[Advance RAG control flow with Mistral and LangChain](https://www.youtube.com/watch?v=sgnrL7yo1TE)

of [Sophia Young](https://x.com/sophiamyang) from Mistral & [Lance Martin](https://x.com/RLanceMartin) from LangChain

![Logo](https://github.com/emarco177/langgraph-course/blob/project/agentic-rag/static/Langgraph%20Adaptive%20Rag.png)
[![udemy](https://img.shields.io/badge/LangGraph🦜🔗%20Udemy%20Course-%20Coupon%20%2412.99-brightgreen)](https://www.udemy.com/course/langgraph/?couponCode=NOV-2026)


## Features

- **Refactored Notebooks**: The original LangChain notebooks have been refactored to enhance readability, maintainability, and usability for developers.
- **Production-Oriented**: The codebase is designed with a focus on production readiness, allowing developers to seamlessly transition from experimentation to deployment.
- **Test Coverage**: Comprehensive test coverage ensures the reliability and stability of the application, enabling developers to validate their implementations effectively.
- **Documentation**: Detailed documentation and branches guides developers through setting up the environment, understanding the codebase, and utilizing LangGraph effectively.


## What You'll Learn

- **Agentic RAG Implementation**: Build a system that can make intelligent decisions about retrieving information
- **Graph-Based Control Flow**: Use LangGraph to create sophisticated control flows for your RAG pipeline
- **Document Relevance Evaluation**: Implement logic to grade document relevance and detect hallucinations
- **Adaptive Information Retrieval**: Create a system that can switch between local knowledge and web search
- **State Management**: Implement proper state handling for complex information flows

## Tutorial Structure

This repository is organized as a series of commits, each representing a video lesson in building the Agentic RAG system:

| Lesson # | Commit | Description | Key Components |
|----------|--------|-------------|----------------|
| 1 | [**Start Here**](https://github.com/emarco177/langgraph-course/commit/80323ce) | Introduction to the course and Agentic RAG concepts | Overview of the project; Introduction to LangGraph and Agentic RAG architecture |
| 2 | [**Project Structure**](https://github.com/emarco177/langgraph-course/commit/3490983) | Setting up the project foundation | Initialize project structure; Configure uv for dependency management |
| 3 | [**Ingestion**](https://github.com/emarco177/langgraph-course/commit/12bd85e) | Setting up the vector database | Create ingestion pipeline; Implement vector store with Chroma and OpenAI embeddings |
| 4 | [**State**](https://github.com/emarco177/langgraph-course/commit/55f26d8) | Defining the state management | Create GraphState class; Set up typed dictionaries for state tracking |
| 5 | [**Retrieve Node**](https://github.com/emarco177/langgraph-course/commit/1cb0579) | Implementing the document retrieval | Build retrieve node; Connect retrieval to vector database |
| 6 | [**Grade Documents Node**](https://github.com/emarco177/langgraph-course/commit/ac83fb0) | Evaluating document relevance | Create document grading functionality; Implement decision logic for document relevance |
| 7 | [**Web Search with Tavily**](https://github.com/emarco177/langgraph-course/commit/d26339b) | Adding external search capability | Integrate Tavily search API; Implement fallback for insufficient local knowledge |
| 8 | [**Generation Node**](https://github.com/emarco177/langgraph-course/commit/5b47047) | Creating the answer generation component | Build generate node; Implement context-aware response generation |
| 9 | [**Graph**](https://github.com/emarco177/langgraph-course/commit/b8e0436) | Constructing the complete LangGraph workflow | Connect all nodes into workflow; Implement conditional edges for adaptive behavior |
| 10 | [**Self-RAG**](https://github.com/emarco177/langgraph-course/commit/e3de720) | Adding self-evaluation capabilities | Implement hallucination detection; Create feedback loops for answer improvement |
| 11 | [**Router**](https://github.com/emarco177/langgraph-course/commit/da87fe6) | Smart query routing | Create intelligent routing between retrieval and web search; Optimize entry point for different query types |
| 12 | [**Formatting**](https://github.com/emarco177/langgraph-course/commit/1b5f496) | Final code formatting and cleanup | Code optimization; Final documentation improvements |

## Environment Variables

To run this project, you will need to add the following environment variables to your .env file:

```bash
OPENAI_API_KEY=your_openai_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here  # For web search capabilities
LANGSMITH_API_KEY=your_langsmith_api_key_here  # Optional, for tracing
LANGSMITH_TRACING=true                         # Optional
LANGSMITH_PROJECT=agentic-rag                  # Optional
```

> **Important Note**: If you enable tracing by setting `LANGSMITH_TRACING=true`, you must have a valid LangSmith API key set in `LANGSMITH_API_KEY`. Without a valid API key, the application will throw an error.

## Getting Started

Clone the repository:

```bash
git clone https://github.com/emarco177/langgraph-course.git
cd langgraph-course
git checkout project/agentic-rag
```

Install dependencies:

```bash
uv sync
```

Run the graph as a local Agent Server (LangSmith Studio and the server API):

```bash
uv run langgraph dev
```

`langgraph.json` tells the server where the compiled graph is (`./graph/graph.py:app`). The vector store is not in the repository: build it once by uncommenting the `Chroma.from_documents` block in `ingestion.py` and running `uv run ingestion.py`.

Follow along with each commit to learn the process of building an Agentic RAG system:

```bash
# View all commits in the tutorial
git log --oneline

# Check out specific lessons:
git checkout 7c9fc71  # Lesson 1: Start Here
git checkout b502232  # Lesson 2: Project Structure
git checkout fbd3084  # Lesson 3: Ingestion
git checkout f055aeb  # Lesson 4: State
git checkout 98176f0  # Lesson 5: Retrieve Node
```

## Prerequisites

- Python 3.10+
- Basic understanding of LLMs and RAG systems
- Familiarity with Python and vector databases (helpful but not required)

## Run Locally

Clone the project

```bash
  git clone https://github.com/emarco177/langgraph-course.git
```

Go to the project directory

```bash
  cd langgraph-course
```

Install dependencies

```bash
  uv sync
```

Start the Agentic Rag flow

```bash
  uv run main.py
```

## Running Tests

To run tests, run the following command

```bash
  uv run pytest . -s -v
```
## Acknowledgements

Original LangChain repository: [LangChain Cookbook](https://github.com/mistralai/cookbook/tree/main/third_party/langchain)
By [Sophia Young](https://x.com/sophiamyang) from Mistral & [Lance Martin](https://x.com/RLanceMartin) from LangChain
![Logo](https://github.com/emarco177/langgraph-course/blob/project/agentic-rag/static/LangChain-logo.png)



## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://www.udemy.com/course/langgraph/?referralCode=FEA50E8CBA24ECD48212)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/eden-marco/)
[![Twitter Follow](https://img.shields.io/twitter/follow/EdenEmarco177?style=social)](https://twitter.com/EdenEmarco177) 