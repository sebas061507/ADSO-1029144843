import random

def IngresarOpcion():
    while True:
        print("\n---- MENU PRINCIPAL ----\n")
        print("\n 1: Buscar número")
        print("\n 2: Buscar número mayor y menor")
        print("\n 3: Verificar si el número leído aparece más veces que el mayor")
        print("\n 4: Calcular la media de todos los números")
        print("\n 5: Calcular la media entre el número mayor y el menor")
        print("\n 6: Invertir toda la lista")
        print("\n 0: Terminar ")

        try:
            opcion = int(input("\n Ingrese la opción: "))
            if 0 <= opcion <= 6:
                return opcion
            else:
                print("Opción no válida.")
        except ValueError:
            print("Entrada inválida. Ingrese un número del 0 al 6.")

# Se genera una sola lista para usarla en todas las funciones
lista_global = [random.randint(1, 100) for _ in range(20)]

def encontrarNum():
    print("\nLista generada:", lista_global)
    while True:
        entrada = input("\nIngrese el número a buscar: ")
        print("")
        if entrada.isdigit():
            numeroB = int(entrada)
            if numeroB in lista_global:
                posiciones = [i for i, val in enumerate(lista_global) if val == numeroB]
                print(f"\nNúmero encontrado en las posiciones: {posiciones}")
            else:
                print("\nNúmero no encontrado en la lista.")
            break
        else:
            print("\nEntrada inválida. Ingrese solo números enteros.")

def orderMax():
    print("\nLista generada:", lista_global)
    numeroM = max(lista_global)
    posiciones = [i for i, num in enumerate(lista_global) if num == numeroM]
    cantidad = len(posiciones)
    print(f"\nEl número mayor es {numeroM}, aparece {cantidad} veces en las posiciones: {posiciones}")

def value():
    print("\nLista generada:", lista_global)
    try:
        numeroL = int(input("\nIntroduce un número a verificar: "))
        numeroM = max(lista_global)
        vecesL = lista_global.count(numeroL)
        vecesM = lista_global.count(numeroM)
        resultado = vecesL > vecesM
        print(f"\n¿El número {numeroL} aparece más veces que el mayor ({numeroM})?: {resultado}")
    except ValueError:
        print("\nEntrada inválida. Ingrese un número entero.")

def promedio():
    print("\nLista generada:", lista_global)
    media = sum(lista_global) / len(lista_global)
    print(f"\nLa media de los números en la lista es: {media:.2f}")

def promMax():
    print("\nLista generada:", lista_global)
    mayor = max(lista_global)
    menor = min(lista_global)
    media_extremos = (mayor + menor) / 2
    print(f"\nEl número mayor es: {mayor}")
    print(f"\nEl número menor es: {menor}")
    print(f"\nLa media entre el mayor y el menor es: {media_extremos:.2f}")

def inversa():
    print("\nLista original: ", lista_global)
    lista_inversa = lista_global[::-1]
    print("\nLista inversa:  ", lista_inversa)

# ----- PROGRAMA PRINCIPAL -----
while True:
    opcion = IngresarOpcion()
    if opcion == 0:
        print("\nPrograma terminado!")
        break
    elif opcion == 1:
        encontrarNum()
    elif opcion == 2:
        orderMax()
    elif opcion == 3:
        value()
    elif opcion == 4:
        promedio()
    elif opcion == 5:
        promMax()
    elif opcion == 6:
        inversa()
