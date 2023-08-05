# Calcular preço de venda para produto por quilo

valorDaGramaProduto = float(input("Digite o valor da grama do produto: "))
peso = float(input("Digite o peso do produto em Kg: "))

preco = valorDaGramaProduto * (peso * 1000) 

print(f'O preço a ser pago é de R${preco}')