import random

def generar_codigo():
    return random.sample(range(10), 4)  

def evaluar_intento(codigo, intento):
    pista = []
    for i in range(4):
        if intento[i] == codigo[i]:
            pista.append("Verde")
        elif intento[i] in codigo:
            pista.append("Amarillo")
        else:
            pista.append("Rojo")
    return pista

def jugar():
    print("🔢 Bienvenido al juego Rojo-Amarillo-Verde")
    codigo = generar_codigo()
    intentos = 0

    while True:
        entrada = input("Introduce 4 dígitos distintos (ej. 1234): ")
        if len(entrada) != 4 or not entrada.isdigit():
            print("Entrada no válida. Debes ingresar 4 dígitos.")
            continue

        intento = [int(d) for d in entrada]
        if len(set(intento)) != 4:
            print("Los dígitos deben ser distintos.")
            continue

        intentos += 1
        pista = evaluar_intento(codigo, intento)

        print("Intento:", intentos)
        print("Pista:  ", pista)

        if pista == ["Verde"] * 4:
            print(f"\n🎉 ¡Has acertado en {intentos} intento(s)!")
            break


jugar()