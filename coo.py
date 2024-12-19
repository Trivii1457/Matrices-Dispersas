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

def SumarMatricesCOO(matriz1, matriz2):
    resultado = {
        "valores": [],
        "filas": [],
        "columnas": []
    }

    # Agregar todos los elementos de la primera matriz al resultado
    for val, fila, col in zip(matriz1["valores"], matriz1["filas"], matriz1["columnas"]):
        resultado["valores"].append(val)
        resultado["filas"].append(fila)
        resultado["columnas"].append(col)

    # Agregar los elementos de la segunda matriz al resultado
    for val, fila, col in zip(matriz2["valores"], matriz2["filas"], matriz2["columnas"]):
        encontrado = False
        for idx, (res_fila, res_col) in enumerate(zip(resultado["filas"], resultado["columnas"])):
            if res_fila == fila and res_col == col:
                resultado["valores"][idx] += val
                encontrado = True
                break
        if not encontrado:
            resultado["valores"].append(val)
            resultado["filas"].append(fila)
            resultado["columnas"].append(col)

    return resultado

def TransponerCOO(matriz_coo):
    transpuesta = {
        "valores": matriz_coo["valores"],
        "filas": matriz_coo["columnas"],
        "columnas": matriz_coo["filas"]
    }
    return transpuesta


if __name__ == "__main__":
    archivo = "Matriz2(15x15).txt"
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
        print("--------------------*"*5)
        #si lee esto profe, estoy cansado jefe 
        #*****************************************************************************************
        #Sumar matrices
        matriz1 = Representacion_coo("Matriz1(15x15).txt")
        matriz2 = Representacion_coo("Matriz2(15x15).txt")
        if matriz1 and matriz2:
            resultado = SumarMatricesCOO(matriz1, matriz2)
            print("Matriz sumada en formato COO:")
            print("Valores:", resultado["valores"])
            print("Filas:", resultado["filas"])
            print("Columnas:", resultado["columnas"])

        matriz_transpuesta = TransponerCOO(resultado)
        print("Matriz transpuesta en formato COO:")
        print("Valores:", matriz_transpuesta["valores"])
        print("Filas:", matriz_transpuesta["filas"])
        print("Columnas:", matriz_transpuesta["columnas"])

#[    ((0, 6), 3),    ((0, 9), 5),    ((1, 12), 8),
#     ((2, 14), 7),    ((3, 4), 7),    ((4, 8), 8),    ((4, 14), 6),    
# ((5, 7), 2),    ((6, 1), 4),    ((6, 13), 8),    ((8, 10), 4),    ((8, 11), 9), 
#    ((10, 5), 9),    ((10, 10), 6),    ((12, 12), 1),    ((13, 9), 2),    ((14, 2), 3)]
