from app.database import engine, Base, SessionLocal
from app import models # Importar para registrar os modelos na Base
from app.seed import popular_banco
from app.crud import criar_funcionario

Base.metadata.create_all(bind=engine)
popular_banco()
db = SessionLocal()
try:
    novo = criar_funcionario(db, 'Pedro Alves', 'pedro@sistemafibra.org', 3200.0)
    print(f'Criado: {novo}')
finally:
    db.close()