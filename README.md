# 📰 AI News Research Tool

An end-to-end Retrieval-Augmented Generation (RAG) application that enables users to ask natural language questions about online news articles and receive AI-generated answers with source attribution.

The application ingests news articles from URLs, creates semantic embeddings, stores them in a FAISS vector database, retrieves the most relevant content based on user queries, and generates contextual answers using OpenAI's language models.

---

## 🚀 Features

- 🔗 Load multiple news articles from URLs
- ✂️ Automatic document chunking
- 🧠 OpenAI Embeddings for semantic search
- 📚 FAISS vector database for fast retrieval
- 🤖 AI-powered question answering using GPT
- ⚡ Streaming responses (token-by-token)
- 📄 Source attribution with clickable article links
- 🎯 Retrieval-Augmented Generation (RAG) architecture

---

## 🏗️ Architecture

```
                 Ingestion Pipeline

          News URLs
               │
               ▼
      UnstructuredURLLoader
               │
               ▼
   RecursiveCharacterTextSplitter
               │
               ▼
      OpenAI Embeddings
               │
               ▼
        FAISS Vector Store
               │
               ▼
         Save Index to Disk


               Query Pipeline

         User Question
               │
               ▼
      Load FAISS Index
               │
               ▼
       Semantic Similarity Search
               │
               ▼
     Retrieve Relevant Chunks
               │
               ▼
        Prompt Construction
               │
               ▼
      OpenAI GPT-4.1 Mini
               │
               ▼
      Streaming AI Response
               │
               ▼
      Answer + Source Links
```

---

## 🛠️ Tech Stack

- Python 3.11
- Streamlit
- LangChain
- OpenAI API
- OpenAI Embeddings
- FAISS
- python-dotenv

---

## 📷 Screenshots

### <img width="1909" height="873" alt="image" src="https://github.com/user-attachments/assets/d31188f3-91fc-4407-b563-1e72794df2fd" />


_Add screenshot here_

### AI Response

_Add screenshot here_

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/Sajjad-Sohail/AIBot-NewsResearchTool.git
cd AIBot-NewsResearchTool
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate the environment

Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```text
OPENAI_API_KEY=your_openai_api_key
```

Run the application

```bash
streamlit run main.py
```

---

## 💡 How It Works

1. Enter one or more news article URLs.
2. Click **Process URLs**.
3. Articles are downloaded and split into smaller chunks.
4. Each chunk is converted into vector embeddings.
5. Embeddings are stored inside a FAISS vector database.
6. Ask questions in natural language.
7. The application retrieves the most relevant document chunks.
8. GPT generates an answer using only the retrieved context.
9. Sources are displayed alongside the answer.

---

## 📂 Project Structure

```
AIBot-NewsResearchTool/
│
├── main.py
├── requirements.txt
├── .gitignore
├── README.md
└── .env.example
```

---

## 🔮 Future Improvements

- PDF document support
- Conversation memory
- Multi-document chat
- Citation highlighting
- Vector database persistence
- ChromaDB integration
- Local LLM support (Ollama)
- Multi-user authentication
- Chat history
- Docker deployment

---

## 📚 AI Concepts Demonstrated

- Retrieval-Augmented Generation (RAG)
- Semantic Search
- Vector Embeddings
- Vector Databases
- Document Chunking
- Prompt Engineering
- Streaming LLM Responses
- Source Attribution

---

## 👨‍💻 Author

**Sajjad Sohail**

Software Engineer | AI Enthusiast

GitHub: https://github.com/Sajjad-Sohail

---

## ⭐ If you found this project useful, consider giving it a star!
