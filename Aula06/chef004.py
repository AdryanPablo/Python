# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações
# possíveis sobre ele.

algo = input('Digite alguma coisa: ')

print('\nO tipo primitivo de {} é {}.'.format(algo, type(algo)))
print('Isso é composto apenas por números? {}'.format(algo.isnumeric()))
print('Isso é composto apenas por letras? {}'.format(algo.isalpha()))
print('Isso é composto por letras e números? {}'.format(algo.isalnum()))
print('Isso é está capitalizado? {}'.format(algo.isupper()))
