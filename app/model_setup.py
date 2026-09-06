from sentence_transformers import SentenceTransformer

# Download from Hugging Face hub
model = SentenceTransformer("sentence-transformers/all-MiniLM-L6-v2")

# Save it to a specific local directory
model.save("./local-all-MiniLM-L6-v2")