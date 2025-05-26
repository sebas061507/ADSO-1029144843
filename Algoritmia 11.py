import random

lista = [random.randint(1, 100) for _ in range(20)]
print("Lista original: ", lista)

lista_inversa = []
i = len(lista) - 1
while i >= 0:
    lista_inversa.append(lista[i])
    i -= 1
print("Lista inversa:  ", lista_inversa)
