# 🚀 FastAPI Mobile Search Backend 📱🔍

A FastAPI-based backend that uses **LangChain & Groq API** to fetch mobile phone recommendations based on company & price range. Returns details like 📸 camera, 🔋 battery, ⚡ processor & 💰 prices from different platforms.

## 🛠 Features
- ✅ Fetch mobile phone recommendations based on brand & budget
- ✅ Get details on camera, battery, processor & price
- ✅ FastAPI-powered backend with LangChain & Groq API
- ✅ Simple, fast & efficient API

## 📦 Installation

1️⃣ **Clone the repository**  
```bash
git clone https://github.com/yourusername/fastapi-mobile-search.git
cd fastapi-mobile-search
```

2️⃣ **Create & activate a virtual environment**  
```bash
python -m venv env
source env/bin/activate  # On Windows use `env\\Scripts\\activate`
```

3️⃣ **Install dependencies**  
```bash
pip install -r requirements.txt
```

## 🚀 Running the Server

```bash
uvicorn main:app --reload
```

Server will be running at: **http://127.0.0.1:8000/**

## 🔥 API Usage

### 🏠 Home Route
```http
GET /
```
📌 **Response:**
```json
"Backend working fine"
```

### 🔍 Search Mobile Phones
```http
GET /search?company=Samsung&price_range=20000-30000
```
📌 **Response Example:**
```json
{
  "fetched results": "Samsung Galaxy A54 - 📸 50MP, 🔋 5000mAh, ⚡ Exynos 1380, 💰 ₹26,999 (Amazon), ₹27,499 (Flipkart)"
}
```

## 🤝 Contributing
Pull requests are welcome! Feel free to improve the project. 😊

## 📜 License
This project is licensed under the **MIT License**.

---
Made with ❤️ by Abhishek 🚀

