from sqlalchemy.orm import Session
from app.models import Tutor, Animal, Atendimento

def inserir_tutor(db: Session, nome: str, telefone: str, email: str):

    novo = Tutor(nome=nome, telefone=telefone, email=email)

    db.add(novo)
    db.commit()
    db.refresh(novo) 
    return novo

def inserir_animal(db: Session, nome_animal: str, especie: str, raca: str, peso_kg: float, tutor_id: int):

    novo = Animal(nome_animal=nome_animal, especie=especie, raca=raca, peso_kg=peso_kg, tutor_id=tutor_id)

    db.add(novo)
    db.commit()
    db.refresh(novo) 
    return novo

def inserir_atendimento(db: Session, data_atend: str, motivo: str, valor_cons: float, animal_id: int):

    novo = Atendimento(data_atend=data_atend, motivo=motivo, valor_cons=valor_cons, animal_id=animal_id)

    db.add(novo)
    db.commit()
    db.refresh(novo) 
    return novo






