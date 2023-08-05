# Escreva um algoritmo em Python para calcular o valor, em reais, que deve ser pago por
# um cliente de uma locadora de carros. Sabe se que:
# a. O valor de locação de cada carro é 100,00 reais;
# b. O cliente pode locar um único carro por vários dias.

diasDelocacao = int(input("Por quantos dias você que alugar o carro? "))

valor = 100 * diasDelocacao

print("O valor a ser pago será de: R$" + str(valor))