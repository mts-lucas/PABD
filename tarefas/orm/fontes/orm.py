from sqlalchemy import create_engine, MetaData, Table
from decouple import config

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

tabela_projeto = Table('projeto', metadata, autoload_with=engine)
tabela_atividade = Table('atividade', metadata, autoload_with=engine)


result = engine.connect().execute(tabela_projeto.select())
for row in result:
	print(row)