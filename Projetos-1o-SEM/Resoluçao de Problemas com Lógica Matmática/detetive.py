# frases 
import random

print("Esse jogo funciona como um detetive. Você vê as pistas 1 vez e com base na Pergunta " +
"sorteada você escolhe 3 pistas e define uma conclusão. Talvez você acerte a resposta mas " + 
"erre as dicas que levam a conclusão")

a = "1. Manoel Gomes é Nordestino"
b = "2. Manoel Gomes só tem no bolso uma caneta azul"
c = "3. Manoel Gomes já foi apaionado"
d = "4. Manoel Gomes parece ser muito calmo"
e = "5. Manoel Gomes fez turnê nos EUA"
f = "6. Manoel Gomes é muito desastrado" 
g = "7. Manoel Gomes odeia o cachorro salsicha"
h = "8. Manoel Gomes odeia quando falam mal do Nordeste"

listaDePistas = [a, b, c, d, e, f, g, h]

listaPerguntas = ["Quem matou Maura e como foi o assassinato?", "Porque Manoel Gomes colocu veneno no Cachorro quente de Osasco?", "Qual droga Manoel Gomes ususfrui no dia a dia?"]

pistaEscolhidaUm = int(input("Qual a primeira pista que você quer escolher: "))
pistaEscolhidaDois = int(input("Qual a segunda pista que você quer escolher: "))
pistaEscolhidaTres = int(input("Qual a terceira pista que você quer escolher: "))

listaDePistasEscolhidas = [pistaEscolhidaUm, pistaEscolhidaDois, pistaEscolhidaTres]

i = 0

while i > 3:
    if pistaEscolhidaUm == 1 or pistaEscolhidaDois == 1 or pistaEscolhidaTres == 1:
        listaDePistasEscolhidas[i] = listaDePistas[0]

    elif pistaEscolhidaUm == 2 or pistaEscolhidaDois == 2 or pistaEscolhidaTres == 2:
        listaDePistasEscolhidas[i] = listaDePistas[1]

    elif pistaEscolhidaUm == 3 or pistaEscolhidaDois == 3 or pistaEscolhidaTres == 3:
        listaDePistasEscolhidas[i] = listaDePistas[2]

    elif pistaEscolhidaUm == 4 or pistaEscolhidaDois == 4 or pistaEscolhidaTres == 4:
        listaDePistasEscolhidas[i] = listaDePistas[3]

    elif pistaEscolhidaUm == 5 or pistaEscolhidaDois == 5 or pistaEscolhidaTres == 5:
        listaDePistasEscolhidas[i] = listaDePistas[4]

    elif pistaEscolhidaUm == 6 or pistaEscolhidaDois == 6 or pistaEscolhidaTres == 6:
        listaDePistasEscolhidas[i] = listaDePistas[5]

    elif pistaEscolhidaUm == 7 or pistaEscolhidaDois == 7 or pistaEscolhidaTres == 7:
        listaDePistasEscolhidas[i] = listaDePistas[6]

    elif pistaEscolhidaUm == 8 or pistaEscolhidaDois == 8 or pistaEscolhidaTres == 8:
        listaDePistasEscolhidas[i] = listaDePistas[7]

    i+=1


print(listaDePistasEscolhidas)
print(listaDePistasEscolhidas)
print(listaDePistasEscolhidas)