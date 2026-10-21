from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Optional
from datetime import datetime

# 1. Contém senha pois o usuário precisa enviar para se cadastrar.
# NÃO contém id nem criado_em / po banco gera automaticamente.

class UsuarioCreate(BaseModel):
    nome: str = Field(..., min_length=2, max_length=100,description="Não coloque números, não iniciar e terminar com espaços!")
    email: EmailStr = Field(..., description="Insira um email váildo. Exemplo: exemplodeemail123@email.com")
    senha: str = Field(..., min_length=8, description="Crie uma senha no minimo de 8 caracteres. Mínimo: 1 letra maiúscula. Mínumo: conter 2 números")

# @field_validator valida o campo 'nome' antes de salvar
# Se a validação falhar: raise ValueError com a mensagem de erro
# Se passar: return valor (o valor é validado)

    @field_validator('nome')
    @classmethod
    def nome_sem_numeros(cls, valor:str) -> str:
        if any(char.isdigit() for char in valor):
            raise ValueError("Nome não pode conter números")
        if not valor.strip():
            raise ValueError('Nome não pode ser só espaços')
        return valor.strip()

    @field_validator('senha')
    @classmethod
    def senha_deve_ter_letra_numero(cls, valor:str) -> str:
        tem_letra = any(caracter.isalpha() for caracter in valor)
        tem_numero = any(caracter.isdigit() for caracter in valor)
        if not tem_letra or not tem_numero:
            raise ValueError("Senha deve conter letras e números")
        return valor

# 2. Schema de ATUALIZAÇÃO PARCIAL (PATCH)
# Todos os campos são opcionais - o usuário envia só o que mudou.
# Não inclui senha - troca de senha seria um endpoint separado.

class UsuarioPatch(BaseModel):
    nome: Optional[str] = Field(..., min_length=2, max_length=100,description="Não coloque números, não iniciar e terminar com espaços!")
    email: Optional[EmailStr] = Field(..., description="Insira um email váildo. Exemplo: exemplodeemail123@email.com")

    @field_validator('nome')
    @classmethod
    def nome_sem_numeros(cls,valor):
        if valor and any(char.isdigit() for char in valor):
            raise ValueError('Nome não pode conter números')
        return valor.strip() if valor else valor

# 3.  UsuarioResponse - RESPOSTA (o que a API retorna)
class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: str
    # Não se coloca o campo da senha aqui para que não apareça na tela de quem acessar
    ativo: bool
    criado_em: datetime

    class Config:
        from_attributes = True

class ErroResponse(BaseModel):
    erro: str
    detalhe: Optional[str] = None