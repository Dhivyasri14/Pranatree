import cohere
from sentence_transformers import SentenceTransformer
from langchain.prompts import ChatPromptTemplate
from langchain.schema.output_parser import StrOutputParser
from langchain.chat_models import ChatOpenAI  # Ensure you're using this for chat-based models
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
COHERE_API_KEY = os.getenv("COHERE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Initialize models
cohere_client = cohere.Client(COHERE_API_KEY)
hf_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
model = ChatOpenAI(model="gpt-4", api_key=OPENAI_API_KEY)  # Make sure this is the correct class

# Create LangChain prompt template for travel assistant
prompt_template = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a travel assistant who specializes in recommending tourist attractions based on user queries. "
                   "If the query is irrelevant or cannot be answered, politely inform the user and redirect them to ask about travel."),
        ("human", "The user is interested in: {request}. Can you suggest some popular destinations?"),
    ]
)

# Define functions for embedding generation
def get_cohere_embedding(text):
    response = cohere_client.embed(
        texts=[text],
        model="large"  # Use the appropriate model
    )
    return response.embeddings[0]

def get_hf_embedding(text):
    return hf_model.encode(text).tolist()

def generate_response(request):
    irrelevant_keywords = ['weather', 'news', 'sports', 'politics', 'finance']  # Add more keywords as needed
    if any(keyword in request.lower() for keyword in irrelevant_keywords):
        return "I'm sorry, I can only assist with travel-related questions. Please ask about travel destinations."
    chain = prompt_template | model | StrOutputParser()
    return chain.invoke({"request": request})

# Main function
def main():
    print("Welcome to the Domain-Specific Assistant!")
    print("Choose an option:")
    print("1. Generate embeddings with Cohere")
    print("2. Generate embeddings with Hugging Face")
    print("3. Ask a travel-related question")

    choice = input("Enter your choice (1/2/3): ")
    
    if choice == "1":
        text = input("Enter text to generate Cohere embeddings: ")
        embedding = get_cohere_embedding(text)
        print(f"Generated Cohere Embedding: {embedding[:10]}...")  
    elif choice == "2":
        text = input("Enter text to generate Hugging Face embeddings: ")
        embedding = get_hf_embedding(text)
        print(f"Generated Hugging Face Embedding: {embedding[:10]}...")  
    elif choice == "3":
        request = input("Enter a travel-related question: ")
        response = generate_response(request)
        print(f"Generated Response: {response}")
    else:
        print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
