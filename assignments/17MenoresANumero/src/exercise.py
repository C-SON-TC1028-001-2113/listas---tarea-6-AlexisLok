def matriz (): #Se define la funcon de creacion de matriz
    matrizSub = [] #Se define la variable con lista vacia

    #Se pide los parametros para construir matriz
    renglon = int(input(""))
    columna = int(input(""))
    for r in range(renglon): #Se crea un ciclo con otro ciclo dentro para construir la lista de listas (matriz)
        renglones = []
        for c in range(columna):
            valores = int(input(""))
            renglones.append(valores)
        matrizSub.append(renglones)
    return matrizSub #Regresa la matriz ya construida
    
def menor(): #Se define la funcion que analizara la matriz construida y pondra todos los valores menores de 10 en una lista
    MatrizMenor = []
    arreglo = matriz()
    for x in range(len(arreglo)): #Se crea un ciclo for con otro ciclo for para poder analizar cada valor de cada lista 
        for y in range(len(arreglo[0])):
            if arreglo[x][y] < 10: #Checa si el valor es menor a 10
                MatrizMenor.append(arreglo[x][y]) 
    return MatrizMenor #Regresa la matriz con solo valores menores a 10

def main():
    print(menor()) #Se imprime la matriz construida de valores menores a 10


if __name__=='__main__':
    main()
