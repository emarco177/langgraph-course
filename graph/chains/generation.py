from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from langsmith import Client

client = Client()

llm = ChatOpenAI(temperature=0)
prompt = client.pull_prompt("rlm/rag-prompt")

generation_chain = prompt | llm | StrOutputParser()
