while True:
    try:
        valor = int(input("Ingrese el valor a cobrar: "))
        monto = int(input("Ingrese el monto entregado: "))
        break
    except:
        print("Ingrese un digito valido")
cambio = monto - valor

if cambio < 0:
    print("Monto insuficiente")
else:
    monedas = [1000, 500, 200, 100, 50]
    print("Cambio a entregar:")
    for moneda in monedas:
        cantidad = cambio // moneda
        cambio = cambio % moneda
        if cantidad > 0:
            print(f"{cantidad} moneda(s) de {moneda}")
