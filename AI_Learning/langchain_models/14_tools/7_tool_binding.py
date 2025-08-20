from json import tool
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.tools import tool

load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

@tool
def multiply(a,b):
    """Multiply tow number"""
    return a*b

@tool
def add(a,b):
    """Add two number"""
    return a+b

llm_with_tools=llm.bind_tools([add,multiply])
result=llm_with_tools.invoke("can you multiple 3 by 3")
print("result",result.tool_calls)

res=multiply.invoke(result.tool_calls[0])
print(res)