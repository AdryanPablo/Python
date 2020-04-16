# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor pesos lidos.

maior = 0
menor = 0

for pessoas in range(0, 5):

    peso = float(input(f'Informe o peso da {pessoas + 1}ª pessoa: '))

    if peso > maior:

        maior = peso

    if pessoas == 0:

        menor = peso

    elif peso < menor:

        menor = peso

print(f'\nO maior peso lido foi {maior} e o menor foi {menor}.')
