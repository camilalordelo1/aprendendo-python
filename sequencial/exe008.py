# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

salarioHora = float(input("Quanto você ganha por hora? "))
horasTrabalhadas = float(input("Quantas horas você trabalhou? "))

salarioTotal = salarioHora*horasTrabalhadas

print(f'O salário total do mes eh {salarioTotal:.2f}')