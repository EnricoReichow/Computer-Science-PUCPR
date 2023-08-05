# Faca um programa que leia dois vetores de 10 posicoes e calcule outro vetor contendo,
# nas posicoes pares os valores do primeiro e nas posicoes impares os valores do segundo.

def coletarPrimeiraLista():
    primeiraLista = []
    for i in range(0, 10):
        valor = input("Digite um número para primeira lista: ")
        primeiraLista.append(valor)
    return primeiraLista

def coletarSegundaLista():
    segundaLista = []
    for i in range(0, 10):
        valor = input("Digite uma palavra para segunda lista: ")
        segundaLista.append(valor)
    return segundaLista

def juntarListas(primeiraLista, segundaLista):
    listaCompleta = []
    for valor in range(0, 10):
        if valor % 2 == 0:
            listaCompleta.append(primeiraLista[valor])
        else:
            listaCompleta.append(segundaLista[valor])
    return listaCompleta

primeiraLista = coletarPrimeiraLista()
segundaLista = coletarSegundaLista()

listaJunta = juntarListas(primeiraLista, segundaLista)

print("Lista Junta com a Lógica")
print(listaJunta)



