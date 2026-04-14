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



## 🧪 Samples for Testing

Below are some sample inputs and expected outputs to test the system:

---

### Input:
What is Python?

### Output:
Python is a high-level programming language used for backend development, data science, and automation.

---

### Input:
What is Java?

### Output:
Java is an object-oriented programming language widely used for building applications.

---

### Input:
Explain Artificial Intelligence

### Output:
Artificial Intelligence enables machines to simulate human intelligence and perform tasks like learning and decision-making.

---

### Input:
What is Data Structures?

### Output:
Data structures organize and store data efficiently for processing and retrieval.

---

### Input:
What is Operating System?

### Output:
An operating system manages computer hardware and software resources and provides services for applications.
