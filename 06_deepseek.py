from langchain_deepseek import ChatDeepSeek
from langchain.agents import create_agent
from langchain.tools import tool
import os
from dotenv import load_dotenv

load_dotenv()
llm = ChatDeepSeek(
    api_key=os.getenv("OPEN_API_KEY"),
    base_url=os.getenv("OPEN_BASE_URL"),
    model="deepseek-v4-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2
)
@tool
def get_weather(city):
    """获取指定城市天气
    """
    return f"{city}天气晴朗"

agent = create_agent(model=llm,tools=[get_weather],system_prompt="你是一个天气助手")
result = agent.invoke(
    {"messages":[{"role":"user","content":"上海天气如何"}]}
)
print(result)
# print(result["messages"][-1].content)