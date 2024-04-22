import psycopg2
from decouple import config

# DEFINE AS CREDENCIAIS DO BANCO DE DADOS
user = config("USER")
password = config("PASSWORD")
host = config("HOST")
port = config("PORT")
database = config("DATABASE")

def get_connection():
    return psycopg2.connect(
        dbname=database,
        user=user,
        password=password,
        host=host,
        port=port
    )

connection = get_connection()

cursor = connection.cursor()

# Letra A
inserindo = "INSERT INTO atividade (descricao, projeto, data_inicio, data_fim) VALUES (%s, %s, %s, %s)"
cursor.execute(inserindo, ('ES2 - Atividade ODBC', 4, '2018-08-20', '2018-10-20'))
connection.commit()

# Letra B
atualizando = "UPDATE projeto SET responsavel = %s WHERE codigo = %s"
cursor.execute(atualizando, (4, 2))
connection.commit()

# Letra C
print("EXIBINDO PROJETOS\n")
cursor.execute("SELECT * FROM projeto")
final_result1 = cursor.fetchall()
for row in final_result1:
    print(row)

print("EXIBINDO ATIVIDADES\n")
cursor.execute("SELECT * FROM atividade")
final_result2 = cursor.fetchall()
for row in final_result2:
    print(row)

# Fechando a conexão
connection.close()
