from pydantic import BaseModel, field_validator
from typing import Optional
from enum import Enum 

# Enum: Define os valores aceitos para o campo cargo
# Aparece como dropdown no swagger(a página da API no Chrome) automaticamente

class CargoEnum(str, Enum):
    engMec = 'Engenheiro Mecânico'
    mec = 'Mecânico'

# Schema de entrada: o que o cliente envia (SEM ID)
class UsuarioEntrada (BaseModel):
    nome: str
    email: str
    cargo: str
    ativo: bool = True
    salario: Optional[float] = None

    @field_validator('nome')
    @classmethod
    def validar_nome(cls, valor: str) -> str:
        valor = valor.strip() # Strip: Eliminação de campos de espaços desnecessários
        if len(valor) < 3: # O nome não pode ser menor do que 3 caractéres
            raise ValueError('Mínimo 3 caracteres')
        return valor.title() # 

# Schema de saída: o que o servidor retorn (COM ID)
class UsuarioSaida(BaseModel):
    id: int
    nome: str
    email: str
    cargo: CargoEnum
    ativo: bool
    salario: Optional[float] = None

    # Schema para atualização parcial (Patch)
    # Todos os campos são Optional - o cliente envia só o que quer mudar

class UsuarioParcial(BaseModel):
    nome: Optional[str] = None
    email: Optional[str] = None
    cargo: Optional[CargoEnum] = None # Somente os cargos que estão na classo CargoEnum
    ativo: Optional[bool] = None
    salario: Optional[float] = None

