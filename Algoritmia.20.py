def calcular_hipoteca():
    capital = float(input("\nIntroduce el capital del préstamo (USD $): "))
    interes_anual = float(input("\nIntroduce el interés anual (%): "))
    anios = int(input("\nIntroduce el número de años: "))

    R = interes_anual / 100 / 12
    N = anios * 12

    if R == 0:
        cuota_mensual = capital / N
    else:
        cuota_mensual = capital * (R * (1 + R) ** N) / ((1 + R) ** N - 1)

    total_a_pagar = cuota_mensual * N

    print(f"\nCuota mensual: {cuota_mensual:.2f} USD $")
    print(f"\nTotal a pagar al final del préstamo: {total_a_pagar:.2f} USD $\n")

calcular_hipoteca()
