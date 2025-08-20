from dotenv import load_dotenv
from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api._errors import TranscriptsDisabled, NoTranscriptFound
from langchain.text_splitter import RecursiveCharacterTextSplitter, Language
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_chroma import Chroma
from langchain.schema import Document
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import (
    RunnableParallel, RunnablePassthrough, RunnableLambda
)

# Load environment variables
load_dotenv()

# --- Format Function ---
def format_docs(retrieved_docs):
    return "\n\n".join(doc.page_content for doc in retrieved_docs)

# --- Main Logic ---
video_id = "MG-Ac4TAvTY"

try:
    # Step 1: Fetch transcript from YouTube
    transcript_list = YouTubeTranscriptApi.get_transcript(video_id, languages=["en"])
    transcript = " ".join(chunk["text"] for chunk in transcript_list)

    # Step 2: Split transcript
    splitter = RecursiveCharacterTextSplitter.from_language(
        language=Language.PYTHON,
        chunk_size=200,
        chunk_overlap=2
    )
    chunks = splitter.create_documents([transcript])

    # Step 3: Generate embeddings
    embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

    # Step 4: Store documents in Chroma vector DB
    vector_store = Chroma(
        persist_directory="chroma_db",
        collection_name="ipl_players",
        embedding_function=embedding,
    )
    
    # Uncomment below if running for the first time
    # vector_store.add_documents(chunks)

    # Step 5: Set up retriever
    retriever = vector_store.as_retriever(search_kwargs={"k": 3})

    # Step 6: Chain to get context from retriever and pass the question
    parallel_chain = RunnableParallel({
        'context': retriever | RunnableLambda(format_docs),
        'question': RunnablePassthrough()
    })

    # Step 7: Invoke the retriever pipeline with a question
    question = "What is the optimized solution?"
    inputs = parallel_chain.invoke(question)

    # Step 8: LLM setup
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")

    # Step 9: Create prompt
    prompt_template = PromptTemplate.from_template(
        """
        Answer the following question in very easy language:

        Context:
        {context}

        Question:
        {question}
        """
    )

    # Step 10: Format prompt
    final_prompt = prompt_template.invoke(inputs)

    # Step 11: Invoke LLM with final prompt
    answer = llm.invoke(final_prompt)
    print("Answer:\n", answer)

except TranscriptsDisabled:
    print("Transcripts are disabled for this video.")
except NoTranscriptFound:
    print("No transcript found in the specified language.")
