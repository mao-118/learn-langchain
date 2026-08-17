from langchain.tools import tool
@tool
def hello_tool(name):
    """向指定的人打招呼
        Args:
            name: 要打招呼的人名
    """
    return "你好"+name

res = hello_tool.invoke({"name":"tom"})
print(res)