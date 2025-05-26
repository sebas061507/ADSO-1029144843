print("")

while True: 
    try:
        numero = int(input("Ingrese un número: "))
        
        if numero % 2 == 0:
            print("")
            print("El número es par.")
            print("")
        else:
            print("")
            print("El número es impar.")
            print("")
        break
    except:
        print(" ")
        print("Caracter invalido")