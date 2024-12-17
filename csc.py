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
        
#Lo mas divertido de hacer esto es.....