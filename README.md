# Intelligent Egyptian Labor Law 2025 Query System 

Welcome to the **Intelligent Egyptian Labor Law 2025 Query System**!  
This project allows you to ask any question related to the **Egyptian Labor Law 2025** and get precise answers directly from the law text—no guessing, no external information.

---

##  Project Idea
The system uses **RAG (Retrieval-Augmented Generation)** to provide intelligent answers for legal questions.  
The workflow is as follows:

1. Load the Egyptian Labor Law PDF (2025).
2. Split the text into chunks while preserving legal context.
3. Convert each chunk into **Arabic embeddings** using the `paraphrase-multilingual-mpnet-base-v2` model.
4. Store embeddings in a **Vector Store** (Chroma).
5. Use a **LLM** (`ChatGroq`) to answer questions based only on the retrieved information.
6. Deliver answers accurately, concisely, and reference the relevant legal article when possible.

---

##  Project Structure

### 1 **processor.py**
- Loads the PDF and splits it into smaller chunks while preserving context.
- **Chunk size:** 600 tokens  
- **Overlap:** 120 tokens  

### 2 **engine.py**
- Connects **Embeddings**, **Vector Store**, and **LLM** to create the RAG chain.
- Uses a **custom prompt** to ensure accurate answers in Arabic.
- Embedding model: `sentence-transformers/paraphrase-multilingual-mpnet-base-v2`
- LLM model: `Llama-3.3-70B-Versatile`

### 3 **main.py**
- **FastAPI** backend to receive user questions and return answers.
- Endpoint: `/ask`
- Input: JSON with `"question"` field

### 4 **ui.py**
- **Streamlit** interactive UI
- Title: `"Intelligent Egyptian Labor Law 2025 Query System"`
- Lets users type questions and get answers from the server.

---

##  How to Run

1. **Install requirements**

```bash
pip install -r requirements.txt
2 - Start FastAPI server
uvicorn main:app --reload
3 - Run Streamlit UI
streamlit run ui.py
