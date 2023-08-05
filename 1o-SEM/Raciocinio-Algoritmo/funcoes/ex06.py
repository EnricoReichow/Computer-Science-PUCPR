# 6. Escreva uma função chamada "imprime_diagonal" que recebe uma matriz de tamanho
# 3x3 preenchida com valores quaisquer, e imprime os valores na diagonal principal

def imprime_digonal(matriz):
    primeiroValor = matriz[0][0]
    segundoValor = matriz[1][1]
    terceiroValor = matriz[2][2] 
    diagonal = str(primeiroValor) + ", " + str(segundoValor) + ", " + str(terceiroValor)
    return diagonal

matrizUsada = [
    [4, 6, 9],
    [3, 2, 1],
    [2, 7, 1]
]

print(imprime_digonal(matrizUsada))
