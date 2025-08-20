from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate

llm = HuggingFacePipeline.from_model_id(
    model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation",
    pipeline_kwargs=dict(
        temperature=0.5,
        max_new_tokens=100
    )
)
model = ChatHuggingFace(llm=llm)


template1 = PromptTemplate(
    template="What is the {topic} and its detail?",
    input_variables=["topic"]
)

template2 = PromptTemplate(
    template="Summarize this in 5 points: {text}",
    input_variables=["text"]
)

parser = StrOutputParser()
chain = template1 | model | parser |template2 | model |parser
# result = model.invoke("What is the capital of iran  and its detail?")
# result = model.invoke("Summarize this in 5 points " + result.content)
result=chain.invoke({'topic': 'Manifestation'})
print("\n ", result)