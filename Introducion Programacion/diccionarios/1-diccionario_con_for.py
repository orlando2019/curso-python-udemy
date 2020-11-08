from operator import itemgetter


def claveValor():
    coleccion = {'Alejandro': 23, 'Orlando': 40, 'Gaby': 10, 'Tobias': 15}

    for clave, valor in coleccion.items():
        print(f'{clave} => {valor}')


def agregarValor():
    nombre = input(f"Digite Nombre De La Persona: \t\n")
    edad = input(f"Digite Edad De La Persona: \t\n")
    datos = {}

    for nombre, edad in datos.items():
        datos[nombre] = edad

    print(f'Nombre {nombre.capitalize()} Edad {edad}')


# Esta funcion nos ayuda contar letras de un frase
def contar_letras():

    mensaje = 'En muchas partes del cuerpo como son las manos, las orejas o los pies, están representados todos los órganos y partes del cuerpo. Incidiendo sobre estas zonas se pueden crear arcos reflejos que actúen directamente sobre cualquier órgano del cuerpo y que solucionen cualquier anomalía que exista. En las manos, las orejas o los pies, se representan todos los órganos del cuerpo. Incidiendo sobre estas zonas se pueden crear arcos reflejos que actúen directamente sobre cualquier punto del organismo y que solucionan cualquier punto del organismo y que solucionen la anomalía que exista.'
    mensaje1 = mensaje.lower().replace('.', '').replace(
        '?', '').replace('¿', '').replace(' ', '').replace(',', '')  # Con este metodo quitmos los signo de puntuacion y los espacios

    total_letra = {}

    # print(mensaje1)

    for letra in mensaje1:
        if letra in total_letra:
            total_letra[letra] += 1
        else:
            total_letra[letra] = 1

    # Aqui oredenamos ascedentemente y lo pasamos a un tipo diccionario
    letras_ord = dict(sorted(total_letra.items(), key=itemgetter(1)))
    # print(letras_ord)

    for k, v in letras_ord.items():  # con este for formateamos el diccionario
        print('{}: {}'.format(k, v))


# claveValor()
# agregarValor()
contar_letras()
