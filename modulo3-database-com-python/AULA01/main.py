from sqlalchemy import Column, Integer, String, Boolean, text
from app.database import engine, Base, SessionLocal

class Departamento(Base):
    __tablename__ = 'departamentos'
    id =    Column(Integer, primary_key=True, autoincrement=True)
    nome =  Column(String(150), nullable=False)
    sigla = Column(String(10), nullable=False)
    ativo = Column(Boolean, default=True)

# Criar a tabela do banco
Base.metadata.create_all(bind=engine)
print('Tabela criada!')

# Inserir dados via sessão 
db = SessionLocal()
try:
    # Verificar se já tem dados
    if db.query(Departamento).count() == 0:
        db.add_all([
             Departamento(nome='Tecnologia da Informação', sigla='TI'),
             Departamento(nome='Recursos Humanos', sigla='RH'),
             Departamento(nome='Financeiro', sigla='FIN'),
             Departamento(nome='Comercial', sigla='COM'),
        ])
        db.commit()
        print('Dados Inseridos')

# Consultar via SQLAlchemy
    deptos = db.query(Departamento).order_by(Departamento.nome).all()
    print(f'\n{len(deptos)} Departamentos no banco: ')
    for d in deptos:
        print(f'  (d.id): i.nome ({d.sigla})')
finally:
    db.close()         
          