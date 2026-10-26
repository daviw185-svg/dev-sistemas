# Definir mpdelo de tabelas
from app.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey

class Genero(Base):
    __tablename__ = 'generos' 
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(80), nullable=False, unique=True)

class Autor(Base):
    __tablename__ = 'autores'
    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String(80), index = True)
    nacionalidade = Column(String(80), nullable=False)

class Livro(Base):
    __tablename__ = 'livros'
    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(100), nullable=False)
    ano_publicacao = Column(Integer, nullable=False)
    disponivel = Column(Boolean, default=True)
    genero_id = Column(Integer, ForeignKey("generos.id"))
    autor_id = Column(Integer, ForeignKey("autores.id"))