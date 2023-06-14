# Leia duas matrizes 4 x 4 e escreva uma terceira com os maiores valores de cada posicao
# das matrizes lidas

def incluirValorNaMatriz1():
    matriz1 = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    for l1 in range(0, 4):
        for c1 in range(0, 4):
            valor1 = int(input(f"Digite um numero para Primeira matriz: "))
            matriz1[l1][c1] = valor1
    
    matriz2 = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]
    for l2 in range(0, 4):
        for c2 in range(0, 4):
            valor2 = int(input(f"Digite um numero para Segunda matriz: "))
            matriz2[l2][c2] = valor2 

    matrizFinal = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0]
    ]

    for lFinal in range(0, 4):
        for cFinal in range(0, 4):
            if matriz1[lFinal][cFinal] > matriz2[lFinal][cFinal]:
                matrizFinal[lFinal][cFinal] = matriz1[lFinal][cFinal]
            else: 
                matrizFinal[lFinal][cFinal] = matriz2[lFinal][cFinal]
    
    print("Matriz com os maiores valores: ")
    for linha in range(0, 4):
            print(matrizFinal[linha])

incluirValorNaMatriz1()

