from langchain_huggingface import HuggingFaceEmbeddings
from pinecone import Pinecone, ServerlessSpec
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_pinecone import PineconeVectorStore
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
import os

# Load environment variables
load_dotenv()

# Initialize the Hugging Face embedding model
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-mpnet-base-v2")
print("Hugging Face Embedding Model Loaded.")

# Set Pinecone API Key
pinecone_api_key = os.getenv("PINECONE_API_KEY")

# Define document loader
def read_doc(directory):
    file_loader = PyPDFDirectoryLoader(directory)
    documents = file_loader.load()
    return documents

# Load documents
doc_directory = "documents/"  # Replace with your directory
docs = read_doc(doc_directory)
print(f"{len(docs)} documents loaded.")

# Split documents into chunks
def chunk_data(docs, chunk_size=800, chunk_overlap=50):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
    chunks = text_splitter.split_documents(docs)
    for chunk in chunks:
        chunk.metadata["source"] = chunk.metadata.get("source", "Unknown")  # Add or retain metadata
    return chunks

documents = chunk_data(docs)
print(f"Documents split into {len(documents)} chunks.")

# Initialize Pinecone client
pc = Pinecone(api_key=pinecone_api_key)
print("Pinecone Client Initialized.")

# Create or connect to Pinecone index
index_name = "vector-index"  # Change the index name if needed
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=768,  # Embedding dimension of all-mpnet-base-v2
        metric="cosine",
        spec=ServerlessSpec(cloud='aws', region='us-east-1')
    )
print(f"Pinecone index '{index_name}' is ready.")

index = pc.Index(index_name)

# Upload documents to Pinecone as vectors
vector_store = PineconeVectorStore.from_documents(
    documents=documents,
    embedding=embeddings,
    index_name=index_name
)
print("Documents uploaded to Pinecone.")

# Initialize LLM (e.g., GPT-4 via OpenAI API)
# Initialize ChatOpenAI LLM
llm = ChatOpenAI(model="gpt-4", temperature=0.0)

# Initialize conversation memory
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# Set up the conversational retrieval chain
retrieval_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    retriever=vector_store.as_retriever(),  # Use Pinecone vector store
    memory=memory
)
print("Conversational Retrieval Chain with Memory is Ready.")

# Start a multi-turn conversation
query1 = "What is the purpose of the Power BI REST API?"
response1 = retrieval_chain.invoke({"question": query1})
print("Response 1:", response1["answer"])

query2 = "Can you give me an example of its usage?"
response2 = retrieval_chain.invoke({"question": query2})
print("Response 2:", response2["answer"])
