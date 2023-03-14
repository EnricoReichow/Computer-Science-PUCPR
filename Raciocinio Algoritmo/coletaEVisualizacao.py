nomeUuario = str(input("Informe seu nome: "))

cpfUsuario = str(input("Informe seu CPF: "))
cpfFormatado = cpfUsuario[:3] + "." + cpfUsuario[3:6] + "." + cpfUsuario[6:9] + "-" + cpfUsuario[9:] 

telefoneUsuario = str(input("Informe seu telefone com DDD: "))
telefoneFormatado = "(" + telefoneUsuario[:2] + ") " + telefoneUsuario[2:7] + "-" + telefoneUsuario[7:]

anoDeNascimentoUsuario = int(input("Informe seu ano de nascimento: "))

print("\n")
print("-------------------")
print("\n")

print("Olá " + nomeUuario + " seja bem vindo!")
print("Seu CPF cadastrado é: " + cpfFormatado)
print("Seu telefone cadastrado é: " + telefoneFormatado)
print("Você pode cursar nossa faculdade ja que nasceu no ano de " + str(anoDeNascimentoUsuario))

print("\n")
print("-------------------")
print("\n")