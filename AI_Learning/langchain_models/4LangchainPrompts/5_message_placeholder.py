from langchain_core.prompts import MessagesPlaceholder, ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()


# ✅ Define the chat prompt template correctly using 'from_messages'
chat_template = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful customer support agent."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{query}")
])

# ✅ Load chat history
chat_history = []
try:
    with open('chat_history.txt', 'r') as f:
            chat_history.extend(f.readlines())
except FileNotFoundError:
    print("No previous chat history found.")

prompt =chat_template.invoke({
    'chat_history': chat_history,
    'query': ' where is my refund for order #12345?'
    })
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
result=llm.invoke(prompt)
print("Loaded history:", chat_history)
print("\nPrompt:", prompt)
print("AI Response:", result.content)   