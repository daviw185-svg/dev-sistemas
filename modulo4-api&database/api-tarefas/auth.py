import bcrypt
from jose import JWTError, jwt
from datetime import datetime, timedelta, timezone
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

SECRET_KEY = 'mensagem-chave'
ALGORITHM = 'HS256'
EXPIRA_MIN = 60

# HASH: senha criada pelo usuario que é criptografado
# HTTPBearer faz o Swagger mostrar um campo simples para colar o token
# Em vez de usar OAuth2PasswordBearer que ped username/password
security = HTTPBearer()

# Criar função criar_hash
def criar_hash(senha: str) -> str:
    return bcrypt.hashpw(senha.encode(), bcrypt.gensalt()).decode()

# Criar função verificar_senha
def verificar_senha(senha: str, hash_salvo: str) -> bool:
    return bcrypt.checkpw(senha.encode(), hash_salvo.encode())

# Criar função criar_token
def criar_token(dados: dict) -> str:
    payload = dados.copy() # Payload é um conjunto de informações, como, senha e nome de usuário
    payload["exp"] = datetime.now(timezone.utc) + timedelta(minutes=EXPIRA_MIN)
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

# Criar função usuario_logado
def usuario_logado(
        credentials: HTTPAuthorizationCredentials = Depends(HTTPBearer()),
) -> str:
    token = credentials.credentials # pega só o token, sem Bearer
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if not email:
            raise HTTPException(401, "Token inválido")
        return email
    except JWTError:
        raise HTTPException(401, "Token inválido ou expirado ")