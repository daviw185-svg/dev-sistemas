from app.database import engine, SessionLocal
from app import models
from app.models import Genero, Autor, Livro


# Cria as tabelas definidas nos modelos
models.Base.metadata.create_all(bind=engine)
print("Tabelas criadas com sucesso!!")

db = SessionLocal()

# Generos
gen1 = Genero(nome="Filosófico")
gen2 = Genero(nome="Religioso")
gen3 = Genero(nome="Sci-Fi")

db.add(gen1)
db.add(gen2)
db.add(gen3)
db.commit()
db.refresh(gen1)
db.refresh(gen2)
db.refresh(gen3)
print(f'Generos criados: {gen1.id}, {gen2.id}, {gen3.id}')

# autores
aut1 = Autor(nome="Filipe Fontes", nacionalidade="Brasileiro")
aut2 = Autor(nome="JB Carvalho", nacionalidade="Brasileiro")
aut3 = Autor(nome="C.S. Lewis", nacionalidade="Irlandês")
aut4 = Autor(nome="Luciano Subirá", nacionalidade="Brasileiro")
aut5 = Autor(nome="Kip Thorne", nacionalidade="Norte-Americano")

db.add(aut1)
db.add(aut2)
db.add(aut3)
db.add(aut4)
db.commit()
db.refresh(aut1)
db.refresh(aut2)
db.refresh(aut3)
db.refresh(aut4)
print(f'Autores Registrados: {aut1.id}, {aut2.id}, {aut3.id}, {aut4.id}, {aut5.id}')

# Livros
livros = [
    Livro(titulo="Cristianismo puro e simples", ano_publicacao=1952, genero_id=gen2.id, autor_id=aut3.id),
    Livro(titulo="A Jornada: De Meninos a Homens", ano_publicacao=2022, genero_id=gen2.id, autor_id=aut2.id),
    Livro(titulo="Filosofia essencial para cristãos", ano_publicacao=2025, genero_id=gen1.id, autor_id=aut1.id),
    Livro(titulo="O Cuidado do Corpo", ano_publicacao=2024, genero_id=gen2.id, autor_id=aut4.id),
    Livro(titulo="Interstellar", ano_publicacao=2014, disponivel=False, genero_id=gen3.id, autor_id=aut5.id),
]

for l in livros:
    db.add(l)
db.commit()
print(f'{len(livros)} Livros inseridos.')

# Listar pra confirmar
todos = db.query(Livro).all()
print("\n Livros no banco")
for l in todos:
    print(f' [{l.id}] {l.titulo} - {l.ano_publicacao}')
db.close()