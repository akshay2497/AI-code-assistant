import json
from sentence_transformers import SentenceTransformer
import chromadb

print("✅ Script started...")

# Load dataset
try:
    with open("../outputs/dataset.json", "r") as file: # add your dataset path here
        questions_data = json.load(file)
    print(f"✅ Loaded {len(questions_data)} questions from JSON.")  # Fix: Properly format count
except Exception as e:
    print(f"❌ Error loading JSON: {e}")

# Initialize embedding model
try:
    embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
    print(f"✅ Embedding model loaded successfully.")
except Exception as e:
    print(f"❌ Error loading embedding model: {e}")

# Initialize ChromaDB
try:
    chroma_client = chromadb.PersistentClient(path="../chroma_db")
    collection = chroma_client.get_or_create_collection(name="airline_reservation_system")
    print("✅ ChromaDB initialized.")
except Exception as e:
    print(f"❌ Error initializing ChromaDB: {e}")

# Convert questions to embeddings
i = 0
for item in questions_data:  # Process first 5 for testing
    try:
        question_text = item["question"]
        vector = embedding_model.encode(question_text).tolist()

        collection.add(
            ids=[str(i)],  # Unique ID based on question_number
            embeddings=[vector],
            metadatas=[
                {
                    "question": item["question"],
                    "answer": item["answer"]
                }
            ]
        )

        print(f"✅ Indexed question {i+1}: {question_text[:50]}...")
        i += 1
    except Exception as e:
        print(f"❌ Error processing question {i+1}: {e}")
        i += 1

print("✅ Questions indexed successfully in ChromaDB!")