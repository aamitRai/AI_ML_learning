from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
load_dotenv()
from langchain_core.prompts import PromptTemplate
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.output_parsers import PydanticOutputParser 
from typing import Literal
from langchain_core.runnables import RunnableParallel , RunnableLambda ,RunnableBranch

class FeedbackOutput(BaseModel):
    result:Literal['positive','negative']= Field(description="The  result always positive or negative single word")
parser2= PydanticOutputParser(pydantic_object=FeedbackOutput)
prompt1 =PromptTemplate(
    template="Classify the feedback text  into positive or negative: {feedback} \n {format_instruction}",
    input_variables=["feedback"],
    partial_variables={'format_instruction': parser2.get_format_instructions()}
)
classifier_chain= prompt1 | llm |parser2
feedback='The product is worst!'


promt2=PromptTemplate(
    template="Write an apppropriate response to this postive feedback {feedback}",
    input_variables=["feedback"]
)
promt3=PromptTemplate(
    template="Write an apppropriate response to this negative feedback {feedback}",
    input_variables=["feedback"]
)

chain2 = promt2 | llm | StrOutputParser()
chain3 = promt3 | llm | StrOutputParser()
branch_chain=RunnableBranch(
    (lambda x:x.result=='positive',chain2),
    (lambda x:x.result=='negative',chain3),
   RunnableLambda(lambda X: "could not classify the feedback")
)
final_chain= classifier_chain| branch_chain
result=final_chain.invoke({'feedback':feedback })
print("Result:", result)