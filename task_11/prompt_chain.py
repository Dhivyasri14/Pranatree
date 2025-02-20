from dotenv import load_dotenv
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain_openai import ChatOpenAI
import os

# Load environment variables from .env
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Create a ChatOpenAI model
model = ChatOpenAI(model="gpt-4", api_key=OPENAI_API_KEY)

# Define prompt templates for the travel assistant
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a travel assistant who specializes in recommending tourist attractions based on user queries. "
                   "If the query is irrelevant or cannot be answered, politely inform the user and redirect them to ask about travel."),
        ("human", "The user is interested in: {request}. Can you suggest some popular destinations?"),
    ]
)


def recommend_tourist_places(request):
    chain = prompt_template | model | StrOutputParser()
    return chain.invoke({"request": request})

# Run the chain
request = "I want the tourist places in Kerala"
result = recommend_tourist_places(request)
print(f"Suggestions for '{request}':\n{result}")
