# sudo apt-get update
# sudo apt-get install libmariadb-dev
# pip install mariadb

import mariadb

# Parâmetros de conexão
conn_params = {
    'host': 'localhost',        # ou o IP do container se necessário
    'port': 3306,               # Porta exposta do container
    'user': 'myuser',           # Usuário criado
    'password': 'mypassword',   # Senha do usuário
    'database': 'mydb'          # Nome do banco de dados
}

try:
    # Estabeleça uma conexão
    connection = mariadb.connect(**conn_params)
    print("Conectado ao banco de dados com sucesso!")

    cursor = connection.cursor()

    # Crie a tabela cakes
    cursor.execute("CREATE TABLE IF NOT EXISTS cakes (id INT AUTO_INCREMENT PRIMARY KEY, cake VARCHAR(100), price DECIMAL(10,2) DEFAULT 1.99)")

    # Popule a tabela cakes com alguns dados
    cursor.execute("INSERT INTO cakes (cake, price) VALUES (?, ?)", ("Chocolate Cake", 12.99))

    # Recupere os dados da tabela cakes
    cursor.execute("SELECT id, cake, price FROM cakes")

    # Imprima o conteúdo
    row = cursor.fetchone()
    while row:
        print(*row, sep=' ')
        row = cursor.fetchone()

    # Vários inserts
    sql = "INSERT INTO cakes (cake, price) VALUES (?, ?)"
    data = [
        ("Vanilla Cake", 9.99),
        ("Red Velvet Cake", 15.99),
        ("Carrot Cake", 11.99),
        ("Cheesecake", 13.99),
        ("Lemon Cake", 10.99)
    ]

    # Insira os dados
    cursor.executemany(sql, data)
    
    cursor.execute("SELECT * FROM cakes")

    # Imprima o conteúdo
    rows = cursor.fetchall()
    for row in rows:
        print(row)

except mariadb.Error as e:
    print(f"Erro ao conectar ao MariaDB ou executar operações: {e}")

finally:
    # Feche os recursos
    if cursor:
        cursor.close()
    if connection:
        connection.close()
