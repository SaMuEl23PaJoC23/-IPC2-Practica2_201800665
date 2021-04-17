from Clase_Acciones import Acciones


accion=Acciones()
opcion=0

while opcion != 4:
    print("---------MENÚ PRINCIPAL------------")
    print("1).Ingresar nuevo contacto")
    print("2).Buscar contacto")
    print("3).Visualizar agenda")
    print("4).SALIR")
    opcion=int(input("Opcion: "))
    print("-----------------------------------")

    if opcion == 1:
        print("-----INGRESAR NUEVO CONTACTO--------")
        accion.NuevoContacto()

    elif opcion == 2:
        print("--------BUSCAR CONTACTO---------")
        telefonoBuscar=input("Ingrese telefono de contacto:")
        accion.BuscarContacto(telefonoBuscar)
                
    elif opcion == 3:
        accion.CrearGrafo()
