from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()  # Loads variables from .env into environment
model = ChatAnthropic(model="claude-2")  # Uses ANTHROPIC_API_KEY from environment          
result = model.invoke("What is the capital of India?")  # Invoke the model with a question
print(result)  # Print the result