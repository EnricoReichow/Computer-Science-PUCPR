# Implemente um programa em Python para ler do teclado a nota deum aluno. Verifique se o valor lido é uma nota válida (maior que 7).
# Se não for, ler este valor até que a mesma seja válida.

nota = 0

while nota != 7:
    nota = int(input("Digite uma nota válida para passar de ano: "))

    if nota >= 7:
        print("Essa nota é válida para passar de ano!")
    else:
        print("--------------------------------------")
