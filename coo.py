def Representacion_coo(archivo):
    vals = []
    fil = []
    cols = []
    try:
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
    
def Apartir_COO(repre):
    max_fil = max(repre["filas"])+1
    max_col = max(repre["columnas"]) + 1
    matr = [[0 for _ in range(max_col)] for _ in range(max_fil)]
    for valor, i, j in zip(repre["valores"], repre["filas"], repre["columnas"]):
        matr[i][j] = valor
    return matr

def Obte(repre, i, j):
    for val, fila, col in zip(repre["valores"], repre["filas"], repre["columnas"]):
        if fila == i and col == j:
            return val 
    return 0 

def Obtfila(repre, i):
    max_col = max(repre["columnas"]) + 1
    fil = [0] * max_col
    for val, fil_act, col in zip(repre["valores"], repre["filas"], repre["columnas"]):
        if fil_act == i:
            print(val)
            print(fil_act)
            print(col)
            fil[col] = val
    return fil

def ObtCol(repre, j):
    max_fila = max(repre["filas"]) + 1
    col = [0] * max_fila 
    for valor, fila, col_actual in zip(repre["valores"], repre["filas"], repre["columnas"]):
        if col_actual == j:
            col[fila] = valor
    return col

def Modele(repre, i, j, x):
    encontrado = False
    for idx, (fil, col) in enumerate(zip(repre["filas"], repre["columnas"])):
        if fil == i and col == j:
            encontrado = True
            if x == 0: 
                del repre["valores"][idx]
                del repre["filas"][idx]
                del repre["columnas"][idx]
            else:
                repre["valores"][idx] = x
            break
    if not encontrado and x != 0:
        repre["valores"].append(x)
        repre["filas"].append(i)
        repre["columnas"].append(j)

if __name__ == "__main__":
    archivo = "Matriz5(6x6).txt"
    matriz_coo = Representacion_coo(archivo)
    if matriz_coo:
        #Representacion
        print("formato COO:")
        print("Valores:", matriz_coo["valores"])
        print("Filas:", matriz_coo["filas"])
        print("Columnas:", matriz_coo["columnas"])
        #Crear
        matriz_densa = Apartir_COO(matriz_coo)
        print("Matriz creada desde COO:")
        for fila in matriz_densa:
            print(fila)
        #Buscar
        elemento = Obte(matriz_coo, 0, 9) 
        print(f"Elemento en (0,9): {elemento}")
        #Obtener Fila
        fila = Obtfila(matriz_coo, 3)
        print(f"Fila 1: {fila}")
        #obtener Colmuna
        columna = ObtCol(matriz_coo, 2)
        print(f"Columna 2: {columna}")
        #Modificar Elemento
        Modele(matriz_coo, 0, 0, 2)
        print("Matriz modificada:")
        print(matriz_coo)
#si lee esto profe, estoy cansado jefe