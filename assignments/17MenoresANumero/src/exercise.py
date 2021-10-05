def matriz (renglon, column):
    renglones = []
    for r in range(renglon):
        columnas = []
        for c in range(column):
            valores = int(input(" "))
            columnas.append(valores)
        renglones.append(columnas)
    return (renglones)

def matrizAux():
    r = int(input(""))
    c = int(input(""))
    m = matriz (r,c) 
    return m

def main():




if __name__=='__main__':
    main()
