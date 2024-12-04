def Representacion_coo(archivo):
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
                        
        return {"valores": vals, "filas": p_fil, "columnas": cols}
    except FileNotFoundError:
        print(f"Error: pailasn bro no se encontro, deja la carrera ya")
        return None

if __name__ == "__main__":
    archivo = "Matriz4(5x5).txt"
    matriz_coo = Representacion_coo(archivo)
    if matriz_coo:
        print("formato crs:")
        print("Valores:", matriz_coo["valores"])
        print("Columnas:", matriz_coo["columnas"])
        print("Filas:", matriz_coo["filas"])

#si lee esto profe, estoy cansado jefe ahora mas
#P.D despues de esto creo que soy un 25.99999% menos feliz que antes
#y un 19.99% mejor programador