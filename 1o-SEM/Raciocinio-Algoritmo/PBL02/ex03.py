# Faça um programa que peça três números inteiros e determine qual é o maior e qual é o menor.

print("DIGITE 3 NÚMEROS E TE DIREI QUAL O MAIOR E QUAL O MENOR :) ")

print("")

numeroUm = int(input("Digite o PRIMEIRO número: "))
numeroDois = int(input("Digite o SEGUNDO número: "))
numeroTres = int(input("Digite o TERCEIRO número: "))

maiorNumero = 0
menorNumero = 0 

if numeroUm > numeroDois and numeroUm > numeroTres:
    maiorNumero = numeroUm
elif numeroUm < numeroDois and numeroUm < numeroTres:
    menorNumero = numeroUm

if numeroDois > numeroUm and numeroDois > numeroTres:
    maiorNumero = numeroDois
elif numeroDois < numeroUm and numeroDois < numeroTres:
    menorNumero = numeroDois

if numeroTres > numeroUm and numeroTres > numeroDois:
    maiorNumero = numeroTres
elif numeroTres < numeroUm and numeroTres < numeroDois:
    menorNumero = numeroTres

else:
    print("Erro de Logica")


print("O maior número que você me passou foi " + str(maiorNumero))
print("E o menor número foi " + str(menorNumero))


