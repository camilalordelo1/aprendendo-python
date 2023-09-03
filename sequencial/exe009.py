# Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.C = 5 * ((F-32) / 9).

temperaturaF = float(input("Qual a temperatura em graus Fahrenheit? "))

fParaCeusius = 5 * ((temperaturaF-32) / 9)

print(f'{temperaturaF}F eh equivalente a {fParaCeusius:.1f}Cº')