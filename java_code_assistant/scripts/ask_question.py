import chromadb
from sentence_transformers import SentenceTransformer
from transformers import pipeline
from huggingface_hub import login

# ✅ Global Variables (for reuse)
embedding_model = None
chroma_client = None
collection = None
deepseek_generator = None

def initialize_models():
    """Initialize the embedding model, ChromaDB, and DeepSeek AI."""
    global embedding_model, chroma_client, collection, deepseek_generator

    print("\n🔹 Logging into Hugging Face API...")
    login("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")  # Use your actual HF token
    print("✅ Successfully authenticated with Hugging Face.")

    print("\n🔹 Loading embedding model and connecting to ChromaDB...")
    embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
    chroma_client = chromadb.PersistentClient(path="../chroma_db")
    collection = chroma_client.get_collection(name="airline_reservation_system")
    print("✅ Embedding model and ChromaDB loaded successfully.")

    print("\n🚀 Loading DeepSeek AI model...")
    deepseek_generator = pipeline(
        "text-generation",
        model="deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B",
        trust_remote_code=True
    )
    print("✅ DeepSeek AI model loaded successfully.")

def retrieve_answer_from_chromadb(query_text):
    """Fetch the best-matching answer from ChromaDB."""
    query_embedding = embedding_model.encode(query_text).tolist()
    results = collection.query(query_embeddings=[query_embedding], n_results=1)

    if not results["metadatas"] or len(results["metadatas"][0]) == 0:
        return "⚠️ No relevant answer found in ChromaDB."
    else:
        return results["metadatas"][0][0].get("answer", "⚠️ No answer available")

def enhance_with_deepseek(answer):
    """Improve answer clarity and completeness using DeepSeek AI."""
    print("\n🚀 Enhancing answer with DeepSeek AI...")
    prompt = f"Detailed Explanation answer:\n{answer}"

    refined_answer = deepseek_generator(
        prompt, max_length=2000, do_sample=True, truncation=True
    )

    if refined_answer and isinstance(refined_answer, list) and "generated_text" in refined_answer[0]:
        final_answer = refined_answer[0]["generated_text"].strip()
        return final_answer.split("</think>")[-1].strip()  # Clean unwanted output
    else:
        return "⚠️ DeepSeek did not return a valid response. Showing original answer."

def main():
    """Interactive Q&A loop until user types 'exit'."""
    try:
        initialize_models()  # ✅ Load everything once at startup

        while True:
            user_query = input("\n💬 Ask a question (or type 'exit' to quit): ").strip()
            if user_query.lower() == "exit":
                print("👋 Exiting the program. Have a great day!")
                break

            print(f"\n🔍 Searching for: '{user_query}'")
            retrieved_answer = retrieve_answer_from_chromadb(user_query)

            print("\n✅ Answer from ChromaDB:")
            print("--------")
            print(retrieved_answer)

            # Enhance with DeepSeek only if ChromaDB's answer is generic or missing
            final_answer = enhance_with_deepseek(retrieved_answer)
            print("\n✅ Final Enhanced Answer:")
            print("--------")
            print(final_answer)

    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()




