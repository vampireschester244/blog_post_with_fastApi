from email import header
from fastapi import HTTPException, status
from jose import JWTError, jwt
from datetime import date, datetime, timedelta
from dotenv import load_dotenv
import os
from typing import Dict
from .schemas import TokenData, db
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

load_dotenv("api/.env")

# To generate secret key use below code
# from base64 import b64encode
# from secrets import token_bytes
# secret_key = b64encode(token_bytes(32)).decode()
# Or
# import secrets
# secret_key = secrets.token_hex(32)

SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES"))


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def create_access_token(payload: Dict):
    to_encode = payload.copy()

    expiration_time = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expiration_time})

    jw_token = jwt.encode(to_encode, key=SECRET_KEY, algorithm=ALGORITHM)

    return jw_token


def verify_access_token(token: str, credential_exception):
    try:
        payload = jwt.decode(token, key=SECRET_KEY, algorithms=[ALGORITHM])

        id: str = payload.get("id")

        if not id:
            raise credential_exception

        token_data = TokenData(id=id)
        return token_data
    except JWTError:
        raise credential_exception


async def get_current_user(token: str = Depends(oauth2_scheme)):
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token could not be verified",
        headers={"WWW-AUTHENTICATE": "Bearer"}
    )

    current_user_id = verify_access_token(token, credential_exception).id

    current_user = await db["users"].find_one({"_id": current_user_id})

    return current_user
