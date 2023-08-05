numeros = [5, 7, 12, 2, 9, 21]

print(numeros) # exibe no console o vetor completo

print(numeros[0]) # exibe cada valor num print baseado no índice
print(numeros[1])
print(numeros[2])
print(numeros[3])
print(numeros[4])
print(numeros[5])
print("")

numeros[1] = 17 # trocando os valores dos indices determinados
numeros[3] = 22

print(numeros[1]) 
print(numeros[3])
print("")


numeros[2] = 1
numeros[4] = 29

print(numeros[2]) # trocando os valores dos indices determinados novamente
print(numeros[4])
print("")

operacaoUm = numeros[5] + numeros[4]     # acessando valores no vetor e fazer operacoes com eles
operacaoDois = numeros[3] - numeros[1]
operacaoTres = numeros[0] * numeros[5]
operacaoQuatro = numeros[3] / numeros[2]

print(operacaoUm)
print(operacaoDois)
print(operacaoTres)
print(int(operacaoQuatro))
print("")

indice = 0

while indice < 6:
    print(numeros[indice])
    indice += 1

