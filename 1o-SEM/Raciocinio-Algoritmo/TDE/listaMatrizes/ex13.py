# Gere matriz 4 x 4 com valores no intervalo [1, 20]. Escreva um programa que transforme
# a matriz gerada numa matriz triangular inferior, ou seja, atribuindo zero a todos os ele-
# mentos acima da diagonal principal. Imprima a matriz original e a matriz transformada

import random

def gerarMatriz():
    matriz = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
    ]

    for l in range(0, 4):
        for c in range(0, 4):
            valor = random.randint(1, 20)
            matriz[l][c] = valor
    
    return matriz

def matrizTriangularInferior(matriz):

    for l0 in range(1, 4):
            valor = 0
            matriz[0][l0] = valor
    

    for l1 in range(2, 4):
            valor = 0
            matriz[1][l1] = valor

    for l2 in range(3, 4):
            valor = 0
            matriz[2][l2] = valor

    for m in range(0, 4):
        print(matriz[m])

matriz = gerarMatriz()

def printarMatrizOriginal(matriz):
    for linha in range(0, 4):
        print(matriz[linha])

print("A matriz gerada foi: ")
printarMatrizOriginal(matriz)
print("")

print("A matriz traformada é:")
matrizTriangularInferior(matriz)

    

             
