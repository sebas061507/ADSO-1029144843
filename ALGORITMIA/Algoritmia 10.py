import random

lista = [random.randint(1, 100) for _ in range(20)]
print("Lista generada:", lista)


mayor = max(lista)
menor = min(lista)

media_extremos = (mayor + menor) / 2

print(f"El número mayor es: {mayor}")
print(f"El número menor es: {menor}")
print(f"La media entre el mayor y el menor es: {media_extremos}")
