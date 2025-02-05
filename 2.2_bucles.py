def contar_letra_en_frase(frase, letra):
    contador = 0
    for caracter in frase:
        if caracter == letra:
            contador += 1
    return contador

frase = input("Introduce una frase: ")
letra = input("Introduce una letra: ")

resultado = contar_letra_en_frase(frase, letra)
print(f"La letra '{letra}' aparece {resultado} veces en la frase '{frase}'")