from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()  
model=ChatOpenAI(model="gpt-3.5-turbo-instruct")  # Uses OPENAI_API_KEY from environment
print(model.invoke("What is the capital of India?"))  # Print the result
