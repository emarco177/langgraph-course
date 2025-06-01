from dotenv import load_dotenv
from langchain_core.messages import BaseMessage
from react import llm, SYSTEM_MESSAGE

load_dotenv()


def run_agent_reasoning_engine(state: list[BaseMessage]) -> list[BaseMessage]:
    response = llm.invoke([{"role": "system", "content": SYSTEM_MESSAGE}, *state])

    return [response]
