# Refaça o desafio 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: todos os lados iguais;
# Isósceles: dois lados iguais;
# Escaleno: todos os lados diferentes.

lado1 = float(input('\nInforme o comprimento do 1º lado do trângulo: '))
lado2 = float(input('Informe o comprimento do 2º lado: '))
lado3 = float(input('Informe o comprimento do 3º lado: '))

if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:

    print(f'\nAs medidades {lado1}, {lado2} e {lado3} podem formar um triângulo ', end='')

    if lado1 == lado2 == lado3:

        print('equilátero.')

    elif lado1 != lado2 != lado3 != lado1:

        print('escaleno.')

    else:

        print('isósceles.')

else:

    print(f'\nAs medidas {lado1}, {lado2} e {lado3} não podem formar um triângulo.')
