import mysql.connector
from tabulate import tabulate

class SistemaBiblioteca:
    def __init__(self, host, user, password, database):
        self.conexion = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

    def get_usuarios(self):
        with self.conexion.cursor() as cursor:
            cursor.execute("SELECT ID_usuario, Nombre, Direccion, DNI FROM Usuario")
            data = cursor.fetchall()

            usuarios = []
            for row in data:
                usuario = Usuario(row[0], row[1], row[2], row[3])
                usuarios.append(usuario)

            return usuarios

class Usuario:
    def __init__(self, ID_usuario, Nombre, Direccion, DNI):
        self.ID_usuario = ID_usuario
        self.Nombre = Nombre
        self.Direccion = Direccion
        self.DNI = DNI

    def __iter__(self):
        yield self.ID_usuario
        yield self.Nombre
        yield self.Direccion
        yield self.DNI


if __name__ == "__main__":
    sistema_biblioteca = SistemaBiblioteca("127.0.0.1", "root", "", "sistema_biblioteca")
    usuarios = sistema_biblioteca.get_usuarios()

    headers = {"ID USUARIO": "ID_usuario", "NOMBRE": "Nombre", "DIRECCIÓN": "Direccion", "DNI": "DNI"}

    print(tabulate([usuario.__dict__ for usuario in usuarios], headers=headers, tablefmt="grid"))
