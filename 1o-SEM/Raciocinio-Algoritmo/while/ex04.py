# Implemente um programa em Python para imprimir na tela o
# somatório dos N primeiros números inteiros a partir do 1. 
# Sendo N lido do teclado

numero = int(input("Digite um número inteiro: "))
soma = 0
i = 2

while i <= numero:
    soma += i
    i += 1

print("A soma dos primeiros " + str(numero), "números inteiros é: " + str(soma))