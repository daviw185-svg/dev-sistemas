from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from database import get_db
from models import Livro
from schema import LivroCreate, LivroPatch
from tags import tags_metadata

# APIRouter agrupa os endpoints - registramos no main.py
router = APIRouter(prefix='/livros', tags=['Livros'])

# GET/Livros - Lista todos os livros disponivels
# response_model=List[LivroResponse] - FastAPI formata a saída
# skip e limit - paginação simples
@router.get('/',
            tags=['Livros'],
            summary='Listar todos os livros',
            description='Todos os livros existentes no sistema são listados.',
            responses={
                  200: {'description': 'Listagem concluída'},
             })

def listar_livros(skip: int=0, limit: int=10,
                    db: Session = Depends(get_db)):
    return db.query(Livro).filter(Livro.disponivel == True).offset(skip).limit(limit).all()

# GET / Livros / (id) - Busca livro pelo ID
@router.get('/{livro_id}',
            tags=['Livros'],
            summary='Busca o livro pelo ID',
            description='Digite o ID do livro para encontrar suas informações', 
            responses={
                200: {'description': 'Busca concluída'},
                404: {'description': 'Livro não encontrado. Verifique se o ID está correto'},
            },)
def buscar_livro(livro_id: int, db: Session = Depends(get_db)):
    livro = db.query(Livro).filter(Livro.id == livro_id).first()
    if not livro or not livro.disponivel:
        raise HTTPException(status_code=404,
                            detail=f'Livro {livro_id} não encontrado')
    return livro

# POST / livros - Criar novo livro
@router.post('/', status_code=201,
            tags=['Livros'],
            summary='Criar livro.',
            description='Aqui você pode criar um livro.',
            responses={
                 201: {'description': 'Livro criado!'},
            })
def criar_livro(dados: LivroCreate, db: Session = Depends(get_db)):
    livro = Livro(
        titulo = dados.titulo,
        autor = dados.autor,
        ano_publicacao = dados.ano_publicacao,
    )
    db.add(livro)         # enfileira o INSERT
    db.commit()             # Executa no banco
    db.refresh(livro)     # Atualiza o objeto com id e criando_em no banco
    return livro

# PUT /livros/(id) - Substitui o livro inteiro
@router.put('/{livro_id}', 
            tags=['Livros'],
            summary='Substitui o livro inteiro',
            description='Neste campo, você pode substitui o livro.',
            responses={
                 200: {'description': 'Substituição realizada!'},
                 404: {'description': 'Livro não encontrado. Verifique se o ID está correto'},
            })
def substituir_livro(livro_id: int, dados: LivroCreate,
                       db: Session = Depends(get_db)):
    livro = db.query(Livro).filter(Livro.id == livro_id).first()
    if not livro or not livro.disponivel:
        raise HTTPException(status_code=404, detail='Não encontrado')
    livro.titulo = dados.titulo
    livro.autor = dados.autor
    livro.ano_publicacao = dados.ano_publicacao
    db.commit()
    db.refresh(livro)
    return livro

# PATCH /livro/(id) - Atualiza só os campo renviados
@router.patch('/{livro_id}',
            tags=['Livros'],
            summary='Atualiza só os campos renviados',
            description='Aqui você atualiza só aquilo que você quer mudar em relação alguma informação do livro',
            responses={
                200: {'description': 'Atualização concuída com sucesso!'},
                404: {'description': 'Livro não encontrado. Verifique se o ID está correto'},
            })
def atualizar_livro(livro_id: int, dados: LivroPatch,
                      db: Session = Depends(get_db)):
    livro = db.query(Livro).filter(Livro.id == livro_id).first()
    if not livro or not livro.disponivel:
            raise HTTPException(status_code=404, detail='Não encontrado')
    if dados.titulo is not None: livro.titulo = dados.titulo
    if dados.autor is not None: livro.autor = dados.autor
    if dados.ano_publicacao is not None: livro.ano_publicacao = dados.ano_publicacao
    db.commit()
    db.refresh(livro)
    return livro

# DELETE /livro/(id) - Soft delete (marca disponivel=False)
@router.delete('/{livro-id}', 
            tags=['Livros'],
            summary='Excluir livro',
            description='Excluir livro selecionado.',
            responses={
                200: {'description': 'Exclusão concluída'},
                404: {'description': 'Livro não encontrado. Verifique se o ID está correto'},
            })
def remover_livro(livro_id: int, db: Session = Depends(get_db)):
     livro = db.query(Livro).filter(Livro.id == livro_id).first()
     if not livro or not livro.disponivel:
          raise HTTPException(status_code=404, detail='Não Encontrado')
     livro.disponivel = False
     db.commit()
     return {'mensagem': f'Livro {livro_id} removido com sucesso'}

