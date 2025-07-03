
aprendices = [
    "\nAlvarez", "\nBenítez", "\nCárdenas", "\nDíaz", "\nEscobar",
    "\nGómez", "\nLópez", "\nMartínez", "\nRamírez", "\nZapata"
]

print("\nLista original de aprendices:")
for apellido in aprendices:
    print(apellido)

nuevo_aprendiz = input("\nIngrese el apellido del nuevo aprendiz: ")

aprendices.append(nuevo_aprendiz)
aprendices.sort()

print("\nLista actualizada de aprendices:")
for apellido in aprendices:
    print(apellido)
