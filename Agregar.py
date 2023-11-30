import mysql.connector

class SistemaBiblioteca:
    def __init__(self, host, user, password, database):
        self.conexion = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

    def agregar_usuario(self, id_usuario, nombre, direccion, dni):
        with self.conexion.cursor() as cursor:
            insert_query = "INSERT INTO Usuario (ID_usuario, Nombre, Direccion, DNI) VALUES (%s, %s, %s, %s)"
            datos_usuario = (id_usuario, nombre, direccion, dni)
            try:
                cursor.execute(insert_query, datos_usuario)
                self.conexion.commit()
            except mysql.connector.errors.IntegrityError:
                print("El usuario ya existe")
            except Exception as e:
                print("Ocurrió un error inesperado:", e)
                self.conexion.rollback()


if __name__ == "__main__":
    sistema_biblioteca = SistemaBiblioteca("127.0.0.1", "root", "", "sistema_biblioteca")
    sistema_biblioteca.agregar_usuario(9, "tiny", "50", "52")
    sistema_biblioteca.close()
