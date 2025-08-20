from langchain_core.tools import tool

@tool
def multiply(a,b):
    """Multiply tow number"""
    return a*b

@tool
def add(a,b):
    """Add tow number"""
    return a+b

class MathToolkit:
    def get_tools(self):
        return [add,multiply]

tools=MathToolkit()
tool=tools.get_tools()
for t in tool:
    print(t.description)