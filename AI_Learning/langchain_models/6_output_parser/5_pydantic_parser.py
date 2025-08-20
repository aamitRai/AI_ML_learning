from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.output_parsers import PydanticOutputParser 
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

class Person(BaseModel):
    name: str = Field(description="The name of the person")
    age: int = Field(gt=18,description="The age of the person")
    occupation: str = Field(description="The occupation of the person")
parser= PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template="detail of any  {topic} and its detail?  \n {format_instruction}",
    input_variables=["topic"],
    partial_variables={'format_instruction': parser.get_format_instructions()}
)

print("prompt:",template)
chain = template | llm | parser
result = chain.invoke({"topic": "india guy"})
print("Result:", result)