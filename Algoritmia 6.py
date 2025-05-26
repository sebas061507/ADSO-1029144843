import random

lista = [random.randint(1, 100) for _ in range(20)]
print("Lista generada:", lista)

while True:
    try:
        numeroB = int(input("Introduce un número a buscar en la lista: "))
        cantidad = len(numeroB)

        if cantidad > 0:
            print(f"El número {numeroB} aparece {cantidad} veces en la lista.")
        else:
            print("El número no se encuentra en la lista.")
        break
    except:
        print("Caracter invalido")