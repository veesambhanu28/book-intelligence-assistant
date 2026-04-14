# book-intelligence-assistant
# 📚 Book Intelligence Assistant

## 🚀 Overview
This is a RAG-based Book Intelligence Assistant that answers user queries using structured book data.

---

## ✨ Features
- Chat-based system
- Book data retrieval
- Response caching
- Clean UI

---

## ⚙️ Setup Instructions
1. Clone the repo  
2. pip install -r requirements.txt  
3. python manage.py runserver  
4. Open http://127.0.0.1:8000/

---

## 🔗 API Documentation

### GET /api/books/
Returns all books

### POST /api/ask/
Request:
{
  "question": "What is Python?"
}

Response:
{
  "answer": "Python is a high-level programming language..."
}

---

## 💡 Sample Questions
- What is Python?
- What is Java?
- Explain AI

---

## 🧪 Sample Output
Q: What is Python?  
A: Python is a high-level programming language...

---

## 📸 Screenshots
(Add 3–4 screenshots here)

---

## 🧠 Approach
Uses Retrieval-Augmented Generation (RAG) to fetch answers from stored book data.
