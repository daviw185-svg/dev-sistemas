from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, field_validator
from typing import Optional
from fastapi import Response

app = FastAPI(title='API de Cadastro - SENAI', version='0.2.0')

# Modelo Pydantic: define a estrutura e os tipos
class Usuario(BaseModel):
    nome: str #obrigatório
    email: str #obrigatório
    cargo: str #origatório
    ativo: bool = True # Valor Padrão
    salario: Optional[float] = None # Campo opcional

# Observar os espaçamentos:

    @field_validator('nome') # Validar o nome
    @classmethod
    def validar_nome(cls, v):
        v = v.strip()
        if len(v) < 3:
            raise ValueError('Nome deve ter pelo menos 3 caracteres')
        return v.title() 
    # Modelo de resposta: incluir o ID gerado pelo servidor
class UsuarioResposta(BaseModel):
    id: int
    nome: str
    email: str
    cargo: str
    ativo: bool
    salario: Optional[float] = None

usuarios_db: list[UsuarioResposta] = [
    UsuarioResposta(id=1, nome='David Willian', email='ivadw185@gmail.com', 
                    cargo='Engenheiro Mecânico', ativo=True, salario=5350.0),
    UsuarioResposta(id=2, nome='Arthur Vilela', email='artvilela45@gmail.com', 
                    cargo='TI', ativo=False, salario=4580.0),
    UsuarioResposta(id=3, nome='Max Muller', email='mmvonnseek@gmail.com', 
                    cargo='Desenvolvedor Red Hat', ativo=True, salario=12000.0),
    UsuarioResposta(id=4, nome='Diana Romanoff', email='blackwindow44@gmail.com', 
                    cargo='Cinema', ativo=True, salario=13620.0),
]
proximo_id = 5

@field_validator('salario')# qual campo vamos validar?
@classmethod
def validar_salario(cls, v):
    if v is None: # se não enviou salário, deixa passar
        return v
    if v <= 0:  # qual comparação bloqueia negativos e zero?
        raise ValueError('Salário Incorreto. Digite um valor acima de 0') # escreva uma mensagem de erro
    return v

# GET / usuarios - Lista todos os usuários

@app.get('/usuarios', response_model=list[UsuarioResposta])
def listar_usuario():
    return usuarios_db

# Rota que retorna só os usuários ativos
@app.get('/usuarios/ativos', response_model=list[UsuarioResposta]) # qual modelo de resposta?
def listar_ativos():
    return [u for u in usuarios_db if u.ativo == True ] # qual campo? qual valor?

# Rota que filtra por cargo
@app.get('/usuarios/cargo/{cargo}', response_model=list[UsuarioResposta]) # Nome do Parâmetro
def lista_por_cargo(cargo:str):     # Mesmo nome
    return[u for u in usuarios_db if u.cargo.lower() == cargo.lower() ]

# Rota de informações
@app.get('/info', tags=['Geral'])
def info():
    total = len(usuarios_db)
    ativos = len([u for u in usuarios_db if u.ativo == True])
    return {
        'total_arquivos': total,
        'usuarios_ativos': ativos,
        'cargo_aceitos': ['Engenheiro Mecânico', 'TI', 'Desenvolvedor Red Hat', 'Cinema'],
    }

@app.get('/usuarios/{usuario_id}', response_model=UsuarioResposta)
def buscar_usuario(usuario_id: int):
    for usuario in usuarios_db:
        if usuario.id == usuario_id:
            return usuario
    raise HTTPException(status_code=404, detail='Usuário não encontrado')

# POST - Cria um novo usuário
@app.post('/usuarios', response_model=UsuarioResposta, status_code=201)
def criar_usuario(dados: Usuario):
    global proximo_id
    #Verificar e-mail duplicado
    for u in usuarios_db:
        if u.email == dados.email:
            raise HTTPException(400, 'E-mail já cadatrado')
    novo = UsuarioResposta(id=proximo_id, **dados.model_dump())
    usuarios_db.append(novo)
    proximo_id += 1
    return novo

# PUT - Substitui o usuário inteiro
@app.put('/usuarios/{usuario_id}', response_model=UsuarioResposta)
def atualizar_usuario(usuario_id: int, dados: Usuario):
    for inpuut, user in enumerate(usuarios_db):
        if user.id == usuario_id:
            atualizado = UsuarioResposta(id=usuario_id, **dados.model_dump())
            usuarios_db[inpuut] = atualizado
            return atualizado
    raise HTTPException(404, 'Usuário não encontrado') 

# DELETE - Deleta um usuário
@app.delete('/usuarios/{usuarios_id}', status_code=204)
def deletar_usuario(usuario_id: int):
    for inpuut, u in enumerate(usuarios_db):
        if u.id == usuario_id:
            usuarios_db.pop(i)
            return Response(status_code=204)
    raise HTTPException(404, 'Usuário não encontrado')






