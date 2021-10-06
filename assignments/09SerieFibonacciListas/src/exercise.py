def main():
    #Se definen las variables para la secuencia de Fibonacci
    res = 0
    num1 = 0
    num2 = 1
    n = -1 #Se define una variable para la captura segura del número de dator
    fib = [] #Se define la lista vacia para guardar los números de Fibonacci
    #Se crea un ciclo para asegurarse que el número ingresado sea igual o mayor a 0
    while n < 0:
        n = int(input(""))
    
    #Se crea un ciclo para agregar los números en la lista
    for x in range(n):
        fib.append(res)
        num1 = num2 
        num2 = res
        res = num1 + num2
    print(fib) 

if __name__=='__main__':
    main()
