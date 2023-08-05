# Faça um programa que peça as notas de três provas de um aluno e calcule a média. Informe se o aluno está aprovado (média maior ou igual a 7), em recuperação (média entre 5 e 7) ou reprovado (média abaixo de 5).

nota1 = float(input("Digite a sua primeira nota: "))
nota2 = float(input("Digite a sua segunda nota: "))
nota3 = float(input("Digite a sua terceria nota: "))
media = (nota1 + nota2 + nota3)/3
if media >= 7:
    print("Parabens você foi aprovado")
elif media < 7 and media >= 5:
    print("Você ficou de recuperação")
else:
    print("Você foi reprovado")