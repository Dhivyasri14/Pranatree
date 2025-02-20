import cohere
import os
from dotenv import load_dotenv

load_dotenv()
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

#Initializes a Cohere client instance using the API key
cohere_client = cohere.Client(COHERE_API_KEY)

def get_cohere_embedding(text):
    response = cohere_client.embed(
        texts=[text],
        model="large"  # Use the appropriate model
    )
    return response.embeddings[0] 


sample_text = "What are embeddings?"
embedding = get_cohere_embedding(sample_text)
print(f"Embedding for '{sample_text}': {embedding}...")  
