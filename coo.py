def Representacion_coo(archivo):
    vals = []
    fil = []
    cols = []
    #arrays para la matrix
    
    try:
        #abrir el documento dentro de la carpeta "TxtPruebas y guardar datos
        with open(f"TxtPruebas/{archivo}", "r") as f:
            for i, linea in enumerate(f):
                fila = map(int, linea.split())
            
                for j, val in enumerate(fila):
                    if val != 0:  
                        vals.append(val)
                        fil.append(i)
                        cols.append(j)
        
        return {"valores": vals, "filas": fil, "columnas": cols}
    except FileNotFoundError:
        print(f"Error: pailasn bro no se encontro, deja la carrera ya")
        return None

if __name__ == "__main__":
    archivo = "Matriz1(15x15).txt"
    matriz_coo = Representacion_coo(archivo)
    if matriz_coo:
        print("formato COO:")
        print("Valores:", matriz_coo["valores"])
        print("Filas:", matriz_coo["filas"])
        print("Columnas:", matriz_coo["columnas"])
#si lee esto profe, estoy cansado jefe