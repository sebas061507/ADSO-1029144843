import random
tam = 10
matriz = [[random.randint(10,99) for i in range(tam)] for j in range(tam)]
print("\n-----------MATRIZ----------")
for fila in matriz:
    print(fila)

print("\n-DIAGONAL PRINCIPAL-")
for i in range(tam):
        print(f"[{'  ' * i}{matriz[i][i]}{'  ' * (tam - i - 1)}]")

print("\n-----DIAGONAL INVERSA-----")
for i in range(tam):
        print(f"[{'  ' * (tam - i - 1)}{matriz[i][i]}{'  ' * i}]")

print("\n--------DIAGONAL INFERIOR IZQUIERDA-------")
for i in range(tam):
    print('[' , end="")
    for j in range(i + 1):
        print(f"{matriz[j][i]}, ", end="")
    print('    ' * (tam - i - 1) + ']')

print("\n---------MATRIZ INFERIOR DERECHA----------")
for i in range(tam):
    print('[' + '    ' * (tam - i - 1), end="")
    for j in range(tam - i - 1, tam):
        print(f"{matriz[i][j]}", end=", ")
    print(']')


print("\n---------MATRIZ SUPERIOR DERECHA----------")
for i in range(tam):
    print('[' + '    ' * i , end="")
    for j in range(i, tam):
        print(f"{matriz[i][j]}", end=", ")
    print(']')

print("\n--------MATRIZ SUPERIOR IZQUIERDA---------")
for i in range(tam):
    print('[', end="")
    for j in range(tam - i):
        print(f"{matriz[i][j]}", end=", ")
    print('    ' * i + ']')
