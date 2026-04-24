import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
        host="127.0.0.1",
        port="3306",
        user="root",
        password="root",
        database="dev_burguer"
    )
    cursor = conexao.cursor(dictionary=True)
    return conexao, cursor