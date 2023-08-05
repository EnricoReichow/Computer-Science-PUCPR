# Faça um programa que peça o salário de um funcionário e calcule o valor do seu aumento. Para salários acima de R$ 1.500,00, o aumento é de 10%. Para salários iguais ou inferiores a R$ 1.500,00, o aumento é de 15%.

salario = float(input("Digite o seu salário: "))
if salario > 1500:
    salarioNovo1 = salario*1.1
    salarioRedondo1 = round(salarioNovo1,2)
    print(f"Seu salário após o aumento é {salarioRedondo1} reais")
else:
    salarioNovo2 = salario*1.15
    salarioRedondo2 = round(salarioNovo2,2)
    print(f"Seu salário após o aumento é {salarioRedondo2} reais")