from Clase_Acciones import Acciones

accion=Acciones()
opcion=0

while opcion != 4:
    try:
        print("---------MENÚ PRINCIPAL------------")
        print("1).Ingresar nuevo contacto")
        print("2).Buscar contacto")
        print("3).Visualizar agenda")
        print("4).SALIR")
        opcion=int(input("Opcion: "))

        try:
            if opcion == 1:
                accion.NuevoContacto()
            elif opcion == 2:
                accion.Mostrar()
            elif opcion == 3:
                print("3")
        except:
            print("fallo en una operacion")

    except:
        print("!! solo numeros !!")
