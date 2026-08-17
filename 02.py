import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
llm = ChatOpenAI(
    model="glm-5.2",
    openai_api_key=os.getenv("OPEN_API_KEY"),
    openai_api_base = os.getenv("OPEN_BASE_URL"),
    temperature=0.7,
    max_tokens=1024
)

response = llm.invoke("你好，你是谁")
print(response.content)