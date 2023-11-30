import mysql.connector
from datetime import datetime 

class SistemaBiblioteca:
    def __init__(self, host, user, password, database):
        self.conexion = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

    def realizar_devolucion(self, id_usuario, id_libro):
        with self.conexion.cursor() as cursor:
            # Verificar si el libro está prestado
            cursor.execute("SELECT ID_libro FROM Prestamos WHERE ID_usuario = %s AND ID_libro = %s", (id_usuario, id_libro))
            libros_prestados = cursor.fetchall()

            if libros_prestados:
                # Actualizar el número de libros prestados para el usuario
                cursor.execute("UPDATE Usuario SET libros_prestados = libros_prestados - 1 WHERE ID_usuario = %s", (id_usuario,))

                # Sumar una unidad al stock del libro
                cursor.execute("UPDATE libros SET Stock = Stock + 1 WHERE ID_libro = %s", (id_libro,))

                # Obtener la fecha y hora actual
                fecha_devolucion = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # Insertar la devolución en la tabla Devoluciones
                cursor.execute("INSERT INTO Devoluciones (fecha_devolucion, ID_usuario, ID_libro) VALUES (%s, %s, %s)", (fecha_devolucion, id_usuario, id_libro))

                # Confirmar la operación
                self.conexion.commit()
                print("Devolución realizada con éxito.")
            else:
                print("El libro no está prestado.")
                
    def cerrar_conexion(self):
        self.conexion.close()

if __name__ == "__main__":
    sistema_biblioteca = SistemaBiblioteca("localhost", "root", "", "sistema_biblioteca")
    sistema_biblioteca.realizar_devolucion(1, 1)
    sistema_biblioteca.cerrar_conexion()
