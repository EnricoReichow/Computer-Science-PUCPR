def receber_numeros():
    numeros = [0, 0, 0, 0, 0, 0]
    contador = 0
    while contador < 6: 
        numeros[contador] = int(input("Digite um número qualquer: "))
        contador += 1
    print(numeros)

receber_numeros()

