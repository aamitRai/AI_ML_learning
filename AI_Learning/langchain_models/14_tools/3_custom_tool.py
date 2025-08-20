from langchain_core.tools import tool

@tool
def multiply(a,b):
    """Multiply tow number"""
    return a*b

result=multiply.invoke({"a":4,"b":3})
print("result",result)
print(multiply.name)
print(multiply.description)
print(multiply.args)