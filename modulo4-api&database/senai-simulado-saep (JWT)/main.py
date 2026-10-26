from fastapi import FastAPI
from database import engine, Base
import models
from routers import auth_routers, usuarios, produtos, movimentacoes

app = FastAPI(
    title="API de Almoxarifado",
    description="Sistema de controle de estoque — Simulado SAEP",
    version="1.0.0",
)

Base.metadata.create_all(bind=engine)

app.include_router(usuarios.router)
app.include_router(produtos.router)
app.include_router(movimentacoes.router)
app.include_router(auth_routers.router)


@app.get("/")
def raiz():
    return {"mensagem": "API de Almoxarifado funcionando!"}