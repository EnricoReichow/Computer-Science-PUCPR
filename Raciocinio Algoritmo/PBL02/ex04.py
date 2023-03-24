# Faça um programa que peça a idade de uma pessoa e informe se ela pode votar ou não.

print("VAMOS VER SE VOCÊ TEM IDADE PARA VOTAR (SE TEM 16 ANOS OU MAIS)")

idade = int(input("Qual sua idade: "))

if idade >= 16:
    print("Você está permitido(a) por lei para votar!")
else: 
    print("Você não possui idade para votar ainda.")