from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
job_description = """
        We are seeking a highly skilled Full Stack Developer to join our dynamic team.
        You will be responsible for developing and maintaining both frontend and backend systems.
        Collaborate with UI/UX designers, product managers, and QA teams to deliver high-quality software.
        Design and implement RESTful APIs and scalable backend services.
        Develop responsive and interactive web applications using modern frameworks.
        Write clean, testable, and efficient code following industry best practices.
        Ensure application performance, security, and scalability.
        Participate in code reviews and provide constructive feedback.
        Troubleshoot and debug issues across the stack.
        Stay updated with the latest technologies and contribute to continuous improvement.
    """

class JobProfileSchema(BaseModel):
    name: str = Field(..., description="name of the job role")
    skills :str= Field(..., description="find skills of the candidate must have") 
   
structured_model=llm.with_structured_output(JobProfileSchema)
result = structured_model.invoke(job_description)
print("\n ",result)