from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import PromptTemplate
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel,RunnableSequence
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

llm2 = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)
prompt1 =PromptTemplate(
    template="Give me  twitter tweet for the  {topic}",
    input_variables=["topic"]
)
prompt2 =PromptTemplate(
    template="Give me  linkdein post for the  {topic}",
    input_variables=["topic"]
)
parser = StrOutputParser()

chain=RunnableParallel({
   'tweet': RunnableSequence(prompt1 , llm,parser),
   'linkdein': RunnableSequence(prompt2 , llm2,parser)
})

result = chain.invoke({'topic': 'LC Language'})
print("result is ",result)
chain.get_graph().print_ascii()
