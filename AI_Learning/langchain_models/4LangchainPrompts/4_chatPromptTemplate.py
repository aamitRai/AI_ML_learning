from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables from .env file (e.g., API keys)
load_dotenv()
# Initialize the Google Generative AI model
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
chat_template=ChatPromptTemplate([
   ('system' ,'You are a helpful {domain} expert.'),
   ('human' ,'Explain in the simple terms , what is {topic} ?'),
])
prompt=chat_template.invoke({
    'domain': 'AI',
     'topic': 'Generative AI'})

print(prompt)
result = llm.invoke(prompt)
print("AI:", result.content)
