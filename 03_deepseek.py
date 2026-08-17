import os
from dotenv import load_dotenv
from langchain_deepseek import ChatDeepSeek
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
res = llm.invoke("你好，介绍一下你自己")
print(res.content)