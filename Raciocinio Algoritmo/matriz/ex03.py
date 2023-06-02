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

soma = matriz[0][0] + matriz[0][0]
subtracao = matriz[2][2] + matriz[2][1]
multiplicacao = matriz[0][1] * matriz[2][0]
divisao = matriz[1][2] / matriz[0][2]

print(" ")

print(soma)
print(subtracao)
print(multiplicacao)
print(divisao)