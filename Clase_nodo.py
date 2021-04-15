class Nodo():

    def __init__(self, nombre, apellido, telefono):
        self.nombre=nombre
        self.apellido=apellido
        self.telefono=telefono
        self.siguiente=None
        self.anterior=None

#------ metodos get --------

    def getNombre(self):
        return self.nombre
    
    def getApellido(self):
        return self.apellido

    def getTelefono(self):
        return self.telefono
    
    def getSiguiente(self):
        return self.siguiente
    
    def getAnterior(self):
        return self.anterior
    
#------ metodos set --------

    def setNombre(self, nombre):
        self.nombre=nombre
    
    def setApellido(self, apellido):
        self.apellido=apellido

    def setTelefono(self, telefono):
        self.telefono

    def setSiguiente(self, siguiente):
        self.siguiente=siguiente

    def setAnterior(self, anterior):
        self.anterior=anterior