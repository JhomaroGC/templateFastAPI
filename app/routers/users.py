from fastapi import APIRouter, HTTPException, Depends
from app.models.user import UserCreate, UserLogin
from app.core.security import hash_password, verify_password
from app.core.jwt import create_access_token
from app.core.dependencies import oauth2_scheme
from app.core.jwt import decode_token


router = APIRouter()
FAKE_BD = []


@router.post("/register")
def create_user(user: UserCreate):
    """Create a new user. With hashed password."""
    hashed_password = hash_password(user.password)
    FAKE_BD.append({"email": user.email, "password": hashed_password})
    return {"status": "User created", "user": user.email}


@router.post("/login")
def login(user: UserLogin):
    """Login a user."""
    found_user = next(
        (db_user for db_user in FAKE_BD if db_user["email"] == user.email), None
    )
    if not found_user or not verify_password(user.password, found_user["password"]):
        raise HTTPException(status_code=401, detail="Credentials are incorrect")
    return {
        "access_token": create_access_token({"sub": user.email}),
        "token_type": "bearer",
    }


@router.get("/me")
def read_users_me(token: str = Depends(oauth2_scheme)):
    """Get the current user."""
    # decodificar el token para obtener el email
    payload = decode_token(token)
    if not payload:
        raise HTTPException(
            status_code=401,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    email = payload.get("sub")
    # buscar usuario en la FakeBD
    found_user = next(
        (db_user for db_user in FAKE_BD if db_user["email"] == email), None
    )
    if not found_user:
        raise HTTPException(status_code=401, detail="User not found")
    return {"email": email, "status": "User authenticated"}
