# Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.

raio = input("Digite o raio de um círculo: ")

# A = π r²
area = 3.14*(float(raio)**2)

print(f'A área do círculo com o raio informado é {area:.2f}')