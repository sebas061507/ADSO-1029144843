from random import randint

# Crear la matriz de 10x10 con números entre 10 y 99
matriz = [[randint(10, 99) for _ in range(10)] for _ in range(10)]

# Definir partes de la cuadrícula
top_border =    "┌" + "───┬" * 9 + "───┐"
middle_border = "├" + "───┼" * 9 + "───┤"
bottom_border = "└" + "───┴" * 9 + "───┘"

# Imprimir la matriz con la cuadrícula
print(top_border)
for i in range(10):
    row = "│" + "│".join(f"{num:3}" for num in matriz[i]) + "│"
    print(row)
    if i < 9:
        print(middle_border)
print(bottom_border)
