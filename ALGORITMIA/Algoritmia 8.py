import random

lista = [random.randint(1, 100) for _ in range(20)]
print("Lista generada:", lista)

numeroL = int(input("Introduce un número a verificar: "))

numeroM = max(lista)

vecesL = len(numeroL)
vecesM = len(numeroM)

resultado = vecesL > vecesM
print(f"¿El número {numeroL} aparece más veces que el mayor ({numeroM})?: {resultado}")