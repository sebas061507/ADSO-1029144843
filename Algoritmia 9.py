import random

lista = [random.randint(1, 100) for _ in range(20)]
print("Lista generada:", lista)

suma = sum(lista)
can = len(lista)
media = suma / can


print(f"La media de los números en la lista es: {media}")
