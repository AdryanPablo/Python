# Desenvolva um programa que leia o primeiro termo e a razão de uma P.A.
# No final, mostre os 10 primeiros termos dessa progressão.

primeiroTermo = int(input('Informe o 1º termo da P.A.: '))
razão = int(input('Informe a razão da P.A.: '))
progressão = primeiroTermo

for contador in range(0, 10):

    print(f'{progressão} ', end='')

    progressão += razão
