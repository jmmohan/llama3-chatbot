# LLaMA 3 Chatbot - Generate User Stories

This is a simple chatbot that takes an **epic** as input and generates detailed **user stories** using the LLaMA 3 model.

## 🚀 Features
- Uses **FastAPI** to create an API.
- Uses **Ollama** to run the LLaMA 3 model.
- Returns structured **user stories** from a given epic.

## 🛠 Prerequisites
Ensure you have the following installed:
1. Python (>= 3.10)
2. Ollama (for running LLaMA 3) → Install from [https://ollama.com](https://ollama.com)
3. FastAPI & Uvicorn → Install with:
   
   pip install -r requirements.txt

## How to Run

python -m uvicorn app:app --host 127.0.0.1 --port 8000