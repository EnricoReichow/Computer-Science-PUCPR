# Leia uma matriz 4 x 4, conte e escreva quantos valores maiores que 10 ela possui.

def incluirValorNaMatriz():
    matriz = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    for l in range(0, 4):
        for c in range(0, 4):
            valor = int(input(f"Digite um numero para a matriz: "))
            matriz[l][c] = valor
    
    return matriz

def verificarValoresAcimaDeDez(matriz):
    valorAcimaDeDez = 0
    for l in range(0, 4):
        for c in range(0, 4):
            if matriz[l][c] > 10:
                valorAcimaDeDez += 1

    print(f"Na matriz tem {valorAcimaDeDez} acima de 10")
                

matrizParaVerificar = incluirValorNaMatriz()

verificarValoresAcimaDeDez(matrizParaVerificar)


