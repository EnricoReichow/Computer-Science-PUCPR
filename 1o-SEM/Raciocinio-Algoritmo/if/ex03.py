# Escreva um algoritmo que dado o PdL (Pontos de Liga) de um jogador, informe a categoria a qual ele pertence

pdl = int(input("Digite seu PDL: "))

if pdl <= 999:
    print("Seu elo é Ferro")
elif pdl <= 1999:
    print("Seu elo é Bronze")
elif pdl <= 2999:
    print("Seu elo é Prata")
elif pdl <= 3999:
    print("Seu elo é Ouro")
elif pdl <= 4999:
    print("Seu elo é Platina")
elif pdl <= 5999:
    print("Seu elo é Diamente")
elif pdl <= 6999:
    print("Seu elo é Mestre")
elif pdl <= 7999:
    print("Seu elo é Grão Mestre")
else:
    print("Seu elo é Desafiante, GOD DEMAIS!!")