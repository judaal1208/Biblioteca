import mysql.connector

class SistemaBiblioteca:
    def __init__(self, host, user, password, database):
        self.conexion = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

    def realizar_prestamo(self, id_usuario, id_libro):
        with self.conexion.cursor() as cursor:
            # Verificar el límite de libros prestados para el usuario
            cursor.execute("SELECT libros_prestados FROM Usuario WHERE ID_usuario = %s", (id_usuario,))
            libros_prestados = cursor.fetchone()

            if libros_prestados[0] < 3:
                # Actualizar el número de libros prestados para el usuario
                cursor.execute("UPDATE Usuario SET libros_prestados = libros_prestados + 1 WHERE ID_usuario = %s", (id_usuario,))

                # Restar una unidad del stock del libro
                cursor.execute("UPDATE libros SET Stock = Stock - 1 WHERE ID_libro = %s", (id_libro,))

                # Insertar el préstamo en la tabla Prestamos
                cursor.execute("INSERT INTO Prestamos (fecha_prestamo, ID_usuario, ID_libro) VALUES (NOW(), %s, %s)", (id_usuario, id_libro))

                # Confirmar la operación
                self.conexion.commit()
                print("Préstamo realizado con éxito.")
            else:
                print("El usuario ha alcanzado el límite de tres libros prestados.")

    def cerrar_conexion(self):
        self.conexion.close()


if __name__ == "__main__":
    sistema_biblioteca = SistemaBiblioteca("localhost", "root", "", "sistema_biblioteca")
    sistema_biblioteca.realizar_prestamo(1, 1)
    sistema_biblioteca.cerrar_conexion()
