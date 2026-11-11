from app.database import engine, SessionLocal
from app import models
from app.models import Tutor, Animal, Atendimento

models.Base.metadata.create_all(bind=engine)
print('Tabelas criadas com sucesso!!')

db = SessionLocal()

# Tutores
tut1 = Tutor(nome_completo='Flávio Guilherme', email='flavio.gui@gmail.com', telefone='(62) 93543-4567')
tut2 = Tutor(nome_completo='Ayrton Borba', email='ayrb375@gmail.com', telefone='(32) 95687-9003')

db.add(tut1)
db.add(tut2)
db.commit()
db.refresh(tut1)
db.refresh(tut2)
print(f'Tutores inseridos: {tut1.nome_completo} - ID: {tut1.id}, {tut2.nome_completo} - ID: {tut2.id}')

# Animais
anm1 = Animal(nome_animal='Simba', especie='Cachorro', raca='Shih Tzu', peso_kg=14.3, tutor_id=tut1.id)
anm2 = Animal(nome_animal='Chiquin', especie='Periquito', peso_kg=1.2, tutor_id=tut2.id)
anm3 = Animal(nome_animal='Garfield', especie='Gato', raca='Persa', peso_kg=10.8, tutor_id=tut2.id)

db.add(anm1)
db.add(anm2)
db.add(anm3)
db.commit()
db.refresh(anm1)
db.refresh(anm2)
db.refresh(anm3)

# Atendimentos
atend1 = Atendimento(data_atend='23-07-2026', motivo='Banho e Tosa bebê', valor_cons=50.90, animal_id=anm1.id)
atend2 = Atendimento(data_atend='19-08-2026', motivo='Tratamento nas asas', valor_cons=43.50, animal_id=anm2.id)
atend3 = Atendimento(data_atend='30-08-2026', motivo='Exame ouricular', valor_cons=72.90, animal_id=anm3.id)

db.add(atend1)
db.add(atend2)
db.add(atend3)
db.commit()
db.refresh(atend1)
db.refresh(atend2)
db.refresh(atend3)

todos = db.query(Atendimento).all()
print(f'\n Atendimentos da VetPet: ')
for a in todos: 
    print(f'Animais listados: \n - {anm1.nome_animal} - Espécie: {anm1.especie}\n - {anm2.nome_animal} - Espécie: {anm2.especie}\n - {anm3.nome_animal} - Espécie: {anm3.especie}')
    print(f'Atendimentos: \n - {atend1.motivo} | R$ {atend1.valor_cons}\n - {atend2.motivo} | R$ {atend2.valor_cons}\n - {atend3.motivo} | R$ {atend3.valor_cons} ')
db.close()