# Leia uma matriz de 3 x 3 elementos. Calcule a soma dos elementos que estao na diago-
# nal principal.

contador = 0 

matriz = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

for l in range(0, 3):
    for c in range(0, 3):
        print(str(l) + " " + str(c))
        valor = int(input(f"Digite o {contador + 1}o valor: "))
        matriz[l][c] = valor
        contador += 1

def somaDaDiagonalPrincipal(matriz):
    soma = 0

    for LinhaEColuna in range(0, 3):
        soma += matriz[LinhaEColuna][LinhaEColuna]

    return soma

soma = somaDaDiagonalPrincipal(matriz)

print(f"A soma é: {soma}")