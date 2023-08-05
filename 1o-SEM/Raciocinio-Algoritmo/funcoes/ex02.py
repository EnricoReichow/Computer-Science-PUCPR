# 2. Escreva uma função chamada "maior" que receba três numeros como parametros e retorne o maior entre elas

def maior(numeroUm, numeroDois, numeroTres):

    if numeroUm > numeroDois and numeroUm > numeroTres:
        print(numeroUm)
    elif numeroDois > numeroUm and numeroDois > numeroTres:
        print(numeroDois)
    elif numeroTres > numeroUm and numeroTres > numeroDois:
        print(numeroTres)
    else:
        print("Os números são igauis")

maior(6, 3, 10)

    