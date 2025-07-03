import random

lista = [random.randint(1, 100) for _ in range(20)]
print("Lista generada:", lista)

while True:
    try: 
        numero_buscado = int(input("Ingrese el número a buscar: "))

        if numero_buscado in lista:
            posicion = lista.index(numero_buscado)
            print(f"Número encontrado en la posición: {posicion}")
        else:
            print("Número no encontrado")
        break
    except:
        print("Caracter invalido")