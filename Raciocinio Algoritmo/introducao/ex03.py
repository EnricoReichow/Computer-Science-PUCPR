# Leia do teclado a temperatura em Celsius e imprima o equivalente em Fahrenheit.
# (Fórmula: (X ºC × 9/5) + 32

celsius = float(input("Digite a temperatura em Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Então a temperatura em Fahrenheit é " + str(fahrenheit))