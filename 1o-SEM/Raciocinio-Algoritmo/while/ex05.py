# Escreva um programa que receba 10 números do teclado e exiba a
# quantidade de números pares e ímpares lidos

i = 0
pares = 0
impares = 0

while i < 10: 
    numero = int(input("Digite 10 números e imprimirei quantos pares e ímpares foram digitados: "))

    if numero % 2 == 0:
        pares += 1
    else: 
        impares +=1

    i += 1    

print("Você me passou " + str(pares) + " números pares, e " + str(impares) + " números impares")
