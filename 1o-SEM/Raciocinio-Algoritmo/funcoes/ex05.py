# 5. Escreva uma função chamada "inverter" que receba uma string como parâmetro e
# imprime a string invertida

def inverter(string):
    string = string [::-1]
    return string

frase = "Eu faço Ciência da Computação"

print(inverter(frase))