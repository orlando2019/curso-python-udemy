from operator import itemgetter
# Esta funcion contamos palabras de una frase

mensaje = 'En muchas partes del cuerpo como son las manos, las orejas o los pies, están representados todos los órganos y partes del cuerpo. Incidiendo sobre estas zonas se pueden crear arcos reflejos que actúen directamente sobre cualquier órgano del cuerpo y que solucionen cualquier anomalía que exista.'

mensaje1 = mensaje.lower().replace('.', '').replace('?', '').replace(
    '¿', '').replace('!', '').replace(',', '')


def contar_palabras():

    mensaje2 = mensaje1.split()  # Convertimos la frase en un array

    # rint(mensaje2)

    total_palabras = {}

    for palabra in mensaje2:
        if palabra in total_palabras:
            total_palabras[palabra] += 1
        else:
            total_palabras[palabra] = 1

    # Aqui oredenamos ascedentemente y lo pasamos a un tipo diccionario
    palabras_ord = dict(
        sorted(total_palabras.items(), key=itemgetter(1), reverse=True))

    for k, v in palabras_ord.items():
        print('{} : {}'.format(k, v))


contar_palabras()
