from jwt import encode, decode

key = "my_secret_key"
algorithm = "HS256"

def create_token(data: dict) -> str:
  token: str = encode(payload=data, key=key, algorithm=algorithm)
  return token

def validate_token(token: str) -> dict:
  uncode_token: dict = decode(token, key=key, algorithms=[algorithm])
  return uncode_token