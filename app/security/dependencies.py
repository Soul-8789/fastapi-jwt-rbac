from fastapi import Depends, HTTPException
from sqlmodel import Session, select
from app.database import engine
from app.security.auth import decode_access_token, oauth2_scheme
from app.models.models import User

# Get Current User
def get_current_user(token: str = Depends(oauth2_scheme)):
    payload = decode_access_token(token)
    username: str = payload.get("sub")
    role: str = payload.get("role")

    with Session(engine) as session:
        user = session.exec(select(User).where(User.username == username)).first()
        if not user:
            raise HTTPException(status_code=401, detail="User not found")
        return user

# Role-Based Dependency
def require_role(required_role: str):
    def role_dependency(user: User = Depends(get_current_user)):
        if user.role != required_role:
            raise HTTPException(status_code=403, detail="Access forbidden: Insufficient permissions")
        return user
    return role_dependency
