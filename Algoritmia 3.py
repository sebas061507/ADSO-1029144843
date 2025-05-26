#suma pares
def sumarPares(inicio, fin):
    
    if inicio > fin:
        inicio, fin = fin, inicio 

    suma = 0
    for i in range(inicio, fin + 1, 2):
        suma += i

    return suma
while True:
    try:
        print("")
        inicio = int(input("Ingrese el número inicial: "))
        print("")
        fin = int(input("Ingrese el número final: "))
        print("")
        print("La suma de los pares es:", sumarPares(inicio, fin))
        break
    except:
        print("")
        print("Caracter invalido")
