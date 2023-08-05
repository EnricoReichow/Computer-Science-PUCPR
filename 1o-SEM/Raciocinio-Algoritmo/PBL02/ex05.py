# Faça um programa que peça o peso e a altura de uma pessoa e calcule o seu IMC (índice de massa corporal) e informe se ela está abaixo, dentro ou acima do peso.

peso = float(input("Digite aqui seu peso em KG: "))
altura = float(input("Digite sua altura aqui em metros: "))
imc = peso / (altura*altura)
if imc <= 18.5:
    print("Você está abaixo do peso ideal seu imc e de", imc)
elif imc > 18.5 and imc <= 25.9:
    print("Você está no peso ideal seu imc e de", imc)
else:
    print("Você está acima do peso seu imc e de", imc) 