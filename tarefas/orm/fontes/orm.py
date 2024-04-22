from decouple import config
from sqlalchemy import MetaData, Table, create_engine

# DEFINE THE DATABASE CREDENTIALS
user = config("USER")
password = config("PASSWORD")
host = config("HOST")
port = config("PORT")
database = config("DATABASE")

def get_connection():
	return create_engine(
		url="postgresql://{0}:{1}@{2}:{3}/{4}".format(
			user, password, host, port, database
		)
	)

engine = get_connection()

metadata = MetaData()
metadata.reflect(bind=engine)

project_table= Table('projeto', metadata, autoload_with=engine)
atvd_table = Table('atividade', metadata, autoload_with=engine)

# letra A
inserindo = atvd_table.insert().values(descricao='ES2 - Atividade ORM', projeto=3, data_inicio='2019-08-20', data_fim='2019-10-20')
# result1 = engine.connect().execute(inserindo)

# letra B
atualizando = project_table.update().where(project_table.c.codigo == 3).values(responsavel=2)
# result2 = engine.connect().execute(atualizando)



with engine.connect() as connection:
    # Inserindo nova atividade
    print("INSERINDO NOVA ATIVIDADE\n")
    result1 = connection.execute(inserindo)
    print("ATIVIDADE INSERIDA\n")
    
    # Atualizando projeto
    print("ATUALIZANDO PROJETO\n")
    result2 = connection.execute(atualizando)
    print("PROJETO ATUALIZADO\n")
    
	# letra c
    print("EXIBINDO PROJETOS\n")
    final_result1 = connection.execute(project_table.select())
    for row in final_result1:
          print(row)
          
    print("EXIBINDO ATIVIDADES\n")
    final_result2 = connection.execute(atvd_table.select())
    for row in final_result2:
          print(row)

