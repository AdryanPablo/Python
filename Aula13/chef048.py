# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três
# e que se encontram no intervalo de 1 até 500.

soma = 0
contador = 0

"""
for contador in range(1, 500):

    if contador % 2 == 1 and contador % 3 == 0:

        print(f'{contador} ', end='')
        soma += contador
"""

for números in range(3, 500, 6):

    if números == 495:

        print(f'{números}.')
        soma += números
        contador += 1

    else:

        print(f'{números}, ', end='')
        soma += números
        contador += 1

print(f'\nA soma dos {contador} números ímpares múltiplos de 3 no intervalo de 1 a 500 é igual a {soma}.')
