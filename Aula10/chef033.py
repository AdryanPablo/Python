# Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

número1 = int(input('\nDigite o 1º número: '))
número2 = int(input('Digite o 2º número: '))
número3 = int(input('Digite o 3º número: '))

maior = número1
menor = número1

if número2 > maior:

    maior = número2

if número3 > maior:

    maior = número3

if número2 < menor:

    menor = número2

if número3 < menor:

    menor = número3

print(f'\nO maior número digitado foi {maior}.')
print(f'\nO menor número digitado foi {menor}.')
