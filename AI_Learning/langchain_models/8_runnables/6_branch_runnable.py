from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableSequence, RunnableBranch, RunnablePassthrough

# Initialize the LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

# Define prompts
prompt1 = PromptTemplate(
    template="Give me a report in 1000 words about {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Summarize the following text in 50 words: {text}",
    input_variables=["text"]
)

# Initialize parser
parser = StrOutputParser()

# Create chains
chain1 = RunnableSequence(prompt1, llm, parser)
chain2 = RunnableSequence(prompt2, llm, parser)

# Create branch chain - Fixed to handle dictionary input
branch_chain = RunnableBranch(
    (lambda x: len(x["text"].split()) > 20, chain2),
    lambda x: x["text"]  # Extract just the text if no summarization needed
)

# Create final chain - Fixed the input/output flow
final_chain = RunnableSequence(
    chain1,
    {"text": RunnablePassthrough()},  # Map output to 'text' key for chain2
    branch_chain
)

# Execute the chain
result = final_chain.invoke({'topic': 'eating 100 gm paneer and 500 ml of milk everyday'})
print("Result is:", result)

# Print the graph
try:
    final_chain.get_graph().print_ascii()
except Exception as e:
    print(f"Graph visualization error: {e}")

# Example workflow:
# Input topic -> prompt1 -> llm -> parser -> check word count -> 
# if >20 words: summarize with chain2, else: pass through unchanged