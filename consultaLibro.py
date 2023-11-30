import mysql.connector
from tabulate import tabulate

class BibliotecaManager:
    def __init__(self):
        self.conexion = mysql.connector.connect(host="localhost", user="root", password="", database="sistema_biblioteca")

    def consultar_stock(self):
        with self.conexion.cursor() as cursor:
            cursor.execute("SELECT ID_libro, Nombre, Stock FROM libros")
            stock_libros = cursor.fetchall()

            if stock_libros:
                headers = ["ID Libro", "Nombre", "Stock"]
                print("Stock actual de libros:")
                print(tabulate(stock_libros, headers=headers, tablefmt="grid"))
            else:
                print("No hay libros registrados en la base de datos.")

    def buscar_stock_por_id(self, id_libro):
        with self.conexion.cursor() as cursor:
            cursor.execute("SELECT ID_libro, Nombre, Stock FROM libros WHERE ID_libro = %s", (id_libro,))
            libro = cursor.fetchone()

            if libro:
                headers = ["ID Libro", "Nombre", "Stock"]
                print(f"Stock del libro con ID {id_libro}:")
                print(tabulate([libro], headers=headers, tablefmt="grid"))
            else:
                print(f"No se encontró ningún libro con ID {id_libro}.")

    def cerrar_conexion(self):
        self.conexion.close()

# Uso de la clase BibliotecaManager
biblioteca_manager = BibliotecaManager()

# Consultar el stock actual
biblioteca_manager.consultar_stock()

# Buscar el stock de un libro por ID
id_libro_a_buscar = 0
biblioteca_manager.buscar_stock_por_id(id_libro_a_buscar)

# Cerrar la conexión
biblioteca_manager.cerrar_conexion()
