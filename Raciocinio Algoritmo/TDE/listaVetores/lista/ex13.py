def posicaoDosMaiores():
    listaDeNumeros = []
    contador = 0
    while contador < 5:
        valor = int(input("Digite um valor qualquer: "))
        listaDeNumeros.append(valor)
        contador += 1

    maior = max(listaDeNumeros)
    menor = min(listaDeNumeros)
    contadorPosicaoMaior = 0
    contadorPosicaoMenor = 0

    while contadorPosicaoMaior < 5:
        if listaDeNumeros[contadorPosicaoMaior] == maior:
            print(f"O maior numero está na posição/index {contadorPosicaoMaior}")
        
        contadorPosicaoMaior += 1 

    while contadorPosicaoMenor < 5:
        if listaDeNumeros[contadorPosicaoMenor] == menor:
            print(f"O maior numero está na posição/index {contadorPosicaoMenor}")
        
        contadorPosicaoMenor += 1


posicaoDosMaiores()