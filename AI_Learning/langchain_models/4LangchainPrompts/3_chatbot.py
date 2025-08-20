from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


# Load environment variables from .env file (e.g., API keys)
load_dotenv()

# Initialize the Google Generative AI model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

# Optional: Store chat history if you want to show/use it later
messages=[
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Hello! How can I assist you today?"),
]

# Start chat loop
while True:
    input_text = input("You: Enter your question (or type 'exit' to quit): ")
    if input_text.lower() == 'exit':
        print("Chat ended.")
        break
    else:
        messages.append(HumanMessage(content=input_text))
        result = llm.invoke(messages)
        messages.append(AIMessage(content=result.content))
        print("AI:", result.content)
