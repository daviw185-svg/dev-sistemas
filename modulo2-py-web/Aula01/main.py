from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware # Conectar o back-end com o front-end

# Criar a iastâncide da Aplicaçãso
app = FastAPI(
    title='API de Cadatro -- SENAI',
    description='Primeira API do curso de DS',
    version='0.1.0'
)

app.add_middleware(
     CORSMiddleware,
     allow_origins=['*'], # Em produção, especificar o domínio(o link) do front
     allow_methods=['*'],
     allow_headers=['*'],
)

#Rota raiz - GET/
@app.get('/status')
def status():
    return {'status': 'online', 'serviço': 'APT SENAI'}

# Lista simulada de usuários -- substitui o banco por enquanto
usuarios_db = [
    {'id': 33561, 'nome': 'Nicholas Duarte', 'cargo': 'MED', 'ativo': True},
    {'id': 35452, 'nome': 'Davi Willian', 'cargo': 'MA', 'ativo': True},
    {'id': 22513, 'nome': 'Jhonny Cruise', 'cargo': 'DEV', 'ativo': True},
]

# GET /usuaios - retorna todos os users
@app.get('/usuarios')
def listar_users():
    return usuarios_db

#GET /usuarios /(id) - retorna um usuário pelo ID
#O (id) é um path parameter - fastAPI extrai da URL automaticamente
@app.get('/usuarios/usuario_id')
def buscar_user(usuario_id: int):
    for usuario in usuarios_db:
        if usuario['id'] == usuario_id:
            return usuario
        return{'erro': 'Usuário não encontrado'}
    
@app.get('/usuarios/busca')
def buscar_name(nome: str = ''):
        if not nome:
            return usuarios_db
        filtrados = [u for u in usuarios_db if nome.lower() in u ['nome'].lower()]
        return filtrados