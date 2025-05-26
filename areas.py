#calcular vlumen del cubo**************************************
import math


#**********Calcular volumen cubico**************
def CalcularCubo():
    lado = IngresarNumero ("Ingresar lado: ")
    print("           ")
    print (f"El volumen del cubo es {pow(lado, 3)}")

#**********Calcular volumen cilindrico**********

def CalcularVolumenCil():
    r = IngresarNumero ("Ingresa el radio: ")
    print("      ")
    h = IngresarNumero ("Ingresa la altura: ")
    print("           ")
    print (f" El volumen del cilindro es { math.pi * r**2 * h}")

#***********Calcular Area Triangular*************
def CalcularAreaTri():
    b = IngresarNumero("Ingresar la base: ")
    print("           ")
    h = IngresarNumero("Ingresar la altura: ")
    print("           ")
    print (f"El area del triangulo es: {b * h / 2}")

#**********Calcular Area Rectangular**********
def CalcularAreaRect():
    a = IngresarNumero("Ingresar Base: ")
    print("           ")
    h = IngresarNumero("Ingresar Altura: ")
    print("           ")
    print (f" El area del Rectangulo es: {a * h}")
#Menu options

def IngresarNumero(mensaje):#*****PROGRAMA PRINCIPAL**********#
    while True:
        try:
            num = int(input(mensaje))
            break
        except:
                print("     ")
                print("Caracter invalido")
        
    return num


def IngresarOpcion():#*****PROGRAMA PRINCIPAL**********
    while True:
        print("     ")
        print("----MENU PRINCIPAL----")
        print("           ")
        print("1: Volumen del cubo")
        print("2: Volumen del cilindro")
        print("3: Area del triangulo")
        print("4: Area del rectangulo")
        print("0: Terminar...")
        print("     ")
        try:
            opcion = int(input("Ingrese la opción: "))
            if opcion >= 0 and opcion < 5:
                break
            else:
                print("           ")
                print("Opcion no valida")
        except:
            print("           ")
            print("Opcion no valida")

    return opcion

while True:
    opc =IngresarOpcion()
    print ()
    if opc == 0:
        break
    else:
        #pedir operandos
        if opc == 1:
            CalcularCubo()
        elif opc == 2:
            CalcularVolumenCil()
        elif opc == 3:
            CalcularAreaTri( )
        elif opc == 4:
            CalcularAreaRect()




print("Programa terminado!")