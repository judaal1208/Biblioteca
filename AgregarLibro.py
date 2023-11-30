import mysql.connector

class SistemaBiblioteca:
    def __init__(self, host, user, password, database):
        self.conexion = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

    def agregar_libro(self, nombre, stock):
        with self.conexion.cursor() as cursor:
            # Insertar un nuevo libro en la tabla libros
            cursor.execute("INSERT INTO libros (Nombre, Stock) VALUES (%s, %s)", (nombre, stock))

            # Confirmar la operación
            self.conexion.commit()
            print("Libro agregado con éxito.")

    def cerrar_conexion(self):
        self.conexion.close()


if __name__ == "__main__":
    sistema_biblioteca = SistemaBiblioteca("localhost", "root", "", "sistema_biblioteca")
    sistema_biblioteca.agregar_libro("James Mosquera's ", 10)
    sistema_biblioteca.cerrar_conexion()
