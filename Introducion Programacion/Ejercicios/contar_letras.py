def leer_frase():
    global texto, text1, text2
    # global text
    # text = (input("Ingrese la frase: \t\n"))
    texto = "Saber qué palabras son las más frecuentes de un texto resulta interesante para diferentes fines. Podemos estar investigando una obra literaria y querer saber qué unidades léxicas usa más frecuentemente el autor. O podremos estar analizando lingüísticamente una entrevista o una grabación y querer saber qué palabras se han repetido más. ¿Qué palabras repite más un político en un discurso importante? ¿Cuáles son los temas más repetidos de un tipo concreto de poesía? ¿Qué país se menciona más veces en un texto de historia"

    text1 = texto.lower().replace('.', '').replace('?', '').replace('¿', '')
    text2 = text1.split()
    """ for i in range(len(text2)):
		print(i,text2[i]) """


def contar_letras():
    contar = 0

    for i in texto:
        if (i.isalpha()):
            contar += 1

    print(f'La cantidad de letras de la frase son: {contar}')


def contar_palabras():
    contar = 0
    for i in text2:
        if (i.isalpha()):
            contar += 1

    print(f'La cantidad de palabras en la frase son: {contar}')


leer_frase()
contar_letras()
contar_palabras()
