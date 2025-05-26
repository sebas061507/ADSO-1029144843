import random

lista = [random.randint(1, 100) for _ in range(20)]
print("Lista generada:", lista)

numeroM = max(lista)

posiciones = [i for i, num in enumerate(lista) if num == numeroM]
cantidad = len(posiciones)

print(f"El número mayor es {numeroM}, aparece {cantidad} veces en las posiciones: {posiciones}")