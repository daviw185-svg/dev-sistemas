from sqlalchemy.orm import Session
from app.models import Funcionario, Departamento

# CREATE
def criar_funcionario(db: Session, nome: str, email: str, salario: float):
    # 1) Verificar se o email já existe
    existe = db.query(Funcionario).filter(
        Funcionario.email == email
    ).first()

    if existe:
        raise ValueError(f'E-mail {email} já cadastrado')

    #2) Criar objeto
    novo = Funcionario(nome=nome, email=email, salario=salario)

    #3) Salvar no Banco
    db.add(novo)
    db.commit()
    db.refresh(novo) # busca o id pelo banco
    return novo

# READ - listar funcionários com cadastro ativo
def listar_funcionarios(db: Session, apenas_ativos: bool=True):
    query = db.query(Funcionario)
    if apenas_ativos:
        query = query.filter(Funcionario.ativo == True)
        return query.order_by(Funcionario.nome).all()

# READ - Buscar funcionario pelo id
def buscar_funcionarios(db: Session, funcionarios_id: int):
    return db.query(Funcionario).filter(
        Funcionario.id == funcionarios_id
    ).first() # Retorna None se não encontrar

# UPDATE
def atualizar_funcionario(
        db: Session, funcionario_id: int,
        nome: str = None,
        salario: float = None     
): 
    func = buscar_funcionarios(db, funcionario_id)

    if not func: 
        raise ValueError(f'Funcionário {funcionario_id} não encontrado')

    # Atualizar só os campos que foram enviados
    if nome is not None:
        func.nome = nome
    if salario is not None:
        func.salario = salario
        
    db.commit()         # confirma a alteração no banco
    db.refresh(func)    # sincronizar
    return func

# DELETE
def desativar_funcionario(db: Session, funcionario_id: int):
    func = buscar_funcionarios(db, funcionario_id)

    if not func:
        raise ValueError(f'Funcionario {funcionario_id} não encontrado')

    if not func.ativo:
        raise ValueError(f'Funcionario {funcionario_id} já está inativo')

    func.ativo = False # Soft delete: só muda o campo
    db.commit()
    return func

# Atividade CRUD

def criar_depto(db: Session, nome: str, sigla: str):
    # Verificar se a sigla já existe
    existe = db.query(Departamento).filter(
        Departamento.sigla == sigla
    ).first() # First: se não encontrar retorna um valor nulo

    if existe: 
        raise ValueError(f'Sigla {sigla} já cadastrada')

    novo = Departamento(nome=nome, sigla=sigla)
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo

def listar_depto(db: Session):
    return db.query(Departamento).order_by(Departamento.nome).all()

def buscar_depto_por_id(db: Session, depto_id: int):
    return db.query(Departamento).filter(
        Departamento.id == depto_id
    ).first()

def up_depto(db: Session, depto_id: int, nome: str, sigla: str):
    depto = buscar_depto_por_id(db, 3)

    if not depto:
        raise ValueError(f'Departamento {depto_id} não encontrado')

    depto.nome = nome
    db.commit()
    db.refresh(depto)
    return depto

def off_depto(db: Session, depto_id: int):
    depto = buscar_depto_por_id(db, depto_id)

    if not depto:
        raise ValueError(f'Departamento {depto_id} não encontrado')

    depto.ativo = False
    db.commit()
    return depto