str = 'Saber qué palabras son las más frecuentes de un texto resulta interesante para diferentes fines. Podemos estar investigando una obra literaria y querer saber qué unidades léxicas usa más frecuentemente el autor. O podremos estar analizando lingüísticamente una entrevista o una grabación y querer saber qué palabras se han repetido más. ¿Qué palabras repite más un político en un discurso importante? ¿Cuáles son los temas más repetidos de un tipo concreto de poesía? ¿Qué país se menciona más veces en un texto de historia?'

str1 = str.lower().replace('.', '').replace(
    '?', '').replace('¿', '').replace(',', '')


def app():
    separador = str1.split()

    print(separador)


app()
