# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

temperaturaC = float(input("Qual a temperatura em graus Celsius? "))

cParaFahrenheit = ((temperaturaC/5)*9) + 32

print(f'{temperaturaC:.1f}Cº eh equivalente a {cParaFahrenheit:.1f}F')
