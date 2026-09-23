from app.database import SessionLocal
from app.models import Departamento, Cargo

def popular_banco():
    db = SessionLocal()
    try: 
        #Se já tem dados, não inserir de novo
        if db.query(Departamento).count() > 0:
            print('Banco já preenchido. Pulando...')
            return
        db.add_all([
            Departamento(nome='Tecnologia da Informação', sigla='TI'),
            Departamento(nome='Recursos Humanos', sigla='RH'),
            Departamento(nome='Financeiro', sigla='FIN'),
            Departamento(nome='Comercial', sigla='COM'),
            Departamento(nome='Engenharia', sigla='ENG'),
            Departamento(nome='Elétrica', sigla='ELT'),
        ])

        db.add_all({
            Cargo(titulo='Desenvolvedor de Software', nivel='Junior', sal_min=2500, sal_max=4100),
            Cargo(titulo='Desenvolvedor de Software', nivel='Pleno', sal_min=4300, sal_max=7200),
            Cargo(titulo='Design', nivel='Junior', sal_min=2120, sal_max=3400),
            Cargo(titulo='Analista RH', nivel='Pleno', sal_min=6000, sal_max=8000),
            Cargo(titulo='Mecânico', nivel='Junior', sal_min=3500, sal_max=4200),
            Cargo(titulo='Mecânico', nivel='Pleno', sal_min=4500, sal_max=6000),
        })

        db.commit()
        print('Banco populado com sucesso!')

    except Exception as erro:
        db.rollback()
        print(f'Erro: {erro}')
    finally:
        db.close()
if __name__=='__main__':
    popular_banco()


