# Pratica 1, crie uma matriz 3x3 e imprima a matriz inteira numa linha,
# a matriz com um FOR
# a matriz com 2 FOR

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

print(matriz)

print(" ")


for linha in range(0, 3):
    print(matriz[linha])

print(" ")

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(matriz[linha][coluna])


