def Representacion_csr(archivo):
    vals = []
    p_fil = []
    cols = []
    cont = 0;
    
    try:
        #abrir el documento dentro de la carpeta "TxtPruebas y guardar datos
        with open(f"TxtPruebas/{archivo}", "r") as f:
            for i, linea in enumerate(f):
                #Verifica que no este vacia la linea, me mate horas pensando y buscando
                linea_compl = linea.lstrip()
                if not linea_compl or not linea_compl[0].isdigit():
                    #cuando algo esta vacio es mejor dejarlo atras y seguir :/
                    continue 
        
                fila = map(int, linea.split())
                p_fil.append(cont)
                for j, val in enumerate(fila):
                    if val != 0:  
                        vals.append(val)
                        cols.append(j)
                        cont += 1        
            p_fil.append(cont)
                        
        return {"valores": vals, "columnas": cols,"filas": p_fil}
    except FileNotFoundError:
        print(f"Error: pailasn bro no se encontro, deja la carrera ya")
        return None
    
def Apartir_csr(repre):
    max_fil = len(repre["filas"])-1
    max_col = max(repre["columnas"]) + 1
    matr = [[0 for _ in range(max_col)] for _ in range(max_fil)]
    for i in range(max_fil):
        ini = repre["filas"][i]
        fin = repre["filas"][i +1]
        for j in range(ini, fin):
            col = repre["columnas"][j]
            matr[i][col] = repre["valores"][j]
    return matr

def Obte(repre, i, j):
    ini = repre["filas"][i]
    f = repre["filas"][i+1]
    for tj in range(ini, f):
        print(tj)
        if repre["columnas"][tj] == j:
            return repre["valores"][tj]
    return 0

def Obtfila(repre, i):
    max_col = max(repre["columnas"]) + 1
    fil = [0] * max_col
    ini = repre["filas"][i]
    f = repre["filas"][i+1]
    for k in range(ini, f):
        col = repre["columnas"][k] 
        fil[col] = repre["valores"][k] 
    return fil

def ObtCol(repre, j):
    max_fila = len(repre["filas"]) - 1
    col = [0] * max_fila 
    
    for fila in range(max_fila):
        inicio = repre["filas"][fila]
        fin = repre["filas"][fila + 1]
        
        for k in range(inicio, fin):
            if repre["columnas"][k] == j:
                col[fila] = repre["valores"][k]
                break
    return col

def Modele(repre, i, j, x):
    encontrado = False
    for idx in range(repre["filas"][i], repre["filas"][i + 1]):
        if repre["columnas"][idx] == j:
            encontrado = True
            if x == 0: 
                del repre["valores"][idx]
                del repre["columnas"][idx]
                for k in range(i + 1, len(repre["filas"])):
                    repre["filas"][k] -= 1  
            else: 
                repre["valores"][idx] = x
            break
    if not encontrado and x != 0:
        repre["valores"].append(x)
        repre["columnas"].append(j)
        for k in range(i + 1, len(repre["filas"])):
            repre["filas"][k] += 1  
        repre["filas"].append(repre["filas"][-1])  

def SumarMatricesCSR(matriz1, matriz2):
    resultado = {
        "valores": [],
        "columnas": [],
        "filas": [0]
    }

    num_filas = max(len(matriz1["filas"]), len(matriz2["filas"])) - 1
    cont = 0

    for i in range(num_filas):
        fila1_start = matriz1["filas"][i] if i < len(matriz1["filas"]) - 1 else 0
        fila1_end = matriz1["filas"][i + 1] if i + 1 < len(matriz1["filas"]) else 0
        fila2_start = matriz2["filas"][i] if i < len(matriz2["filas"]) - 1 else 0
        fila2_end = matriz2["filas"][i + 1] if i + 1 < len(matriz2["filas"]) else 0

        fila1_vals = {matriz1["columnas"][j]: matriz1["valores"][j] for j in range(fila1_start, fila1_end)}
        fila2_vals = {matriz2["columnas"][j]: matriz2["valores"][j] for j in range(fila2_start, fila2_end)}

        all_cols = set(fila1_vals.keys()).union(set(fila2_vals.keys()))

        for col in sorted(all_cols):
            val = fila1_vals.get(col, 0) + fila2_vals.get(col, 0)
            if val != 0:
                resultado["valores"].append(val)
                resultado["columnas"].append(col)
                cont += 1

        resultado["filas"].append(cont)

    return resultado

def TransponerCSR(matriz_csr):
    num_filas = len(matriz_csr["filas"]) - 1
    num_columnas = max(matriz_csr["columnas"]) + 1 if matriz_csr["columnas"] else 0

    transpuesta = {
        "valores": [],
        "columnas": [],
        "filas": [0] * (num_columnas + 1)
    }

    # Contar el número de elementos en cada columna de la matriz original
    for col in matriz_csr["columnas"]:
        transpuesta["filas"][col + 1] += 1

    # Convertir los conteos acumulados en punteros de fila
    for i in range(1, len(transpuesta["filas"])):
        transpuesta["filas"][i] += transpuesta["filas"][i - 1]

    # Crear una lista temporal para almacenar los índices de inserción
    inserciones = transpuesta["filas"][:]

    # Llenar los valores y las columnas de la matriz transpuesta
    for fila in range(num_filas):
        start = matriz_csr["filas"][fila]
        end = matriz_csr["filas"][fila + 1]
        for i in range(start, end):
            col = matriz_csr["columnas"][i]
            val = matriz_csr["valores"][i]
            idx = inserciones[col]
            transpuesta["valores"].insert(idx, val)
            transpuesta["columnas"].insert(idx, fila)
            inserciones[col] += 1

    return transpuesta
#Yo pensaba que no tenia que pensar tanto, si mañana no estoy es porque me  mimi  por siempre

if __name__ == "__main__":
    archivo = "Matriz2(15x15).txt"
    matriz_csr = Representacion_csr(archivo)
    if matriz_csr:
        print("formato crs:")
        print("valores:", matriz_csr["valores"])
        print("columnas:", matriz_csr["columnas"])
        print("p-filas:", matriz_csr["filas"])

        matriz_densa = Apartir_csr(matriz_csr)
        print("Matriz creada desde csr:")
        for fila in matriz_densa:
            print(fila)
        
        elemento = Obte(matriz_csr, 1, 1) 
        print(f"Elemento: {elemento}")

        fila = Obtfila(matriz_csr, 1)
        print(f"Fila 1: {fila}")
        
        columna = ObtCol(matriz_csr, 2)
        print(f"Columna 2: {columna}")

        Modele(matriz_csr, 0, 0, 0)
        print("Matriz modificada:")
        print(matriz_csr)

#si lee esto profe, estoy cansado jefe ahora mas
#P.D despues de esto creo que soy un 25.99999% menos feliz que antes
#y un 19.99% mejor programador

    archivo1 = "Matriz1(15x15).txt"
    archivo2 = "Matriz2(15x15).txt"
    matriz_csr1 = Representacion_csr(archivo1)
    matriz_csr2 = Representacion_csr(archivo2)

    if matriz_csr1 and matriz_csr2:
        matriz_sumada = SumarMatricesCSR(matriz_csr1, matriz_csr2)
        print("Matriz sumada en formato CSR:")
        print("Valores:", matriz_sumada["valores"])
        print("Columnas:", matriz_sumada["columnas"])
        print("Punteros de fila:", matriz_sumada["filas"])

    matriz_transpuesta = TransponerCSR(matriz_sumada)
    print("Matriz transpuesta en formato CSR:")
    print("Valores:", matriz_transpuesta["valores"])
    print("Columnas:", matriz_transpuesta["columnas"])
    print("Punteros de fila:", matriz_transpuesta["filas"])
#[    ((0, 6), 3),    ((0, 9), 5),    ((1, 12), 8),
#     ((2, 14), 7),    ((3, 4), 7),    ((4, 8), 8),    ((4, 14), 6),    
# ((5, 7), 2),    ((6, 1), 4),    ((6, 13), 8),    ((8, 10), 4),    ((8, 11), 9), 
#    ((10, 5), 9),    ((10, 10), 6),    ((12, 12), 1),    ((13, 9), 2),    ((14, 2), 3)]