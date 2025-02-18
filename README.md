# AI-code-assistant
This is CromaDB and DeepSeek-R1-Distill-Qwen-1.5B based code assistant for my Collage Java project (Airline Reservation System)

# AI Code Assistant - Q&A System

## Overview
This project is a **Q&A system** built using **ChromaDB**, **Sentence Transformers**, and **DeepSeek AI**. It allows you to index a dataset of questions and answers into a vector database and retrieve the most relevant answer using semantic search.

## Features
- ✅ **Embeds and stores questions & answers** using **ChromaDB** and **Sentence Transformers**.
- ✅ **Retrieves answers** based on query similarity.
- ✅ **Enhances answers** using **DeepSeek AI** for clarity and completeness.
- ✅ **Interactive CLI** where users can ask questions dynamically.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/AI-code-assistant.git
cd AI-code-assistant
```

### 2. Install Dependencies
Ensure you have Python 3.8+ installed. Install required libraries:
```bash
pip install -r scripts/requirements.txt
```

### 3. Prepare the Dataset
Place your dataset in `outputs/dataset.json`. Example format:
```json
[
    {
        "question": "What is an API?",
        "answer": "An API (Application Programming Interface) is a set of rules..."
    }
]
```

### 4. Load Data into ChromaDB
Run the script to load questions into ChromaDB:
```bash
python misc/load_data.py
```

### 5. Ask Questions
Run the interactive Q&A system:
```bash
python misc/ask_question.py
```

## Project Structure
```
AI-code-assistant/
│── java_code_assistant/
│   ├── chroma_db/  # Stores ChromaDB persistent data
│   ├── misc/  # Utility scripts
│   ├── outputs/  # Stores dataset and metadata
│   ├── Project/  # Java project files
│   ├── scripts/
|   |   ├── load_data.py  # Loads dataset into ChromaDB
|   |   ├── ask_question.py  # Handles user Q&A
│── README.md  # Documentation
│── .gitignore  # Ignore unnecessary files
```

## Use of ChromaDB and DeepSeek AI

### [ChromaDB](https://www.datacamp.com/tutorial/chromadb-tutorial-step-by-step-guide)
ChromaDB is used as a **vector database** to store and retrieve question-answer embeddings efficiently. When a question is asked, its embedding is compared against stored embeddings to find the closest match. This allows for **semantic search** rather than simple keyword matching, ensuring more relevant results.

### DeepSeek AI
DeepSeek AI is integrated to **enhance and refine answers** retrieved from ChromaDB. If a retrieved answer is too generic or incomplete, DeepSeek AI generates a more detailed and contextually rich response, improving the quality of answers provided to users.

## Use of Sentence Transformer - [all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
The **all-MiniLM-L6-v2** model from **Sentence Transformers** is a lightweight yet powerful model for generating text embeddings. It is used in this project to convert questions into high-dimensional vectors, enabling effective similarity searches in ChromaDB.

### Key Features of all-MiniLM-L6-v2:
- **Compact & Fast**: Optimized for performance with 6 transformer layers.
- **High Accuracy**: Provides strong semantic representations despite being lightweight.
- **Useful for Question-Answering**: Ideal for embedding-based retrieval tasks like this project.

## How It Works
1. **Data Ingestion** (`load_data.py`)
   - Loads questions from `dataset.json`.
   - Generates embeddings using `all-MiniLM-L6-v2`.
   - Stores question-answer pairs in **ChromaDB**.

2. **Question Answering** (`ask_question.py`)
   - Takes user input and encodes it.
   - Find's the best-matching answer from **ChromaDB**.
   - Uses **DeepSeek AI** to enhance the response.

## Future Improvements
- 🔹 Add support for multiple datasets.
- 🔹 Implement web-based UI.
- 🔹 Improve response generation with advanced LLMs.

## Contributing
Feel free to submit issues and PRs! 🚀


