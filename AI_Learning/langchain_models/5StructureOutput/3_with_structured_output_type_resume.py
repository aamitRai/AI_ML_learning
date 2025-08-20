from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
resume ="""
      PROFESSIONAL SUMMARY
Self-motivated and detail-oriented Computer Science graduate with 1+ years of full-stack development experience.
Strong command over JavaScript (React, Node.js), Python (FastAPI, ML basics), and cloud platforms like AWS. Adept
in building user-centric applications and deploying scalable systems with RESTful APIs. Experienced in Agile, version
control, and cross-functional collaboration. Excited to bring a curious, impact-driven mindset to high-growth
environments.
AMIT RAI
+91 8602638324 | amitrai8602@gmail.com | Indore, India
FULL STACK DEVELOPER
Date of birth  :2002-01-15
TECHNICAL SKILLS
PROFESSIONAL EXPERIENCE
Languages: JavaScript (ES6+), Python, Java, TypeScript, SQL
Frontend: React, Angular, HTML5, CSS, Bootstrap
Backend: Node.js, Express, Spring Boot, Django, FastAPI
Cloud/DevOps: AWS (EC2, S3), Docker, Git, CI/CD
Databases: PostgreSQL, MySQL, MongoDB, DynamoDB
Tools: Postman, Swagger, JIRA, Trello, GitHub
AI/ML Basics: NumPy, Pandas, Matplotlib
Data Structures & Algorithms: Strong problem-solving foundation
Full Stack Developer
Fealty Technologies Pvt. Ltd., India
2023 - Current
Designed and deployed high-performance REST APIs using FastAPI and MySQL for internal and external
applications.
Developed Angular-based interfaces with dynamic chart visualizations using Chart.js.
Reduced backend API response time by 30% through performance tuning and scalable architecture.
Integrated AI-based automation features using Python for enhanced user interaction and reporting.
Managed database maintenance, deployed projects to production, and integrated third-party APIs for
extended functionality.
Engineered solutions integrating AI features, while continuously learning and experimenting with
emerging AI tools and frameworks.
linkedin.com/in/amitrai2002
KEY PROJECTS
Mining Management :
Role: Full Stack Developer
Technologies: React, Fast API, Chart.js, Bootstrap 5, Mysql.
Achievement: Developed robust backend services to extract, transform, and serve mining
sector data, enabling seamless UI visualization through RESTful APIs.
Impact: Streamlined data processing workflows, reducing manual effort and improving data
accessibility for stakeholders. Enhanced system reliability and enabled real-time data
visualization for better decision-making.
Cricket Tournament & Venue Management
Role: Full Stack Developer
Technologies: React.js, Node Express, TypeScript, MongoDB.
Achievement: Built a multi-role platform supporting players, partners, venue owners, and
admins across four integrated apps. Developed key modules for user registration, team
management, tournament participation, venue listing, slot booking, and subscription handling
with end-to-end functionality.
Impact: enabled seamless collaboration between users, streamlined tournament and venue
operations, and improved booking efficiency. Enhanced platform scalability and user
engagement through role-based access and real-time slot management.
B2B Shipping Management
Role: Full Stack Developer
Technologies: Java, Spring Boot, Spring Data JPA, React.js, MySQL.
Achievement: Developed a B2B shipping management platform integrating admin and client
modules, enabling vendors to manage products, inventory, shipments, and real-time tracking
through robust backend services and seamless frontend integration.
Impact: Streamlined shipping operations and improved order management efficiency for vendor
companies by integrating with major e-commerce platforms.
Cloud Kitchen Management
Role: Backend Developer
Technologies: Django, Python and Django ORM.
Achievement: Implemented scalable backend features using Django and Django ORM to
support a cloud-based culinary platform.
Impact: Improved system efficiency and data reliability, enhancing overall user experience and
operational flow.
EDUCATION
Bachelor of Technology in Computer Science
Swami Vivekanand College of Engineering Indore | 2020 - 2024
English (Professional) Hindi (Native)
DECLARATION : I hereby declare that the details mentioned in my resume are true and correct to
the best of my knowledge and belief.
LANGUAGE    """
#schema 
class ResumeSchema(BaseModel):
    name: str = Field(..., description="name of the  candidateperson of the resume")
    age: int = Field(..., description="find age of the candidate")
    degree:str = Field(..., description="find degree  of the candidate")
    skills :str= Field(..., description="find skills of the candidate") 
    experience: str = Field(..., description="Short summary of the review content")

structured_model=llm.with_structured_output(ResumeSchema)
result = structured_model.invoke(resume)
print("\n ",result)