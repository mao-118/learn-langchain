import os
from dotenv import load_dotenv
from langchain.tools import tool
from langchain.agents import create_agent
from langchain_deepseek import ChatDeepSeek
from langchain.messages import HumanMessage
load_dotenv()
key = os.getenv("OPEN_API_KEY")
url = os.getenv("OPEN_BASE_URL")
@tool
def get_weather(city):
    """查询指定城市天气情况。
        Args:
            city 城市名称
    """
    weather_data = {
        "杭州": "晴，25°C，湿度 60%",
        "北京": "多云，18°C，湿度 45%",
        "上海": "小雨，22°C，湿度 80%",
    }
    if weather_data.get(city):   
        return f"{weather_data.get(city)}，今天天气晴朗，适合外出。"
    else:
        return "抱歉，未找到该城市天气信息"
def intent_check(query: str) -> tuple[bool, str]:
    """
    使用LLM做意图判断
    返回：(是否允许执行agent,拒绝提示文本)
    """
    check_system = """
        你是意图分类器。判断用户的问题是否为天气查询相关问题。
        只允许输出 true 或者 false，不要输出任何其他解释、标点、多余文字。
        - true：用户询问某个城市的天气、气温、湿度等天气相关
        - false：闲聊、写诗、写代码、科普、历史、其他无关问题
    """
    resp = llm.invoke([
        {"role": "system", "content": check_system},
        {"role": "user", "content": query}
    ])
    result = resp.content.strip().lower()
    print("意图",resp.content)
    if result == "true":
        return True, ""
    else:
        return False, "不好意思，我仅能查询天气，请提问天气相关问题。"
llm = ChatDeepSeek(
    api_key=os.getenv("OPEN_API_KEY"),
    base_url=os.getenv("OPEN_BASE_URL"),
    model="deepseek-v4-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2
)
agent = create_agent(
    model=llm,
    tools=[get_weather],
    system_prompt="你是一个天气查询助手"
)
# user_query =  {"messages": [{"role":"user","content":"天津天气如何"}]}
# res = agent.invoke(user_query)
# print(res["messages"][-1].content)


# 意图判断
# user_query = "今天吃什么"
user_query = "今天杭州天气如何"
allow_run, reject_msg = intent_check(user_query)
if not allow_run:
    print(reject_msg)
else:
    inputs = {"messages": [{"role": "user", "content": user_query}]}
    res = agent.invoke(inputs)
    print(res["messages"][-1].content)