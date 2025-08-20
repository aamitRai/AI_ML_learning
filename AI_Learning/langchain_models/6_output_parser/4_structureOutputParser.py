from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.output_parsers import StructuredOutputParser, ResponseSchema
from langchain_core.prompts import PromptTemplate

load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

# Define the schema first
schema = [
    ResponseSchema(
        name="topic_name",  # Fixed: Use snake_case for field names
        description="The name of topic"
    ),  
    ResponseSchema(
        name="details",
        description="Detailed information about the topic in 5 points"
    ),
    ResponseSchema(
        name="conclusion",
        description="A brief conclusion about the topic in 2 lines"
    )
]

# Create parser from schema (removed the empty parser initialization)
parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template="What is the {topic} and its detail?  \n {format_instruction}",
    input_variables=["topic"],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

chain = template | llm | parser
result = chain.invoke({"topic": "artificial intelligence"})
print("Result:", result)