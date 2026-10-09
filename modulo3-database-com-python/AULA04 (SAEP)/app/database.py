from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# URL do banco SQLite - Cria o arquivo estoque.db na raiz do projeto

DATABASE_URL = "sqlite:///./estoque.db"
engine = create_engine(
    DATABASE_URL, 
    connect_args={"check_same_thread": False} # connect_args: obrigatório do SQLite
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) # autocomnit: evita que as informações sejam salvas automaticamente; autoflush: não deixa commitar uma atualização; bind: qual configuração o banco vai utilizar em cada sessão 
class Base(DeclarativeBase):
    pass
