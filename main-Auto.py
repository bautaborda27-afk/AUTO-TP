from Clasesa import *

auto = Auto("toyota", "Etios", "2020")
def menu():
    print("1. Agregar conductor")
    print("2. Ver datos del auto")
    print("3. Ver conductores")
    print()
    opc = int(input("Opcion numerica: "))
    return opc

while True:
    opc = menu()
    if opc == 1:
        nombre = input("Nombre: ")
        edad = int(input("Edad: "))
        habilitado = input("Responde si estas habilitado con si o no: ")
        auto.crear_conductor(nombre, edad, habilitado)
    elif opc == 2:
        auto.get_info_auto()
    elif opc == 3:
        auto.get_conductores()
    else:
        break


