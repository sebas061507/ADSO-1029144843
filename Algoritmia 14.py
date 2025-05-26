while True:
    try:
        año = int(input("Ingrese un año: "))
        break
    except:
        print("Ingrese un valor valido")

if año % 4 == 0:
    if año % 100 == 0:
        if año % 400 == 0:
            print("Es un año bisiesto")
        else:
            print("No es un año bisiesto")
    else:
        print("Es un año bisiesto")
else:
    print("No es un año bisiesto")
