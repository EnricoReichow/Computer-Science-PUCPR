def mensagemInicial():
    print("Vamos calcular a média das notas de 15 alunos!!")

def calcularMedia():
    vetorDeNotas = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for i in range(0, 15):
        vetorDeNotas[i] = int(input(f"Qual a nota do {i + 1}o aluno: "))
    soma = sum(vetorDeNotas)
    media  = soma / 15
    print(media)

mensagemInicial()
calcularMedia()