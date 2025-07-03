import random

def generar_codigo():
    return random.sample(range(10), 4)

def evaluar_intento(codigo, intento):
    verde = amarillo = rojo = 0

    for i in range(4):
        if intento[i] == codigo[i]:
            verde += 1
        elif intento[i] in codigo:
            amarillo += 1
        else:
            rojo += 1

    return verde, amarillo, rojo

def jugar():
    print("🔐 Bienvenido al modo difícil del juego Rojo-Amarillo-Verde")
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
        verde, amarillo, rojo = evaluar_intento(codigo, intento)

        print(f"Intento {intentos}: ")
        print(f"Pista: {verde} Verde(s), {amarillo} Amarillo(s), {rojo} Rojo(s)")

        if verde == 4:
            print(f"\n🎉 ¡Has acertado el código {codigo} en {intentos} intento(s)!")
            break


jugar()
