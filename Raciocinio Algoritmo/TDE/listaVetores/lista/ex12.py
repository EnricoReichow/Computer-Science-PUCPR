def calcularMedia(valores):
    soma = sum(valores)
    media = soma / len(valores)
    return media

def resolucao() :
    numeros  = []

    for i in range(0, 5):
        valor = float(input("Digite um valor: "))
        numeros.append(valor)

    print(f"Números lidos: {numeros}")
    
    maiorNumero = max(numeros)
    menorNumero = min(numeros)
    media = calcularMedia(numeros)

    print(f"Maior número: {maiorNumero}")
    print(f"Menor número: {menorNumero}")
    print(f"Media dos números: {media}")

resolucao() 

    