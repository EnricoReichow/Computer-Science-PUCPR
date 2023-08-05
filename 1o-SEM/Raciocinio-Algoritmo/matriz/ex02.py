# Pratica 2, pegue o ex01 e mude os valores e reemprima dos 3 jeitos

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

print(" ")

print("Mudando valores...")

print(" ")

matriz[0][0] = 20
matriz[1][2] = 15
matriz[2][1] = 19

print(matriz)

print(" ")


for linha in range(0, 3):
    print(matriz[linha])

print(" ")

for linha in range(0, 3):
    for coluna in range(0, 3):
        print(matriz[linha][coluna])
