# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares.
# Se o valor digitado for ímpar, desconsidere-o.

soma = 0
contador = 0

for números in range(0, 6):

    número = int(input(f'Digite o {números + 1}º número: '))

    if número % 2 == 0:

        soma += número
        contador += 1

print(f'A soma dos {contador} números pares digitados é igual a {soma}.')
