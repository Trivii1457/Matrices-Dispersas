
class Lector:
    def leer_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'r') as archivo:
                contenido = archivo.read()
                return contenido
        except FileNotFoundError:
            print(f"El archivo {nombre_archivo} no se encontró.")
            return None
    