from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate

load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
parser = JsonOutputParser()

template1 = PromptTemplate(
    template="What is the {topic} and its detail?  \n {format_instruction}",
    input_variables=["topic"],
    partial_variables={'format_instruction': parser.get_format_instructions()}  # Fixed typo
)

template2 = PromptTemplate(
    template="Summarize this in 5 points: {text} \n {format_instruction} ",
    input_variables=["text"],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

# Create a proper chain that passes data between prompts
chain = template1 | llm | parser

# Execute the chain with a topic
result1 = chain.invoke({"topic": "artificial intelligence"})  # Added required input
print("First result:", result1)

# Use the result from the first chain as input to the second
chain2 = template2 | llm | parser
result2 = chain2.invoke({"text": str(result1)})  # Pass result1 as text input
print("Final result:", result2)