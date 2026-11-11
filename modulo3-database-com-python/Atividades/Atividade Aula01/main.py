from sqlalchemy import Column, Integer, String, Boolean, Float, text
from app.database import engine, Base, SessionLocal

class Departamento(Base):
    __tablename__ = 'departamentos'
    id =    Column(Integer, primary_key=True, autoincrement=True)
    nome =  Column(String(150), nullable=False)
    sigla = Column(String(10), nullable=False)
    ativo = Column(Boolean, default=True)

class Cargo(Base):
    __tablename__='cargos' # nome da tabela
    id = Column(Integer, primary_key=True, autoincrement=True)
    titulo = Column(String(100), nullable=False)
    nivel = Column(String(20), nullable=False)
    salario_min = Column(Float, nullable=False)
    salario_max = Column(Float, nullable=False)
    ativo = Column(Boolean, default=True)

    def __repr__(self):
        return f'<Cargo titulo={self.titulo} nivel={self.nivel}>' 


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
        db.commit() # Confirmar no banco
        print('Dados Inseridos')

# Popular cargos (se ainda não tiver dados)
    if db.query(Cargo).count() == 0:
        db.add_all([
            Cargo(titulo='Desenvolvedor', nivel='Júnior', salario_min=2500, salario_max=4000),
            Cargo(titulo='Desenvolvedor', nivel='Pleno', salario_min=4000, salario_max=7000),
            Cargo(titulo='Designer', nivel='Júnior', salario_min=2200, salario_max=3500),
            Cargo(titulo='Analista RH', nivel='Pleno', salario_min=3500, salario_max=6000),
        ])
        db.commit()
        print('Cargos inseridos✅')


# Consultar via SQLAlchemy
    deptos = db.query(Departamento).order_by(Departamento.nome).all()
    print(f'\n{len(deptos)} Departamentos no banco: ')
    for d in deptos:
        print(f'  (d.id): i.nome ({d.sigla})')
   
    #1. Listar todos os cargos ordenados por título
    todos = db.query(Cargo).order_by(Cargo.titulo).all()
    print(f'\n{len(todos)} cargos cadastrados: ')
    for c in todos: # "c" = cargos
        print(f' {c.titulo} ({c.nivel}) -- R${c.salario_min} a R${c.salario_max}')

    #2. Filtrar só cargos Júnior
    juniors = db.query(Cargo).filter(Cargo.nivel=='JÚnior').all()
    print(f'\nCargos Júnior: {len(juniors)}')

    #3. Buscar um cargo específico pelo título
    designer = db.query(Cargo).filter(Cargo.titulo == 'Júnior'). first()
    if designer:
        print(f'Designer encontrado: faixa R${designer.salario_min} - R${designer.salario_max}')
    
finally:
    db.close()         
          