from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from app.database import engine
from app.models.models import User
from app.models.schemas import UserCreate, Token
from app.security.auth import get_password_hash, verify_password, create_access_token
from fastapi.security import OAuth2PasswordRequestForm

router = APIRouter()

@router.post("/register")
def register(user: UserCreate):
    with Session(engine) as session:
        # Make sure we're checking the "users" table
        existing_user = session.exec(select(User).where(User.username == user.username)).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="Username already taken")
        
        hashed_password = get_password_hash(user.password)
        new_user = User(username=user.username, hashed_password=hashed_password, role=user.role)
        session.add(new_user)
        session.commit()
        session.refresh(new_user)  # Ensure the data is saved
        print(f"✅ User '{new_user.username}' registered successfully!")

    return {"message": "User registered successfully","user":new_user}

@router.post("/login", response_model=Token)
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    with Session(engine) as session:
        user = session.exec(select(User).where(User.username == form_data.username)).first()
        if not user or not verify_password(form_data.password, user.hashed_password):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

        access_token = create_access_token(data={"sub": user.username, "role": user.role})
        return {"access_token": access_token, "token_type": "bearer"}