# 🤖 Persona-Adaptive Customer Support Agent

## AI Engineering Internship Assignment

### Overview

The **Persona-Adaptive Customer Support Agent** is an AI-powered support system that automatically detects a customer's communication style, retrieves relevant information from a knowledge base using Retrieval-Augmented Generation (RAG), generates persona-specific responses, and escalates unresolved issues to a human support agent.

This project demonstrates practical applications of Large Language Models (LLMs), Retrieval-Augmented Generation (RAG), Vector Databases, Persona Detection, and Human-in-the-Loop AI systems.

---
# Features

* Customer Persona Detection
* Retrieval-Augmented Generation (RAG)
* ChromaDB Vector Database
* Sentence Transformer Embeddings
* PDF Knowledge Base
* Persona-Based Response Generation
* Automatic Escalation
* Streamlit User Interface

---

# Supported Personas

### Technical Expert

Characteristics

* Technical terminology
* APIs
* Configuration
* Logs
* Debugging

Response Style

* Detailed
* Technical
* Step-by-step troubleshooting

---

### Frustrated User

Characteristics

* Emotional language
* Urgent requests
* Complaints

Response Style

* Empathetic
* Reassuring
* Simple language

---

### Business Executive

Characteristics

* Business impact
* Timeline
* ROI
* Concise communication

Response Style

* Short
* Professional
* Business focused

---

# Project Architecture

```
                User Query
                     │
                     ▼
            Persona Detection
                     │
                     ▼
          Knowledge Base Search
              (RAG Pipeline)
                     │
                     ▼
        ChromaDB Vector Database
                     │
                     ▼
        Relevant Document Chunks
                     │
                     ▼
     Persona Adaptive Response Generator
                     │
                     ▼
          Escalation Decision
                     │
        ┌────────────┴────────────┐
        ▼                         ▼
AI Generated Response     Human Support Handoff
```

---

# Project Structure

```
persona-support-agent/

│── app.py
│── README.md
│── requirements.txt
│── .env

│── test_rag.py
│── test_classifier.py
│── test_generation.py
│── test_escalator.py

├── data/
│   ├── password_reset_guide.pdf
│   ├── billing_policy.md
│   ├── login_troubleshooting.md
│   ├── refund_policy.md
│   ├── api_authentication.md
│   └── ...

├── chroma_db/

└── src/
    ├── config.py
    ├── rag_pipeline.py
    ├── classifier.py
    ├── generation.py
    ├── escalator.py
```

---

# Technology Stack

| Technology            | Purpose               |
| --------------------- | --------------------- |
| Python                | Backend               |
| Streamlit             | User Interface        |
| LangChain             | Document Processing   |
| ChromaDB              | Vector Database       |
| Sentence Transformers | Embedding Model       |
| PyPDF                 | PDF Loading           |
| python-dotenv         | Environment Variables |

---

# RAG Pipeline

1. Load Support Documents
2. Read PDF / Markdown / Text files
3. Split into chunks
4. Generate embeddings
5. Store embeddings in ChromaDB
6. Perform similarity search
7. Retrieve top matching documents

---

# Persona Detection Strategy

The classifier identifies one of three customer personas:

* Technical Expert
* Frustrated User
* Business Executive

The detected persona determines the tone and style of the generated response.

---

# Response Generation

Responses are adapted according to the detected persona.

Technical Expert

* Detailed explanation
* Root cause
* Technical guidance

Frustrated User

* Empathetic
* Action-oriented
* Reassuring

Business Executive

* Concise
* Business impact
* Resolution summary

---

# Escalation Logic

The system escalates support requests when:

* No relevant document is retrieved
* The customer is highly frustrated
* The issue cannot be resolved automatically

During escalation the system generates a structured support handoff.

---

# Installation

Clone the repository

```bash
git clone https://github.com/yourusername/persona-support-agent.git
```

Navigate into the project

```bash
cd persona-support-agent
```

Create virtual environment

```bash
python -m venv venv
```

Activate

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create a `.env` file

```
GEMINI_API_KEY=YOUR_API_KEY
```

---

# Run Application

```bash
streamlit run app.py
```

---

# Example Queries

### Password Reset

```
How do I reset my password?
```

---

### Technical Expert

```
Our API keeps returning HTTP 401 Unauthorized.
```

---

### Frustrated User

```
Nothing works! I'm really frustrated.
```

---

### Business Executive

```
How will this issue affect business operations?
```

---

### Login Issue

```
I didn't receive my password reset email.
```

---

# Sample Output

```
Detected Persona

Technical Expert

Retrieved Source

password_reset_guide.pdf

Response

Detailed technical troubleshooting steps...

Escalation

Not Required
```

---

# Future Improvements

* Multi-turn conversation memory
* LLM-based persona detection
* Confidence scoring
* Sentiment analysis
* Dashboard analytics
* Human approval workflow
* Email integration
* Ticket generation

---

# Known Limitations

* Small knowledge base
* Rule-based persona classification
* Basic escalation logic
* Single-session conversations

---

# Author

**Santosh Buddhivant Tambe**

AI Engineering Internship Assignment

2026
