import random

def IngresarOpcion ():
    #*****PROGRAMA PRINCIPAL**********
    while True:
        print("\n----MENU PRINCIPAL----")
        print("\n1: Buscar numero")
        print("\n2: Buscar numero mayor y menor")
        print("\n3: Verificar si el numero leido aparece mas veces que el mayor")
        print("\n4: Calcula la media de todos los numero")
        print("\n5: Calcula la media entre el numero mayor y el menor")
        print("\n6: Invierte toda la lista")
        print("\n0: Terminar...\n")
        try:
            opcion = int(input("\nIngrese la opción: "))
            if opcion >= 0 and opcion < 6:
                break
            else:
                print("\nOpcion no valida")
        except:
            print("\nOpcion no valida")

    return opcion

def encontrarNum ():
    while True:
        lista = [random.randint(1, 100) for _ in range(20)]
        print("\nLista generada:", lista)

        while True:
            entrada = input("\nIngrese el número a buscar: ")
            if entrada.isdigit():
                numeroB = int(entrada)
                if numeroB in lista:
                    posicion = lista.index(numeroB)
                    print(f"\nNúmero encontrado en la posición: {posicion}")
                else:
                    print("\nNúmero no encontrado en la lista.")
                break
            else:
                print("\nEntrada inválida. Ingrese solo números enteros.")
        break

def orderMax ():
    lista = [random.randint(1, 100) for _ in range(20)]
    print("\nLista generada:", lista)
    numeroM = max(lista)
    posiciones = [i for i, num in enumerate(lista) if num == numeroM]
    cantidad = len(posiciones)
    print(f"\nEl número mayor es {numeroM}, aparece {cantidad} veces en las posiciones: {posiciones}")

def value ():
    lista = [random.randint(1, 100) for _ in range(20)]
    print("\nLista generada:", lista)
    numeroL = int(input("\nIntroduce un número a verificar: "))
    numeroM = max(lista)
    vecesL = len(numeroL)
    vecesM = len(numeroM)
    resultado = vecesL > vecesM
    print(f"\n¿El número {numeroL} aparece más veces que el mayor ({numeroM})?: {resultado}")

def promedio ():
    lista = [random.randint(1, 100) for _ in range(20)]
    print("\nLista generada:", lista)
    suma = sum(lista)
    can = len(lista)
    media = suma / can
    print(f"\nLa media de los números en la lista es: {media}")

def promMax ():
    lista = [random.randint(1, 100) for _ in range(20)]
    print("\nLista generada:", lista)
    mayor = max(lista)
    menor = min(lista)
    media_extremos = (mayor + menor) / 2
    print(f"\nEl número mayor es: {mayor}")
    print(f"\nEl número menor es: {menor}")
    print(f"\nLa media entre el mayor y el menor es: {media_extremos}")

def inversa ():
    lista = [random.randint(1, 100) for _ in range(20)]
    print("\nLista original: ", lista)

    lista_inversa = []
    i = len(lista) - 1
    while i >= 0:
        lista_inversa.append(lista[i])
        i -= 1
    print("\nLista inversa:  ", lista_inversa)

while True:
    try:
        Opc = IngresarOpcion ()
        if Opc == 0:
            print("\nPrograma terminado! \n")
            break
        else:
            if Opc == 1:
                encontrarNum()
            elif Opc == 2:
                orderMax ()
            elif Opc == 3:
                value ()
            elif Opc == 4:
                promedio ()
            elif Opc == 5:
                promMax ()
            elif Opc == 6:
                inversa ()
    except:
        print("\nCaracter / opcion invalida")