print("Vamos calcular a média de uma matéria sua")
materiaEstudada = str(input("Qual a matéria que vamos calcular a média e dar o resultado? "))

notaUm = float(input("Digite sua primeira nota: "))
notaDois = float(input("Digite sua segunda nota: "))
notaTres = float(input("Digite sua terceira nota: "))

media = (notaUm + notaDois + notaTres) / 3

if media >= 7:
    print("Você foi aprovado na matéria " + materiaEstudada + " com média " + str(media) + "!")
else: 
    print("Sinto te dizer que você reprovou em " + materiaEstudada + " com média " + str(media) + " :(")