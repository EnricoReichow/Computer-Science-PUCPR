vetorDeNumeros = [34, 55, 1879, 2, 630, 47893, 23671, 32222, 9, 100001]

def paresEImpares(vetorDeNumeros):
    pares = 0
    impares = 0

    for numeros in vetorDeNumeros:
        if numeros % 2 == 0:
            pares += 1

    print(f"Valores Pares: {pares}")

paresEImpares(vetorDeNumeros)