from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

# Load environment variables from .env file (e.g., API keys)
load_dotenv()
# Initialize the Google Generative AI model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
messages=[
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Hello! How can I assist you today?"),
]
result = llm.invoke(messages)
messages.append(AIMessage(content=result.content))
print(messages)