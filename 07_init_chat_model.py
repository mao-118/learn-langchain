from langchain.chat_models import init_chat_model
from dotenv import load_dotenv
import os
load_dotenv()
model = init_chat_model(model="deepseek-chat",
                        api_key=os.getenv("OPEN_API_KEY"),
                        base_url=os.getenv("OPEN_BASE_URL"))
print(type(model))