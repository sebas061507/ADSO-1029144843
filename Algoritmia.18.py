def calcular_letra_nit(nit):
    letras_control = ['T', 'R', 'W', 'A', 'G', 'M', 'Y', 'F', 'P', 'D', 'X', 'B',
        'N', 'J', 'Z', 'S', 'Q', 'V', 'H', 'L', 'C', 'K', 'E']
    
    try:
        nit_num = int(nit)
    except ValueError:
        return "\nError: El NIT debe ser un número."

    resto = nit_num % 23

    letra = letras_control[resto]

    return letra

nit = input("\nIntroduce el NIT: ")
letra_control = calcular_letra_nit(nit)
print(f"\nLa letra de control para el NIT {nit} es: {letra_control}\n")
