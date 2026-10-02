from app.database import engine, SessionLocal
from app import models
from app.models import Categoria, Fornecedor, Produto


# Cria as tabelas definidas nos modelos
models.Base.metadata.create_all(bind=engine)
print("Tabelas criadas com sucesso!!")

db = SessionLocal()

# categorias
cat1 = Categoria(nome="Eletrônicos")
cat2 = Categoria(nome="Roupas")
cat3 = Categoria(nome="Alimentos")

db.add(cat1)
db.add(cat2)
db.add(cat3)
db.commit()
db.refresh(cat1)
db.refresh(cat2)
db.refresh(cat3)
print(f'Categorias criadas: {cat1.id}, {cat2.id}, {cat3.id}')

# fornecedores
forn1 = Fornecedor(nome="Tech LTDA", contato="techltda@gmail.com")
forn2 = Fornecedor(nome="KBAL Sport", contato="kbaltshirts@gmail.com")
forn3 = Fornecedor(nome="NOS Brasil Energy", contato="nos.brasilenergy@gmail.com")

db.add(forn1)
db.add(forn2)
db.add(forn3)
db.commit()
db.refresh(forn1)
db.refresh(forn2)
db.refresh(forn3)
print(f'Fornecedores criados: {forn1.id}, {forn2.id}, {forn3.id}')

# produtos
produtos = [
    Produto(nome="Arduíno UNO Leonardo", preco=75.90, quantidade=30, categoria_id=cat1.id, fornecedor_id=forn1.id),
    Produto(nome="Camisa Robot's District", preco=56.90, quantidade=40, categoria_id=cat2.id, fornecedor_id=forn2.id),
    Produto(nome="Energético NOS Energy 450ml", preco=10.90, quantidade=70, categoria_id=cat3.id, fornecedor_id=forn3.id),
]
