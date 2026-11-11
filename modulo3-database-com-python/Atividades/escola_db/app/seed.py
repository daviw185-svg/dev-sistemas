from app.database import SessionLocal
from app.models import Curso, Aluno

def popular_banco():
    db = SessionLocal()

    try: 
        if db.query(Curso).count() > 0:
            print('Banco já populado. Pulando...')
            return

        db.add_all([
            Curso(nome='Desenvolvimento de Sistemas', duracao=1200),
            Curso(nome='Engenharia Mecânica', duracao=1400),
            Curso(nome='Sistema de Refrigeração', duracao=1300),
            Curso(nome='Eletroeletrônica', duracao=1250),
        ])

        db.add_all([
            Aluno(nome='Davi Willian', email='davi.w.s@aluno.senai.br', matricula = '7578543'),
            Aluno(nome='Heitor Amazonas', email='heitor.carvalho@aluno.senai.br', matricula = '3346264'),
            Aluno(nome='Luiz Guilherme', email='luiz.araujo@aluno.senai.br', matricula = '1365714'),
            Aluno(nome='João Martins', email='joao.martins@aluno.senai.br', matricula = '3254732'),
        ])

        db.commit()
        print('Banco populado com sucesso!')

    except Exception as e:
        db.rollback() # desfazer se der erro
        print(f'Erro: {e}')
    finally:
        db.close()
if __name__ == '__main__':
    popular_banco()