saldo = 1000
# Función de consultar saldo
def consultar_saldo(saldo):
    print("Su saldo es: ", saldo)
    input("Presione enter para continuar. ")
    return saldo
# Función de depositar dinero
def depositar(saldo):
    monto = float(input("Ingrese el monto a depositar: "))
    if monto > 0:
        saldo += monto
        print("Deposito exitoso.")
        print("Nuevo saldo: ", saldo)
    else:
        print("El monto debe ser mayor a cero")
        print("Su saldo es: ", saldo)
    input("Presione enter para continuar. ")
    return saldo
    
# Función de retirar dinero
def retirar(saldo):
    retiro = float(input("Ingrese el monto a retirar: "))
    if retiro <= 0:
        print("Error, el monto debe ser mayor a cero.")
    elif retiro > saldo:
        print("Fondos insuficientes.")
        print(saldo)
    else:
        saldo -= retiro
        print("Retiro exitoso.")
        print("Nuevo saldo: ", saldo)
    input("Presione enter para continuar. ")
    return saldo
# Seleccionar opciones
opcion = -1
while opcion != 0:
    print("\n-------MENÚ CAJERO AUTOMÁTICO-------")
    print("1. Consultar saldo. ")
    print("2. Depositar dinero. ")
    print("3. Retirar dinero")
    print("0. Salir. ")
    opcion = int(input("Seleccione una opción: "))
    if opcion == 1:
        saldo = consultar_saldo(saldo)
    elif opcion == 2:
        saldo = depositar(saldo)
    elif opcion == 3:
        saldo = retirar(saldo)
    elif opcion == 0:
        print("Gracias por usar el cajero automático.")
