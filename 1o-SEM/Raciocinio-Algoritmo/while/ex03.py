# Implemente um programa em Python para ler do teclado números.
# Caso o usuário forneça um número igual a -1, o programa deve
# fornecer a média dos números e encerrar

i = 0
numeroQualquer = 0
soma = 0 

while numeroQualquer != -1:
    numeroQualquer = int(input("Digite um número qualquer. Se quiser parar digite -1 e te darei a média dos números anteriores: "))

    if numeroQualquer == -1:
        print("A média é = " + str(soma / i))
    else: 
        print("-----------------------------")

    soma += numeroQualquer

    i += 1
