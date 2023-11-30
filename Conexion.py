import mysql.connector

def conectado(host, user, password, database):
    conectado = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="",
        database="sistema_biblioteca"
    )
    return conectado
    