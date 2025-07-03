numeros = []
for i in range(5):
    numero = int(input(f"Número {i+1}: "))
    numeros.append(numero)

numeros.sort(reverse=True)

print("Números ordenados de mayor a menor:")
for num in numeros:
    print(num)
