def ordenar_lista_palabras():
    palabras = []
    while True:
        palabra = input("Ingrese una palabra (o 'salir' para terminar): ")
        if palabra.lower() == 'salir':
            break
        palabras.append(palabra)
    
    palabras.sort()
    print("Lista de palabras ordenadas alfabéticamente:")
    for palabra in palabras:
        print(palabra)

ordenar_lista_palabras()
