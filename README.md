# CRUD Using FastAPI with MongoDB

## 📌 Project Description
This project is a **CRUD (Create, Read, Update, Delete) API** built using **FastAPI** and **MongoDB**.  
It allows users to perform basic database operations using REST API endpoints.

## 🚀 Features
- Create new data records  
- Read data from database  
- Update existing records  
- Delete records  
- Fast and modern backend using FastAPI  
- MongoDB database integration  
- Environment variable security using `.env`

- 
## 🛠️ Technologies Used
- Python  
- FastAPI  
- MongoDB  
- Motor (Async MongoDB Driver)  
- Pydantic  
- Uvicorn  
- dotenv


## 📦 Installation

### Clone Repository
```bash
git clone YOUR_REPOSITORY_LINK
cd fastapi-mongo-crud
### Create Virtual Environment
python -m venv venv
venv\Scripts\activate

### Install Dependencies
pip install -r requirements.txt

### 🔑 Environment Variables
Create a .env file and add:
MONGO_URL=your_mongodb_connection_string

### ▶️ Run Project

Start FastAPI server:
uvicorn main:app --reload

# 📂 Project Structure
fastapi-mongo-crud/
│
├── main.py
├── database.py
├── requirements.txt
├── .gitignore
├── .env
└── venv/


#👨‍💻 Author

Shoaib Ahmed


#📜 License

This project is for learning and educational purposes.


⭐ If you like this project, please give a star on GitHub.
