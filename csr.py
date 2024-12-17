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