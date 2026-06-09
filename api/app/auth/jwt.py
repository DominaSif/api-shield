from datetime import datetime, timedelta
from jose import jwt, JWTError
from app.config import settings

def create_token(user_id: int) -> str:
    payload = {
        "user_id": user_id,
        "exp": datetime.utcnow() + timedelta(minutes=settings.jwt_expire_minutes)
    }
    return jwt.encode(payload, settings.secret_key, algorithm=settings.jwt_algorithm)

def verify_token(token: str) -> int:
    try:
        payload = jwt.decode(token, settings.secret_key, algorithms=[settings.jwt_algorithm])
        return payload["user_id"]
    except JWTError:
        return None
