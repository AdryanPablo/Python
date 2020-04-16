# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

anoAtual = date.today().year
maiores = 0
menores = 0

for pessoas in range(0, 7):

    anoDeNascimento = int(input(f'Qual o ano de nascimento da {pessoas + 1}ª pessoa: '))

    if anoAtual - anoDeNascimento >= 18:

        maiores += 1

    else:

        menores += 1

print(f'\n{maiores} são maiores de idade e {menores} são menores.')
