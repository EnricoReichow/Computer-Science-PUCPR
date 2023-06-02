# 4. Escreva uma função chamada "media" que receba uma lista de números como
# parâmetro e retorne a média desses números.

def media(listaDeNumeros):
    mediaEntreEles = sum(listaDeNumeros) / len(listaDeNumeros)
    return mediaEntreEles

listaDeNumeros = [2, 4, 6, 8, 10]

print(media(listaDeNumeros))
