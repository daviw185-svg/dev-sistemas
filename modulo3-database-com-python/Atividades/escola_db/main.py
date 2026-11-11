# CRIAR AS TABELAS NO BANCO

from app.database import engine, Base
from app import models
from app.seed import popular_banco

# Criar todas as tabelas que não existem
Base.metadata.create_all(bind=engine)
popular_banco()
print('Tabelas criadas!')