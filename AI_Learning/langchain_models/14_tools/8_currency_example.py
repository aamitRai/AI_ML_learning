from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.tools import tool
import requests

load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

@tool
def currency_convert(rate,value):
    """Multiply the current curreny rate with the user want to convert into which curreny"""
    print("converter called,",rate,value)
    return rate*value
@tool
def currency_conversion_rate(cur1: str, cur2: str) -> float:
    """
    Fetch the conversion rate from cur1 to cur2 using exchangerate-api.com.
    """
    URL = f"https://v6.exchangerate-api.com/v6/a7dca24a028417ec2709b087/latest/{cur1.upper()}"
    response = requests.get(URL)
    data = response.json()
    if response.status_code != 200 or data.get("result") != "success":
        raise Exception(f"API error: {data.get('error-type', 'Unknown error')}")
    conversion_rates = data.get("conversion_rates", {})
    rate = conversion_rates.get(cur2.upper())
    if rate is None:
        raise ValueError(f"Currency '{cur2}' not available in conversion rates.")

    return rate

llm_with_tools=llm.bind_tools([currency_conversion_rate,currency_convert])
tools_suggested=llm_with_tools.invoke("convert 1 euro in indian ruppess")
# Inspect tool call suggestions
print("Tool calls:", tools_suggested.tool_calls)

# Execute the tools based on tool_calls
for tool_call in tools_suggested.tool_calls:
    if tool_call["name"] == "currency_conversion_rate":
        rate = currency_conversion_rate.invoke(tool_call["args"])
        print("Rate:", rate)
    elif tool_call["name"] == "currency_convert":
        result = currency_convert.invoke(tool_call["args"])
        print("Converted Value:", result)