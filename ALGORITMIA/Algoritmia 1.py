
while True:
    try: 
        print(" ")
        N = int(input("Ingrese un número: "))

        suma = 0

        for i in range(1, N + 1):
            suma += i
        print(" ")
        print(f"La suma de 1 hasta {N} es {suma}")
        print(" ")
        break
    except:
        print("")
        print("Caracter invalido")
        print(" ")