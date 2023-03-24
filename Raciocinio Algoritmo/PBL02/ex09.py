# Faça um programa que peça o nome de um mês e informe quantos dias ele tem. Considere fevereiro sempre com 28 dias.

mesRaw = input("Digite o nome do mês (Ex: Janeiro): ")
mes = mesRaw.lower()

if mes == "janeiro" or mes == "january":
    print("Esse mês tem 31 dias.")

elif mes == "fevereiro" or mes == "february":
    print("Esse mês tem 28 dias.")

elif mes == "março" or mes == "march":
    print("Esse mês tem 31 dias")

elif mes == "abril" or mes == "april":
    print("Esse mês 30 dias")

elif mes == "maio" or mes == "may":
    print("Esse mês tem 31 dias")

elif mes == "junho" or mes == "june":
    print("Esse mês tem 30 dias.")

elif mes == "julho" or mes == "july":
    print("Esse mês tem 31 dias.")

elif mes == "agosto" or mes == "august":
    print("Esse mês tem 31 dias.")

elif mes == "setembro" or mes == "september":
    print("Esse mês tem 30 dias.")

elif mes == "outubro" or mes == "october":
    print("Esse mês tem 31 dias.")

elif mes == "novembro" or mes == "november":
    print("Esse mês tem 30 dias.")

elif mes == "dezembro" or mes == "dezember":
    print("Esse mês tem 31 dias")

else:
    print("Você não digitou um mês valido")