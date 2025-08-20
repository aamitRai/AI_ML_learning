from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from pydantic import BaseModel, Field
load_dotenv()
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
review ="""
            It tore within 2 days of use. I am very disappointed with the quality of this product. I expected better from Puma.
            I've been using Puma shoes for a few months now, and overall, I'm quite impressed. The design is sleek and modern, making them great for both workouts and casual wear. They're lightweight, and the cushioning provides decent comfort for daily running or walking. The grip on the sole also performs well on most surfaces.
            The only downside I noticed is that the arch support could be better for those with high arches or specific foot needs. But for the price point, they're definitely a solid and stylish option. Would recommend for general use!
        """
#schema 
class ReviewSchema(BaseModel):
    product_category: str = Field(..., description="Category of the product, e.g., shoes, electronics")
    rating: int = Field(..., description="Rating out of 5")
    summary: str = Field(..., description="Short summary of the review content")
structured_model=llm.with_structured_output(ReviewSchema)

result = structured_model.invoke(review)
print("\n ",result)