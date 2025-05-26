def contar_digitos(numero):
    numero = abs(numero)  
    return len(str(numero))

while True:
    try:
        num = int(input("\nIntroduce un número entero: \n"))
        digitos = contar_digitos(num)
        print(f"\nEl número {num} tiene {digitos} dígito(s).\n")
        break
    except:
        print("\nCaracter invalido, introduce un numero entero  \n")
