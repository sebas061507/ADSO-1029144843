from random import randint

# Crear la matriz de 10x10 con números entre 10 y 99
matriz = [[randint(10, 99) for _ in range(10)] for _ in range(10)]
i = 0
for valor in i:
    print(i, valor)
    i += 1
    for i in range(10):


# Definir partes de la cuadrícula
a = "┌" + "───┬" * 9 + "───┐"
b = "├" + "───┼" * 9 + "───┤"
c = "└" + "───┴" * 9 + "───┘"

# Imprimir la matriz con la cuadrícula
print(a)
for i in range(10):
    row = "│" + "│".join(f"{num:3}" for num in matriz[i]) + "│"
    print(row)
    if i < 9:
        print(b)
print(c)
