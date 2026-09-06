import os
from dotenv import load_dotenv
import requests
import os
from openai import OpenAI
from sentence_transformers import SentenceTransformer

load_dotenv()
api_key = os.getenv("Deep_Seek_API_KEY")

def embedding(sentences: str):
    model = SentenceTransformer("./local-all-MiniLM-L6-v2")

    # Define texts to embed
    sentences = [
        "This is an example sentence",
        "Each sentence is converted into a vector",
        "Hello world from Python"
    ]

    # Generate embeddings
    embeddings = model.encode(sentences)

    # Print results
    print(f"Embedding shape: {embeddings.shape}")  # Output: (3, 384)
    print(f"First vector (truncated): {embeddings[0][:5]}...")
    return embeddings

def response(api: str):
    client = OpenAI(
            api_key=api,
            base_url="https://api.deepseek.com")

    response = client.chat.completions.create(
        model="deepseek-v4-flash",
        messages=[
            {"role": "system", "content": "You are a helpful assistant"},
            {"role": "user", "content": "Hello, write haiku about random things"},
        ],
        stream=False,
        reasoning_effort="low",
        extra_body={"thinking": {"type": "disabled"}}
    )


    if response == 200:
        print(response.choices)
        
    else:
        #data = response.json()
        print(response)

def conversation_agent():
    return "s"
    



if __name__ == "__main__":
    
    print ("hello, {}", api_key)
    