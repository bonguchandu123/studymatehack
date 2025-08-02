# 📚 StudyMate – AI-Powered PDF-Based Q&A System for Students

![StudyMate Banner](https://github.com/user-attachments/assets/1399b023-cbaf-43fc-9419-d77d69ee18f1)

**StudyMate** is an AI-powered academic assistant that allows students to upload their study PDFs and ask questions directly from the content. It's designed to simplify academic learning, boost revision, and help students understand complex topics in seconds.

---



## 🧠 Project Overview

Many students face difficulties in comprehending their academic PDFs, especially during last-minute preparations. StudyMate solves this by:

- Reading the uploaded PDF.
- Extracting and chunking its content.
- Generating vector embeddings using FAISS.
- Answering user questions using a Hugging Face-powered LLM.

---

## 🖼️ Authentication Flow

![Authentication Flow](https://github.com/user-attachments/assets/910276a3-9644-45ee-a428-c729008e51f2)

StudyMate uses a separate authentication backend for secure user management.

🔐 Authentication Repo: [studymateAuth](https://github.com/bonguchandu123/studymateAuth)  
🔧 Tech Stack: **FastAPI + MongoDB**

---

## 🛠️ Tech Stack

### 🔹 Frontend
- [Streamlit](https://streamlit.io/) – For interactive UI

### 🔹 Backend
- [FastAPI](https://fastapi.tiangolo.com/) – Authentication service
- [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) – For PDF text extraction
- [FAISS](https://github.com/facebookresearch/faiss) – For similarity search and vector embeddings
- [Hugging Face Transformers](https://huggingface.co/) – For Q&A model

### 🔹 Database
- [MongoDB](https://www.mongodb.com/) – User data and authentication

---

## 🧩 System Architecture

```text
[ User ] → [ Streamlit Frontend ] 
        → [ FastAPI Auth Server (studymateAuth) ] → MongoDB
        → [ PDF Upload & Extraction via PyMuPDF ]
        → [ Vector Embedding via FAISS ]
        → [ Q&A via HuggingFace ]
        → [ Streamlit Response UI ]
### # 📚 StudyMate – AI-Powered PDF-Based Q&A System for Students

![StudyMate Banner](https://github.com/user-attachments/assets/1399b023-cbaf-43fc-9419-d77d69ee18f1)

**StudyMate** is an AI-powered academic assistant that allows students to upload their study PDFs and ask questions directly from the content. It's designed to simplify academic learning, boost revision, and help students understand complex topics in seconds.

---




## 🧠 Project Overview

Many students face difficulties in comprehending their academic PDFs, especially during last-minute preparations. StudyMate solves this by:

- Reading the uploaded PDF.
- Extracting and chunking its content.
- Generating vector embeddings using FAISS.
- Answering user questions using a Hugging Face-powered LLM.

---

## 🖼️ Authentication Flow

![Authentication Flow](https://github.com/user-attachments/assets/910276a3-9644-45ee-a428-c729008e51f2)

StudyMate uses a separate authentication backend for secure user management.

🔐 Authentication Repo: [studymateAuth](https://github.com/bonguchandu123/studymateAuth)  
🔧 Tech Stack: **FastAPI + MongoDB**

---

## 🛠️ Tech Stack

### 🔹 Frontend
- [Streamlit](https://streamlit.io/) – For interactive UI

### 🔹 Backend
- [FastAPI](https://fastapi.tiangolo.com/) – Authentication service
- [PyMuPDF](https://pymupdf.readthedocs.io/en/latest/) – For PDF text extraction
- [FAISS](https://github.com/facebookresearch/faiss) – For similarity search and vector embeddings
- [Hugging Face Transformers](https://huggingface.co/) – For Q&A model

### 🔹 Database
- [MongoDB](https://www.mongodb.com/) – User data and authentication

---

## 🧩 System Architecture

```text
[ User ] → [ Streamlit Frontend ] 
        → [ FastAPI Auth Server (studymateAuth) ] → MongoDB
        → [ PDF Upload & Extraction via PyMuPDF ]
        → [ Vector Embedding via FAISS ]
        → [ Q&A via HuggingFace ]
        → [ Streamlit Response UI ]

### ✨ Features
✅ Secure login/signup system

✅ Upload any academic PDF

✅ Ask questions based on the uploaded document

✅ Intelligent answers powered by transformers

✅ Minimalist and responsive Ui

### 🧪 Example Use-Case
Login using your credentials (from FastAPI Auth server)

Upload your subject PDF (e.g., DBMS Notes.pdf)

Ask: "What is 2NF in normalization?"

Get an instant, relevant answer extracted from your document!

---

### 📁 Folder Structure
```
studymate/
├── app.py                        # Streamlit main app
├── utils/
│   ├── pdf_utils.py              # PDF extraction and chunking
│   └── retriever.py              # FAISS & Q&A logic
├── requirements.txt
└── README.md

https://github.com/bonguchandu123/studymateAuth

```
---
### 🔑 Authentication API Endpoints (From studymateAuth)

POST /register – Create a new user

POST /login – Login existing user

GET /me – Fetch user info

JWT-based authentication

MongoDB stores users securely
---

### 🎯 Target Audience
College & university students struggling with understanding large PDFs

Students preparing for exams needing quick and contextual revision

Anyone looking to use AI to make studying smarter and faster

### ⚠️ Known Challenges
Occasional backend crashes (handled with retries)

Long PDFs may impact performance (optimized chunking and embedding used)

Hugging Face Q&A models have input length limits
---

### 📸 UI Preview
✅ Clean Streamlit dashboard

✅ Interactive upload & chat window

✅ Real-time answers with references (if available)
---

### 🧪 Installation & Run Locally
```
# Clone UI & main logic
git clone https://github.com/YOUR_USERNAME/studymate.git
cd studymate

# Clone Auth backend separately
git clone https://github.com/bonguchandu123/studymateAuth.git
```

### 🔹 Backend Setup (studymateAuth)

```
cd studymateAuth
pip install -r requirements.txt
uvicorn main:app --reload
```

### 🔹 Frontend Setup (Streamlit)
```
cd studymate
pip install -r requirements.txt
streamlit run app.py
```

### 🧪 Demo Credentials (for testing)
✨ Add sample login credentials here if available, or use Auth API to register.
---

### 👥 Team CDN
B. Chandu

K.S.S. Dinesh

B. Nithin

### 📌 Final Deliverables
✅ Hackathon Project Report

✅ Demo Video (link soon)

✅ GitHub Repositories

✅ Live Presentation

[Auth](https://github.com/bonguchandu123/studymateAuth)



