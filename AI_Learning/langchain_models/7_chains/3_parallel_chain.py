from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import PromptTemplate
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
from langchain_core.output_parsers import StrOutputParser
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline

from langchain_core.runnables import RunnableParallel , RunnableLambda

llm2 = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)

# Fix: Pass llm as keyword argument
model = ChatHuggingFace(llm=llm2)

prompt1 =PromptTemplate(
    template="Generate a 1 page report for this topic  {topic} add introduction, body and conclusion with headings",
    input_variables=["topic"]
)
prompt2 =PromptTemplate(
    template="Give me 5 small interesting facts about {topic}",
    input_variables=["topic"]
)

prompt3 =PromptTemplate(
    template="Give me 3 small interesting question for the {text}",
    input_variables=["text"]
)
parser = StrOutputParser()

parallel_chain =RunnableParallel(
    {
      'report' :  prompt1 | llm | parser,
       'fact' : prompt2 | model | parser,
    }
)
merge_inputs = RunnableLambda(lambda x: {"text": x["report"] + "\n" + x["fact"]})
merge_chain =prompt3 | llm | parser
chain = parallel_chain | merge_inputs | prompt3 | llm | parser

result = chain.invoke({'topic': 'Love'})
print("\n📝 Result:\n", result)

# Optional: Visualize chain
chain.get_graph().print_ascii()