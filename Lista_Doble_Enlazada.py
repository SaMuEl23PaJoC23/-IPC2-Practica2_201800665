from Clase_nodo import Nodo

class Lista_Doble_Enlazada():

    def __init__(self):
        self.primero=None
        self.ultimo=None

    def vacio(self):
        return self.primero==None

    def Insertar(self, nombre, apellido, telefono):
        if self.vacio():
            self.primero=self.ultimo=Nodo(nombre,apellido,telefono)
        
        else:
            NodoNuevo=Nodo(nombre,apellido,telefono)
            self.ultimo.setSiguiente(NodoNuevo)
            NodoNuevo.setAnterior(self.ultimo)
            self.ultimo=NodoNuevo
    
    def Recorrer(self):
        if not self.vacio():
            tmp=self.primero
            while tmp != None:
                print("-------------------------")
                print("Nombre:",tmp.getNombre())
                print("Apellido:",tmp.getApellido())
                print("telefono:",tmp.getTelefono())
                tmp=tmp.getSiguiente()
        else:
            print("Lista Vacía...")