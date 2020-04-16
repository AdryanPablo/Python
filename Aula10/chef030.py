# Crie um programa que leia um número inteiro e mostre na tela se ele é par ou ímpar.

número = int(input('\nDigite um número inteiro qualquer: '))


if número % 2 == 0:

    parOuImpar = 'par'

else:

    parOuImpar = 'ímpar'

print(f'\n{número} é {parOuImpar}.')
