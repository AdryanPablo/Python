# Crei um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.

"""for contador in range(1, 51):

    if contador % 2 == 0:

        if contador == 50:

            print(f'{contador}.')

        else:

            print(f'{contador}, ', end='')
"""

for contador in range(2, 51, 2):

    if contador == 50:

        print(f'{contador}.')

    else:

        print(f'{contador}, ', end='')
