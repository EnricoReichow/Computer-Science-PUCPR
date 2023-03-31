# Crie um algoritmo que calcula o IMC e imprime o resultado

pesoUsuario = float(input("Qual seu peso: "))
alturaUsuario = float(input("Qual sua altura: "))

calculo = pesoUsuario / (alturaUsuario * alturaUsuario)
imc = str(calculo)

print("Seu IMC tem valor de: " + imc[0:4])