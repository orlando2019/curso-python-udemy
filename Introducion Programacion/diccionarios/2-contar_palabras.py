from operator import itemgetter
import re
# Esta funcion contamos palabras de una frase

mensaje = 'En muchas partes del cuerpo como son las manos, las orejas o los pies,,,,,,.... están representados todos los órganos y partes del cuerpo. Incidiendo sobre estas zonas se pueden crear arcos Reflejos que Actúen ORLANDO ORLANDO ORLANDO Directamente sobre cualquier órgano del cuerpo y que solucionen cualquier anomalía? ORLANDO ORLANDO11 221 22000 ORLANDO111 que exista.?¿¡¡!!'

#Expresion regular y sustituimos por espacios en blanco
texto = re.sub(r"\,|\.|\?|\¿|\!|\d|\¡", "", mensaje)
#texto1 = re.sub(r"\d", "", mensaje)
#print(texto)

mensaje1 = texto.lower()
#print(mensaje1)


def contar_palabras():

    mensaje2 = mensaje1.split()  # Convertimos la frase en un array

    # print(mensaje2)

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
        #print('{} : {}'.format(k, v))
        print(f'{k} : {v}')


contar_palabras()
