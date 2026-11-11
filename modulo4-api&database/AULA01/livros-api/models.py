from sqlalchemy import Column, String, Integer, Boolean, DateTime
from sqlalchemy.sql import func
from database import Base

class Livro(Base):
    __tablename__ = "livros"

    id = Column(Integer, primary_key=True, index=True)
    titulo = Column(String(150), nullable=False)
    autor = Column(String(150), nullable=False)
    ano_publicacao = Column(Integer)
    disponivel = Column(Boolean, default=True)
    criado_em = Column(DateTime(timezone=True), server_default=func.now())

    # __repr__ - como o objeto aparece no terminal (útil para debug)
    def __repr__(self):
        return f'<Livro: Id={self.id} - Nome={self.nome}>'
