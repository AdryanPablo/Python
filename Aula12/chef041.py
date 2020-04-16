# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta
# e mostre a sua categoria, de acordo com a idade:
# Até 9 anos: Mirim
# Até 14 anos: Infantil
# Até 19 anos: Júnior
# Até 25 anos: Sênior
# Acima: Master

from time import gmtime

anoDeNascimento = int(input('\nEm que ano você nasceu? '))
anoAtual = gmtime().tm_year

idade = anoAtual - anoDeNascimento

if idade == 1:
    print('\nVocê tem 1 ano.')
else:
    print(f'\nVocê tem {idade} anos.')

if idade <= 9:
    print('Classificação: Mirim')
elif idade <= 14:
    print('Classificação: Infantil')
elif idade <= 19:
    print('Classificação: Júnior')
elif idade <= 25:
    print('Classificação: Sênior')
else:
    print('Classificação: Master')
