from langchain_google_genai import ChatGoogleGenerativeAI
#from langchain_ollama import ChatOllama
from langchain.agents import create_agent
from pydantic import BaseModel, Field
from agent.tools import recommend_tool
from typing import List

# Define the structured response format for a single product
class ProductInfo(BaseModel):
    name: str = Field(description="Name of the product")
    price: float = Field(description="Price in USD")
    rating: float = Field(description="Rating of the product")
    reviews: int = Field(description="Number of reviews")
    discount: float = Field(description="Discount percentage if available")
    imgUrl: str = Field(description="URL of the product image")
    productURL: str = Field(description="URL of the product page")

# This is the wrapper that forces the model to return MULTIPLE products
class ProductList(BaseModel):
    products: List[ProductInfo] = Field(description="A list of 5 products found")

    
def create_agents():
    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite") #Gemini model
    # model = ChatOllama(model="granite3.1-dense:2b", format=ProductList.model_json_schema()) #Ollama model

    tools = [recommend_tool]

    agent = create_agent(model=model, tools=tools, response_format=ProductList)

    return agent

