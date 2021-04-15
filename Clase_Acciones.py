from Lista_Doble_Enlazada import Lista_Doble_Enlazada

class Acciones():

    def __init__(self):
        self.listaDatos=Lista_Doble_Enlazada()

    def NuevoContacto(self):
        print("-----------------------")
        nombrePersona=input("Ingrese Nombre: ")
        apellidoPersona=input("Ingrese Apellido: ")
        telefonoPersona=input("Ingrese Teléfono: ")
        self.listaDatos.Insertar(nombrePersona,apellidoPersona,telefonoPersona)

    def Mostrar(self):
        self.listaDatos.Recorrer()
        

