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
        return {"val": vals, "p_col": p_col, "fil": cols}
    except FileNotFoundError:
        print(f"Pailas algo fallo, :O")
        return None

if __name__ == "__main__":
    archivo = "Matriz4(5x5).txt"
    matriz_csc = Representacion_csc(archivo)
    if matriz_csc:
        print("formato csc:")
        print("valores:", matriz_csc["val"])
        print("filas:", matriz_csc["fil"])
        print("p-columnas:", matriz_csc["p_col"])
#Lo mas divertido de hacer esto es.....