def analizar_texto():
    texto = input("Ingrese un texto: ")

    palabras = texto.split()

    cantidad_palabras = len(palabras)

    if palabras:
        palabra_mas_larga = max(palabras, key=len)
        longitud_maxima = len(palabra_mas_larga)
    else:
        longitud_maxima = 0

    print(f"\nNúmero de palabras: {cantidad_palabras}")
    print(f"Tamaño de la palabra más larga: {longitud_maxima}")

analizar_texto()
