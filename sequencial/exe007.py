# Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = float(input("Digite o tamanho do lado do quadrado: "))

# Área do quadrado: L*L
area = lado * lado

print(f'A área do quadrado é {area:.2f} e o dobro da área é {(area*2):.2f}')