from Lector import Lector as LEC
from MatrizDispersa import MatrizDispersa as MD

class Main:
    def __init__(self):
        self.Lector = LEC()
        self.Matriz = MD()
        contenido = self.Lector.leer_archivo("TxtPruebas/Matriz1(15x15).txt")
        if contenido:
            print(contenido)
        else:
            print("No se pudo leer el archivo.")

if __name__ == '__main__':
    main = Main()