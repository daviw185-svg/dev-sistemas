from app.database import engine, Base
from app import models # Importar para registrar os modelos na Base
from app.seed import popular_banco

Base.metadata.create_all(bind=engine)
popular_banco()
print('Pronto')