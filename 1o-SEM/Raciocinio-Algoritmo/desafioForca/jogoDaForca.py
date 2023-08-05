import random # para fornecer dados randomicamente

# as palavras são marcas de carro
palavrasDoJogo = ["ferrari", "mercedes", "mclaren", "volkswagen", "renault"]

# escolhe uma palavra aleatória do vetor *palabrasDoJogo*
palavrasEscolhida = random.choice(palavrasDoJogo)

# setando as variáveis essenciais
tentativasRestantes = 10
erros = 0
tamanhoPalavra = 0
posicaoDaPalavra = 0

# lógica para definir o tamanho da palavra
for letra in palavrasEscolhida:
    tamanhoPalavra += 1

# faz um vetor de "•" com o tamanho da palavra
vetorSemResposta = ["•"] * tamanhoPalavra

# while para logica de repetição das jogadas
while True:
    print(f"## Tentativas Restantes = {tentativasRestantes} ##")
    print(" ".join(vetorSemResposta))
    tentativaDeLetra = input("Digite uma Letra: ")

    # valida se a letra escolhida tem na palavra e se tiver aparece no lugar das "•"
    # se não tiver diminui uma tentativa
    if tentativaDeLetra in palavrasEscolhida:
        for letraEscolhida in palavrasEscolhida:
            if tentativaDeLetra == letraEscolhida:
                vetorSemResposta[posicaoDaPalavra] = letraEscolhida
                posicaoDaPalavra += 1
            else:
                posicaoDaPalavra += 1
    else:
        tentativasRestantes -= 1

    # se todas as "•" acabarem o jogador vence já que a palavra está completa
    if "•" not in vetorSemResposta:
        print(f"Você venceu!! A palavra escolhida pelo sistema foi {palavrasEscolhida}")
        break

    # se a as tentativas acabarem o jogador perde
    if tentativasRestantes == 0:
        print(f"Fim de Jogo :( a palavra escolhida pelo sistema foi{palavrasEscolhida}")
        break

    posicaoDaPalavra = 0
    