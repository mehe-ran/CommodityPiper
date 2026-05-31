import secrets
from fastapi import Security, HTTPException, status
from fastapi.security import APIKeyHeader

# define the header key expected from clients
api_key_header = APIKeyHeader(name="x-api-key", auto_error=False)

# generate a secure random token for new clients
def generate_api_token() -> str:
    return secrets.token_urlsafe(32)

# validate incoming requests
def verify_api_key(api_key: str = Security(api_key_header)):
    if not api_key:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="missing or invalid api key"
        )
    return api_key