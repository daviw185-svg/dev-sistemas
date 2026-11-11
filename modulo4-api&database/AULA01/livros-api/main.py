from fastapi import FastAPI
from database import engine, Base
from router import router as livro_router
from tags import tags_metadata

# Criar as tabelas no banco ao inicar a API
# Se o banco.db não existir, criar o arquivo e as tabelas
# Se já existir, não faz nada - não apaga os dados
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title='API de Livros',
    description = "## API de gerenciamneto de livros ",
    version="3.0.0",
    openapi_tags=tags_metadata
)

# Registra o router com prefixo /produtos
app.include_router(livro_router)

@app.get('/')
def raiz():
    return {"status":"online", "docs":"/docs", "versao":"2.0.0"}


 

























































































