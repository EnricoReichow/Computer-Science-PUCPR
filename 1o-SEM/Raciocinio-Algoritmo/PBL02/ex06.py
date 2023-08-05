# Faça um programa que peça um número inteiro entre 1 e 7 e informe o dia da semana correspondente.

dia = int(input("insira um numero de 1 a 7 "))

if dia == 7:
    print("Hoje  e sabado que tambem e dia de tomar uma")
elif dia == 6:
    print("Hoje e sexta dia de tomar uma")
elif dia == 5:
    print("Hoje e quinta quase dia de tomar uma")
elif dia == 4:
    print("Hoje e quarta meio da semana")
elif dia == 3:
    print("Hoje e terca rapaz")
elif dia == 2:
    print("Hoje e segunda dia de sonhar com a sexta")
elif dia == 1:
    print("Domingou dia de churrasco cerveja e pagode")
else:
    print("Esse número digitado não corresponde a um dia da semana")