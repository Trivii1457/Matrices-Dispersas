import random
import os

def gen_mat_dis(M, N, dens=0.1):
    matriz = []
    for i in range(M):
        fila = []
        for j in range(N):
            if random.random() < dens:
                valor = random.randint(1, 10)
            else:
                valor = 0
            fila.append(valor)
        matriz.append(fila)
    return matriz

def guar_matr_en_arch(matriz, archivo):

    if not os.path.exists("TxtPruebas"):
        os.makedirs("TxtPruebas")

    with open(f"TxtPruebas/{archivo}", 'w') as f:
        for fila in matriz:
            f.write(" ".join(map(str, fila)) + "\n")


if __name__ == "__main__":
    M = 200
    N = 200
    dens = 0.05

    matriz = gen_mat_dis(M, N, dens)
    
    archivo = "matriz3(200x200).txt"
    guar_matr_en_arch(matriz, archivo)

