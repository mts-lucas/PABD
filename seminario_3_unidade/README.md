# Como executar o código

Para criar e rodar o servidor do mariadb em sua máquina execute o seguinte comando


<pre>docker run --name mariadb-container -e MYSQL_ROOT_PASSWORD=root -e MYSQL_DATABASE=mydb -e MYSQL_USER=myuser -e MYSQL_PASSWORD=mypassword -d mariadb:latest</pre>

Para poder utilizar a biblioteca no python é preciso instalar certas dependências, então execute o seguinte comando

<pre>
sudo apt-get update
sudo apt-get install libmariadb-dev
</pre>

Crie seu ambiente virtual, em seguida instale a biblioteca do mariadb em seu ambiente virtual

<pre>
pip install mariadb
</pre>

Por ultimo altere no código o host, para o o IP que a container do mariadb estiver rodando, ou usuario e senha diferentes caso tenha optado por mudar o comando docker no começo

<pre>
conn_params = {
    'host': 'localhost',        # ou o IP do container se necessário
    'port': 3306,               # Porta exposta do container
    'user': 'myuser',           # Usuário criado
    'password': 'mypassword',   # Senha do usuário
    'database': 'mydb'          # Nome do banco de dados
}
</pre>



