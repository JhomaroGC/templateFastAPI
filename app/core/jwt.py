from datetime import timedelta, datetime
from jose import JWTError, jwt
from app.core.config import TRUNCATED_SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES


def create_access_token(data: dict):
    to_encode = data.copy()
    expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    expire = datetime.utcnow() + expires_delta
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, TRUNCATED_SECRET_KEY.encode("utf-8"), algorithm=ALGORITHM
    )
    return encoded_jwt


def decode_token(token: str):
    try:
        payload = jwt.decode(token, TRUNCATED_SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None
