def Representacion_csc(archivo):
    vals = [] 
    p_col = [0]  
    cols = []    
    cont = 0   
    try:
        matr = []
        with open(f"TxtPruebas/{archivo}", "r") as f:
            for linea in f:
                lin_compl = linea.lstrip()
                if not lin_compl or not lin_compl[0].isdigit():
                    continue 
                fila = list(map(int, linea.split()))
                matr.append(fila)
        num_fil = len(matr)
        num_col = len(matr[0]) if matr else 0
        for j in range(num_col): 
            for i in range(num_fil):  
                val = matr[i][j]
                if val != 0: 
                    vals.append(val) 
                    cols.append(i)   
                    cont += 1
            p_col.append(cont)
        return {"val": vals, "fil": cols,"p_col": p_col}
    except FileNotFoundError:
        print(f"Pailas algo fallo, :O")
        return None

def Apartir_csc(repre):
    max_col = len(repre["p_col"]) - 1
    print(max_col)
    max_fil = max(repre["fil"]) + 1
    matr = [[0 for _ in range(max_col)] for _ in range(max_fil)]
    
    for col in range(max_col):
        ini = repre["p_col"][col]  
        fin = repre["p_col"][col + 1] 
        for j in range(ini, fin):

            fila = repre["fil"][j]
            matr[fila][col] = repre["val"][j]
    return matr

def Obte(repre, i, j):
    ini = repre["p_col"][i]
    f = repre["p_col"][i+1]
    for tj in range(ini, f):
        print(tj)
        if repre["fil"][tj] == j:
            return repre["val"][tj]
    return 0

def Obtfila(repre, i):
    max_col = len(repre["p_col"]) - 1
    fils = [0] * max_col 
    for colm in range(max_col):
        inicio = repre["p_col"][colm]
        fin = repre["p_col"][colm + 1]
        for k in range(inicio, fin):
            if repre["fil"][k] == i:
                fils[colm] = repre["val"][k]
                break
    return fils

def ObtCol(repre, j):
    max_fil = max(repre["fil"]) + 1
    col = [0] * max_fil
    ini = repre["p_col"][j]
    f = repre["p_col"][j+1]
    for k in range(ini, f):
        fil = repre["fil"][k] 
        col[fil] = repre["val"][k] 
    return col

def Modele(repre, i, j, x):
    encontrado = False

    for idx in range(repre["p_col"][i], repre["p_col"][i + 1]):
        if repre["fil"][idx] == j:
            encontrado = True
            if x == 0:
                del repre["val"][idx]
                del repre["fil"][idx]
                for k in range(i + 1, len(repre["p_col"])):
                    repre["p_col"][k] -= 1  
            else:
                repre["val"][idx] = x
            break
    if not encontrado and x != 0:
        repre["val"].append(x)
        repre["fil"].append(j)
        for k in range(i + 1, len(repre["p_col"])):
            repre["p_col"][k] += 1  
        repre["p_col"].append(repre["p_col"][-1])  
  
def SumarMatricesCSC(matriz1, matriz2):
    resultado = {
        "val": [],
        "fil": [],
        "p_col": [0]
    }

    num_cols = max(len(matriz1["p_col"]), len(matriz2["p_col"])) - 1
    cont = 0

    for j in range(num_cols):
        col1_start = matriz1["p_col"][j] if j < len(matriz1["p_col"]) - 1 else 0
        col1_end = matriz1["p_col"][j + 1] if j + 1 < len(matriz1["p_col"]) else 0
        col2_start = matriz2["p_col"][j] if j < len(matriz2["p_col"]) - 1 else 0
        col2_end = matriz2["p_col"][j + 1] if j + 1 < len(matriz2["p_col"]) else 0

        col1_vals = {matriz1["fil"][i]: matriz1["val"][i] for i in range(col1_start, col1_end)}
        col2_vals = {matriz2["fil"][i]: matriz2["val"][i] for i in range(col2_start, col2_end)}

        all_rows = set(col1_vals.keys()).union(set(col2_vals.keys()))

        for row in sorted(all_rows):
            val = col1_vals.get(row, 0) + col2_vals.get(row, 0)
            if val != 0:
                resultado["val"].append(val)
                resultado["fil"].append(row)
                cont += 1

        resultado["p_col"].append(cont)

    return resultado


def TransponerCSC(matriz_csc):
    num_cols = len(matriz_csc["p_col"]) - 1
    num_filas = max(matriz_csc["fil"]) + 1 if matriz_csc["fil"] else 0

    transpuesta = {
        "val": [],
        "fil": [],
        "p_col": [0] * (num_filas + 1)
    }

    # Contar el número de elementos en cada fila de la matriz original
    for fila in matriz_csc["fil"]:
        transpuesta["p_col"][fila + 1] += 1

    # Convertir los conteos acumulados en punteros de columna
    for i in range(1, len(transpuesta["p_col"])):
        transpuesta["p_col"][i] += transpuesta["p_col"][i - 1]

    # Crear una lista temporal para almacenar los índices de inserción
    inserciones = transpuesta["p_col"][:]

    # Llenar los valores y las filas de la matriz transpuesta
    for col in range(num_cols):
        start = matriz_csc["p_col"][col]
        end = matriz_csc["p_col"][col + 1]
        for i in range(start, end):
            fila = matriz_csc["fil"][i]
            val = matriz_csc["val"][i]
            idx = inserciones[fila]
            transpuesta["val"].insert(idx, val)
            transpuesta["fil"].insert(idx, col)
            inserciones[fila] += 1

    return transpuesta


if __name__ == "__main__":
    archivo = "Matriz4(5x5).txt"
    matriz_csc = Representacion_csc(archivo)
    if matriz_csc:
        print("formato csc:")
        print("valores:", matriz_csc["val"])
        print("filas:", matriz_csc["fil"])
        print("p-columnas:", matriz_csc["p_col"])

        matriz_densa = Apartir_csc(matriz_csc)
        print("Matriz creada desde Csc:")
        for fila in matriz_densa:
            print(fila)

        elemento = Obte(matriz_csc, 0, 0) 
        print(f"Elemento: {elemento}")

        fila = Obtfila(matriz_csc, 0)
        print(f"Fila 1: {fila}")

        columna = ObtCol(matriz_csc, 1)
        print(f"Columna 2: {columna}")

        Modele(matriz_csc, 0, 0, 0)
        print("Matriz modificada:")
        print(matriz_csc)
        print("-------------------------"*5)
#Lo mas divertido de hacer esto es.....
    #Sumar matrices en formato CSC
    archivo1 = "Matriz1(15x15).txt"
    archivo2 = "Matriz2(15x15).txt"
    matriz_csc1 = Representacion_csc(archivo1)
    matriz_csc2 = Representacion_csc(archivo2)
    if matriz_csc1 and matriz_csc2:
        matriz_sumada = SumarMatricesCSC(matriz_csc1, matriz_csc2)
        print("Matriz sumada en formato CSC:")
        print("Valores:", matriz_sumada["val"])
        print("Filas:", matriz_sumada["fil"])
        print("Punteros de columna:", matriz_sumada["p_col"])

    matriz_transpuesta = TransponerCSC(matriz_sumada)
    print("Matriz transpuesta en formato CSR:")
    print("Valores:", matriz_transpuesta["valores"])
    print("Columnas:", matriz_transpuesta["columnas"])
    print("Punteros de fila:", matriz_transpuesta["filas"])

#[    ((0, 6), 3),    ((0, 9), 5),    ((1, 12), 8),
#     ((2, 14), 7),    ((3, 4), 7),    ((4, 8), 8),    ((4, 14), 6),    
# ((5, 7), 2),    ((6, 1), 4),    ((6, 13), 8),    ((8, 10), 4),    ((8, 11), 9), 
#    ((10, 5), 9),    ((10, 10), 6),    ((12, 12), 1),    ((13, 9), 2),    ((14, 2), 3)]