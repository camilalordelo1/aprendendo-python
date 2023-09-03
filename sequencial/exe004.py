# Faça um Programa que peça as 4 notas bimestrais e mostre a média.
n1 = input("Digite nota 1: ")
n2 = input("Digite nota 2: ")
n3 = input("Digite nota 3: ")
n4 = input("Digite nota 4: ")

media = (float(n1) + float(n2) + float(n3) + float(n4))/4

print(f'A media do aluno eh {media:.2f}')