# Imprima na tela a tabuada de um número inteiro lido pelo teclado

numeroEscolhido = int(input("Digite um número e imprimirei a tabuada dele: "))
i = 0

while i <= 10:
    print(str(numeroEscolhido) + " x " + str(i) + " = " + str(numeroEscolhido * i))
    i += 1