# 🤖 PolicyPilot AI

An AI-powered HR Assistant that helps employees instantly find answers to HR-related questions using company policy documents. Built with Retrieval-Augmented Generation (RAG), the assistant retrieves relevant information from HR documents and generates context-aware responses using Groq's Llama model.

---

## 🚀 Features

- 📄 Answers questions based on HR policy documents
- 🔍 Semantic search using Pinecone Vector Database
- 🧠 Gemini Embeddings for accurate document retrieval
- ⚡ Groq Llama 3.3 for fast response generation
- 💬 Interactive Streamlit chat interface
- 🚫 Prevents hallucinations by answering only from retrieved HR documents
- 👋 Handles greetings while restricting unrelated queries

---

## 🛠 Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| Streamlit | User Interface |
| Groq (Llama 3.3) | Large Language Model |
| Gemini Embeddings | Text Embeddings |
| Pinecone | Vector Database |
| PyPDF | PDF Processing |
| python-dotenv | Environment Variable Management |

---

## 🏗 Architecture

```
                 HR Documents
                      │
                      ▼
               Text Extraction
                      │
                      ▼
                  Chunking
                      │
                      ▼
             Gemini Embeddings
                      │
                      ▼
              Pinecone Vector DB
                      │
          User HR Query
                      │
                      ▼
             Query Embedding
                      │
                      ▼
         Semantic Search (Top-K)
                      │
                      ▼
           Retrieved HR Context
                      │
                      ▼
           Groq Llama 3.3 Model
                      │
                      ▼
             Grounded Response
```

---

## 📂 Project Structure

```
PolicyPilot-AI/
│
├── app.py                 # Streamlit Interface
├── QueryProcessor.py      # Query Pipeline
├── llm.py                 # Groq LLM Integration
├── embedder.py            # Gemini Embeddings
├── vectorstore.py         # Pinecone Operations
├── dataprocessor.py       # PDF Processing & Indexing
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Installation

### Clone the repository

```bash
git clone https://github.com/your-username/PolicyPilot-AI.git
cd PolicyPilot-AI
```

### Create a virtual environment

```bash
python -m venv venv
```

Activate it:

Windows

```bash
venv\Scripts\activate
```

Mac/Linux

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_groq_api_key
GEMINI_API_KEY=your_gemini_api_key
PINECONE_API_KEY=your_pinecone_api_key
PINECONE_INDEX_NAME=your_index_name
```

---

## 📑 Index HR Documents

Place your HR policy PDFs in the project directory and run:

```bash
python dataprocessor.py
```

This will:

- Extract text from PDFs
- Split text into chunks
- Generate embeddings
- Store vectors in Pinecone

---

## ▶️ Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 💡 Example Questions

- What is the leave policy?
- How many casual leaves are available?
- Explain the attendance policy.
- What are the employee benefits?
- What is the resignation process?
- Describe the probation period.

---

## 🎯 Why RAG?

Instead of relying solely on a language model's training data, PolicyPilot AI retrieves relevant information from company HR documents before generating a response. This ensures:

- Accurate answers
- Reduced hallucinations
- Context-aware responses
- Better reliability for enterprise use cases

---

## 🔮 Future Enhancements

- Upload HR documents directly from the UI
- Source citations with document names
- Multi-document support
- Conversation history
- Role-based HR assistants
- Deployment on Streamlit Cloud

---

## 👩‍💻 Author

**R Deeksha**

Passionate about AI, Generative AI, and building practical LLM-powered applications.

---

⭐ If you found this project interesting, consider giving it a star!
