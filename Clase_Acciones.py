from Lista_Doble_Enlazada import Lista_Doble_Enlazada
from graphviz import render
from io import open
import webbrowser

class Acciones():

    def __init__(self):
        self.listaDatos=Lista_Doble_Enlazada()

    def NuevoContacto(self):
        print("-----------------------")
        nombrePersona=input("Ingrese Nombre: ")
        apellidoPersona=input("Ingrese Apellido: ")
        telefonoPersona=input("Ingrese Teléfono: ")
        
        ContactoExistente=self.listaDatos.BuscarExistente(telefonoPersona)
        if ContactoExistente==False:
            self.listaDatos.Insertar(nombrePersona,apellidoPersona,telefonoPersona)
            print("\n>>> Contacto almacenado Exitosamente !!!\n")
        else:
            print("\n>>> Teléfono Existente, Usuario no Almacenado\n")
        

    def BuscarContacto(self,telefono):
        ContactoExistente=self.listaDatos.Buscar(telefono)
        if ContactoExistente == False:
            print("\n>>> Contacto no existente !!!")
            AgregarNuevo=input("\n¿ Desea agregarlo ? s=si / n=no: ")

            if AgregarNuevo== "s" or AgregarNuevo == "si":
                nombrePersona=input("Ingrese Nombre: ")
                apellidoPersona=input("Ingrese Apellido: ")
                self.listaDatos.Insertar(nombrePersona,apellidoPersona,telefono)
                print("\n>>> Contacto almacenado Exitosamente !!!\n")

    def CrearGrafo(self):
        if not self.listaDatos.vacio():
            NombrePictureSalida="agenda.dot"

            Crear_escribirArchivo=open(NombrePictureSalida,'w')
            Crear_escribirArchivo.write('digraph G {\n')
            Crear_escribirArchivo.write('node [shape=plaintext] \n')
            Crear_escribirArchivo.write('a [label=<<table border="0" cellborder="1" cellspacing="0"> \n')

            Crear_escribirArchivo.write('<tr><td colspan="4" bgcolor="orange">AGENDA DE CONTACTOS</td></tr> \n')
            Crear_escribirArchivo.write('<tr> \n')
            Crear_escribirArchivo.write('<td bgcolor="green">INDICE</td>\n')
            Crear_escribirArchivo.write('<td bgcolor="green">NOMBRE</td>\n')
            Crear_escribirArchivo.write('<td bgcolor="green">APELLIDO</td>\n')
            Crear_escribirArchivo.write('<td bgcolor="green">TELEFONO</td>\n')
            Crear_escribirArchivo.write('</tr> \n')

            indice=1
            tmp=self.listaDatos.primero
            while tmp != None:
                Crear_escribirArchivo.write('<tr> \n')
                Crear_escribirArchivo.write('<td>'+str(indice)+'</td>\n')
                Crear_escribirArchivo.write('<td>'+str(tmp.getNombre())+'</td>\n')
                Crear_escribirArchivo.write('<td>'+str(tmp.getApellido())+'</td>\n')
                Crear_escribirArchivo.write('<td>'+str(tmp.getTelefono())+'</td>\n')
                tmp=tmp.getSiguiente()
                indice+=1
                Crear_escribirArchivo.write('</tr>\n')
            
            Crear_escribirArchivo.write('</table>>];')
            Crear_escribirArchivo.write('}')
            Crear_escribirArchivo.close()
            render('dot','png',NombrePictureSalida)
            webbrowser.open_new_tab('agenda.dot.png')
            print("--- Se generó archivo .dot ---")
        
        else:
            print(">>> No hay Contactos que mostrar !!!")
            


        

