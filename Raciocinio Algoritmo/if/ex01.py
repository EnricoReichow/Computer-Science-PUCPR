# Leia a idade do usuário e imprima se ele pode tirar a carteira de habilitação

idade = int(input("Qual sua idade? "))

if idade >= 18:
    print("Você já pode iniciar o processo da carteira de motorista (CNH)")

else: 
    print("Você não possui idade para tirar sua carteira de motorista")