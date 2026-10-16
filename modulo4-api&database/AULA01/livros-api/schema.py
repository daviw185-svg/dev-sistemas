from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

# Entrada: POST e PUT (campos obrigatórios)
class LivroCreate(BaseModel):
    titulo: str = Field(..., min_length=2, max_length=150)
    autor: str = Field(..., min_length=2, max_length=150) # gt=0 - Os valores têm que ser maior que zero
    ano_publicacao: int = Field(0, ge=0) # ge=0 - Maior ou igual a zero

# Entrada: PATCH (todos opcionais)
class LivroPatch(BaseModel):
    titulo: Optional[str] = Field(None, min_length=2, max_length=150)
    autor: Optional[str] = Field(None, min_length=2, max_length=150)
    ano_publicacao: Optional[int] = Field(None, ge=0) # ge=0 - Maior ou igual a zero

# Saída: O que a API retorna
class LivroResponse(BaseModel):
    id: int
    titulo: str
    autor: str
    ano_publicacao: int
    disponivel: bool
    criado_em: datetime

    class Config:
        from_attributes=True # Permite converter SQLAlchemy > Pydantic