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


# 📌 Testing the End Points

### **All the Api EndPoints in Swagger UI**

![Screenshot 2025-03-15 040024](https://github.com/user-attachments/assets/39f4ec3e-72ca-49c2-9938-35523e081adf)

### **Register the User**

![Screenshot 2025-03-15 040239](https://github.com/user-attachments/assets/1e54aa33-4c5f-4671-b702-fcaa14331e54)

### **Response the of Registered User**

![Screenshot 2025-03-15 040251](https://github.com/user-attachments/assets/a91674c2-29d0-415f-881f-27de75a293ff)

### **Login the User**

![Screenshot 2025-03-15 040449](https://github.com/user-attachments/assets/63401934-f748-4525-81d9-97671aa3a7df)

### **Response the of Login User**

![Screenshot 2025-03-15 040506](https://github.com/user-attachments/assets/a916b1fe-6002-481e-9d35-43babad7cdb7)

### **Get all the Projects**

![Screenshot 2025-03-15 040536](https://github.com/user-attachments/assets/4efdff73-c418-4a97-a24f-5221d78d22bd)


### **Create the Projects**

![Screenshot 2025-03-15 040625](https://github.com/user-attachments/assets/3c1aa457-db78-4ec8-b409-fd499b7be842)


### **Creating project without authenticated**


![Screenshot 2025-03-15 040723](https://github.com/user-attachments/assets/867830b0-7dea-4771-b6e9-c21b47fa5d6c)

### **After Authentication**

![Screenshot 2025-03-15 040648](https://github.com/user-attachments/assets/5d93d3d4-a8ec-4e95-ab44-1a7eebdecac3)

### **Project Created**


![Screenshot 2025-03-15 041146](https://github.com/user-attachments/assets/de782a84-1c4f-4b17-bda8-c22ec83cd7a2)
