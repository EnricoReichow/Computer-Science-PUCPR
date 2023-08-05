# criando uma matriz

matriz = [[1, 2], [3, 4]]

matrizMelhorVisualização = [
    [1, 2],
    [3, 4]                       # geralmente cria-se assim para melhor visualização
]

matrizExample = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

matrizExample[0][2] = 2 # [linha][coluna]
matrizExample[2][0] = 7
matrizExample[3][3] = 8

numero1 = matrizExample[0][2] # atribuindo um valor da matriz na variável

for linha in range(0, 4): # depois de terminar as colunas da linha 0 ele pula de linha
    for coluna in range(0, 4): # PRIMEIRO TERMINA AS COLUNAS DA LINHA
        print(matrizExample[linha][coluna]) # percorrendo a matriz

for linha in range(0, 4):
    print(matrizExample[linha])