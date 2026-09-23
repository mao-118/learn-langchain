from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek
from langchain.agents import create_agent
import os
from langgraph.checkpoint.memory import InMemorySaver
load_dotenv()
model = init_chat_model(model="deepseek-v4-flash",
                        api_key=os.getenv("OPEN_API_KEY"),
                        base_url=os.getenv("OPEN_BASE_URL"))

config = {"configurable": {"thread_id": "thread_1"}}
agent = create_agent(model=model,checkpointer=InMemorySaver())
result = agent.invoke(
    {"messages":[{"role":"user","content":"hello！我是jack，我喜欢猫猫"}]},
    config
)
print(result)
result = agent.invoke(
    {"messages":[{"role":"user","content":"我喜欢什么"}]},
    config
)
print(result)