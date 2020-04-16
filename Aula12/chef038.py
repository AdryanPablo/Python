# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# 1) O primeiro valor é o maior;
# 2) O Segundo valor é o maior;
# 3) Os dois valores são iguais.

número1 = int(input('\nDigite um número: '))
número2 = int(input('Digite outro: '))

if número1 > número2:
    print(f'\n{número1} é maior!')
elif número1 < número2:
    print(f'\n{número2} é maior!')
else:
    print('\nOs números são iguais.')
