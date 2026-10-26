from app.database import engine, Base, SessionLocal
from app import models # Importar para registrar os modelos na Base
from app.seed import popular_banco
from app.crud import criar_funcionario, listar_funcionarios, buscar_funcionarios, atualizar_funcionario, desativar_funcionario
from app.crud import criar_depto, listar_depto, up_depto, off_depto

Base.metadata.create_all(bind=engine)
popular_banco()
db = SessionLocal()
try:
    novo = criar_funcionario(db, 'Pedro Alves', 'pedro@sistemafibra.org', 3200.0)
    print(f'Criado: {novo}')

    todos = listar_funcionarios(db)
    print(f'Total: {len(todos)} funcionarios')
    for funcionario in todos:
        print(f' {funcionario.nome} - R${funcionario.salario}')

    um = buscar_funcionarios(db, 1)
    if um:
        print(f'\nFuncionario 1: {um.nome}')

# 3 UPDATE
    atualizado = atualizar_funcionario(db, 1, salario=5600.0)
    print(f'{atualizado.nome}: R$ {atualizado.salario}')

# 4 DELETE
    desativado = desativar_funcionario(db, 3)
    print(*f'{desativado.nome}: ativo={desativado.ativo}')

    ativo = listar_funcionarios(db, apenas_ativos=True)
    print(f'Ativos restantes: {len(ativo)}')
finally:
    db.close()

db = SessionLocal()
try:
    #Criar
    novo = criar_depto(db, 'Jurídico', 'JUR')
    print(f'Criado: {novo.nome} ({novo.sigla})')

    # Listar
    todos = listar_depto(db)
    print(f'Total: {len(todos)} departamentos')

    # Atualizar
    atualizado = up_depto(db, novo.id, 'Jurídico e Compliance', 'JUR')
    print(f'Atualizado: {atualizado.nome} ({atualizado.sigla})')

    # Desativar
    desativado = off_depto(db, novo.id)
    print(f'Desativado: {desativado.nome} - Ativo={desativado.ativo}')
finally:
    db.close()