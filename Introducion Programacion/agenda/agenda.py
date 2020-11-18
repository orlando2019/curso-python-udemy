import os
import sys

CARPETA = "mis_contactos/"  # Carpeta de contactos
EXTENSION = ".txt"  # Extension de contactos


# Clase Contacto
class Contacto:
    def __init__(self, nombre, apellido, telefono, categoria):
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono
        self.categoria = categoria


# Aplicacion Principal
def app():

    crear_directorio()

    mostrar_menu()

    # Preguntar al usuario la acción a realizar
    preguntar = True
    while preguntar:
        opcion = input("Seleccione una opción: \r\n")
        opcion = int(opcion)

        # Ejecutar las opciones
        if opcion == 1:
            agregar_contacto()
            preguntar = False
        elif opcion == 2:
            editar_contacto()
            preguntar = False
        elif opcion == 3:
            mostrar_contacto()
            preguntar = False
        elif opcion == 4:
            buscar_contacto()
            preguntar = False
        elif opcion == 5:
            eliminar_contacto()
            preguntar = False
        elif opcion == 6:
            cerrar()
        else:
            print("OPCIÓN NO VALIDA, INTENTE DE NUEVO!!! \r\n")
        mostrar_menu()


# -- CREACION DE FUNCIONES PARA LA APLICACION PRINCIPAL ---


# Función de Agregar Contacto
def agregar_contacto():
    print("Escribe los datos para agregar el nuevo Contacto:")
    nombre_contacto = input("Nombre del Nuevo Contacto:\r\n")

    # Revisar si el contacto ya existe antes de crearlo
    existe = existe_contacto(nombre_contacto)
    if not existe:
        with open(CARPETA + nombre_contacto + EXTENSION, "w") as archivo:

            # Resto de los campos
            apellido_cotacto = input("Agrega El Apellido: \r\n")
            telefono_cotacto = input("Agrega El Teléfono: \r\n")
            categoria_cotacto = input("Agrega La Categoria: \r\n")

            # Instanciamos la clase
            contacto = Contacto(nombre_contacto, apellido_cotacto,
                                telefono_cotacto, categoria_cotacto)

            # Escrbir el archivo
            archivo.write("Nombre: " + contacto.nombre + "\n")
            archivo.write("Apellido: " + contacto.apellido + "\n")
            archivo.write("Telefono: " + contacto.telefono + "\n")
            archivo.write("Cateria: " + contacto.categoria + "\n")

            # Mostrar un mensaje de éxito
            print("\r\n Contacto Creado Correctamente \r\n")
    else:
        print(f"Ya {nombre_contacto} Existe.... Crea Otro Contacto\r\n")
    # Reiniciando nuestra app
    app()


# Funcion Editar contacto
def editar_contacto():
    nombre_editar = input("Nombre del contacto que desea editar: \r\n")

    # Revisamos si el contacto ya existe
    existe = existe_contacto(nombre_editar)

    if existe:
        with open(CARPETA + nombre_editar + EXTENSION, 'w') as archivo:

            # Resto de los campos
            nombre_contacto = input("Agrega el Nuevo Nombre del Contacto:\r\n")
            apellido_cotacto = input("Agrega el Nuevo Apellido: \r\n")
            telefono_cotacto = input("Agrega el Nuevo Teléfono: \r\n")
            categoria_cotacto = input("Agrega la Nueva Categoría: \r\n")

            # Intanciamos la clase contacto
            contacto = Contacto(nombre_contacto, apellido_cotacto,
                                telefono_cotacto, categoria_cotacto)

            # Escrbir el archivo
            archivo.write("Nombre: " + contacto.nombre + "\n")
            archivo.write("Apellido: " + contacto.apellido + "\n")
            archivo.write("Telefono: " + contacto.telefono + "\n")
            archivo.write("Cateria: " + contacto.categoria + "\n")

            # Renombrar el archivo
        os.rename(
            CARPETA + nombre_editar + EXTENSION,
            CARPETA + nombre_contacto + EXTENSION,
        )
        # Mostrar un mensaje de éxito
        print("\r\n Contacto Editado Correctamente \r\n")
    else:
        print("El contacto No existe")
    app()


#Funcion Mostrar Contacto
def mostrar_contacto():
    archivos = os.listdir(CARPETA)

    archivos_txt = [i for i in archivos if i.endswith(EXTENSION)]

    print(f'Lista De Contactos')

    for archivo in archivos_txt:
        with open(CARPETA + archivo) as contacto:
            for linea in contacto:
                #Imprime Los Contacto
                print(linea.rstrip())
            #Imprime un Separador entre contactos
            print('\r\n')
    #Reinicio App
    app()


#Funcion Buscar Contacto
def buscar_contacto():
    nombre = input('Seleccione el Contacto que desea Buscar: \r\n')

    try:
        with open(CARPETA + nombre + EXTENSION) as contacto:
            print('\r\n Informacion Del Cotacto: \r\n')
            for linea in contacto:
                print(linea.rstrip())
            print('\r\n')
    except IOError:
        print('El Archivo No Exite....')

    #Reeiniciamos la app
    app()


#Funcion Eliminar Contacto
def eliminar_contacto():
    nombre = input('Seleccione El Contacto Que Desea Eliminar: \r\n')

    try:
        os.remove(CARPETA + nombre + EXTENSION)
        print('\r\n El Contacto Fue Eliminado Correctamente')
    except:
        print('No Existe Ese Contacto....!!\r\n')
    #Reiniciamos la App
    app()


#Funcion Cerrar
def cerrar():
    sys.exit(print('Gracias Por Utilizar Nuestra Aplicacion\r\n'))


# Muestra el Munú de Opciones
def mostrar_menu():
    print("bienvenido a mi aplicación \r\n".title().center(50, ' '))
    print("#### Seleccione del menú lo que desea hacer: #### \r\n".title())
    print("1 => Agregar Nuevo Contacto")
    print("2 => Editar Contacto")
    print("3 => Ver Contactos")
    print("4 => Buscar Contacto")
    print("5 => Eliminar Contacto")
    print("6 => Cerrar Aplicación")


# Revisa si mi carpeta de contactos ya existe
def crear_directorio():
    if not os.path.exists(CARPETA):
        # Crea la carpeta
        os.makedirs(CARPETA)
    """ else:
        print('La Carpeta ya existe!!!') """


def existe_contacto(nombre):
    return os.path.isfile(CARPETA + nombre + EXTENSION)


app()
