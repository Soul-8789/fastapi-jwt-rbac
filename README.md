# 🚀 FastAPI JWT RBAC Authentication System
A **FastAPI-based REST API** with **JWT authentication** and **role-based access control (RBAC)** using PostgreSQL and SQLModel.


## 📌 **Features**
- ✔ **User Registration & Login** using JWT (JSON Web Token)  
- ✔ **Role-Based Access Control (RBAC)**  
- ✔ **Secure Password Hashing** using `bcrypt`  
- ✔ **PostgreSQL Database** for data storage  
- ✔ **FastAPI + SQLModel ORM** for efficient database handling  
- ✔ **Swagger API Documentation**  

## **🛠️ Tech Stack**
- **FastAPI** 🚀 (Python-based web framework)
- **PostgreSQL** 🗄️ (Relational Database)
- **SQLModel (ORM)** 🔗 (Database interactions)
- **JWT Authentication** 🔑 (Secure token-based authentication)
- **bcrypt** 🔐 (For password hashing)
- **Uvicorn** ⚡ (ASGI server)


## **📌 Installation Guide**

### **1️⃣ Clone the Repository**

```sh 
https://github.com/Soul-8789/fastapi-jwt-rbac.git
cd fastapi-jwt-rbac
```

### **2️⃣ Create a Virtual Environment**

```sh
Copy code
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
```
### **3️⃣ Install Dependencies**

```sh
pip install -r requirements.txt
```

## **📌 Database Setup**


### **1️⃣ Install PostgreSQL**

Make sure PostgreSQL is installed and running.

### **2️⃣ Create a Database**

```sql

CREATE DATABASE test_db;

```
### **3️⃣ Update .env file**

Create a .env file and update the DATABASE_URL:


```ini
DATABASE_URL=postgresql://postgres:yourpassword@localhost:5432/test_db
SECRET_KEY=your_secret_key

```

# 📌 Running the Application

```sh
uvicorn app.main:app --reload
```

✅ API is now running at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

# 📄 Open API Documentation

Access the interactive API documentation at:

- **Swagger UI**: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)


# 📌 API Endpoints

## 🔹 User Authentication
| Method | Endpoint        | Description            |
|--------|---------------|------------------------|
| POST   | /users/register | Register a new user   |
| POST   | /users/login   | Login and get JWT token |

## 🔹 Projects (RBAC Controlled)
| Method | Endpoint  | Role  | Description       |
|--------|----------|-------|-------------------|
| GET    | /projects | user / admin | Get all projects  |
| POST   | /projects | admin | Create a project |
