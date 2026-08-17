import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("OPEN_API_KEY")
if api_key:
    print(api_key)
else:
    print("未配置")