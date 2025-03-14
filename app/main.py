from fastapi import FastAPI
from app.database import create_db_and_tables
from app.routes import user_routes, project_routes

app = FastAPI(title="FastAPI JWT Authentication with RBAC")

# Initialize database tables
create_db_and_tables()

# Include routers
app.include_router(user_routes.router, prefix="/users", tags=["Users"])
app.include_router(project_routes.router, prefix="/projects", tags=["Projects"])

@app.get("/")
def home():
    return {"message": "Welcome to the FastAPI JWT Auth API"}
