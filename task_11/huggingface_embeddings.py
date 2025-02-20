from sentence_transformers import SentenceTransformer

# Load a pre-trained SentenceTransformer model
hf_model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')

#Define a function to generate embeddings
def get_hf_embedding(text):
    return hf_model.encode(text).tolist()  # Convert to list for compatibility

sample_text = "Explain transformer models."
embedding = get_hf_embedding(sample_text)
print(f"Embedding for '{sample_text}': {embedding[:15]}...")
