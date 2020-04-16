# Crie um programa que faça o computador jogar Jokenpô com você.

from random import randint
from time import sleep

escolhaDoComputador = randint(1, 3)

if escolhaDoComputador == 1:
    escolhaDoComputador = 'Pedra'
elif escolhaDoComputador == 2:
    escolhaDoComputador = 'Papel'
else:
    escolhaDoComputador = 'Tesoura'

escolhaDoUsuário = str(input('\nPedra, Papel ou Tesoura? ')).title()

print('\nJO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ!')

if escolhaDoUsuário in 'Pedra Papel Tesoura':

    print(f'\nVocê escolheu {escolhaDoUsuário}.')
    print(f'O computador escolheu {escolhaDoComputador}.')

    if escolhaDoUsuário == 'Pedra' and escolhaDoComputador == 'Pedra':
        print('Opa! Deu empate!')
    elif escolhaDoUsuário == 'Pedra' and escolhaDoComputador == 'Papel':
        print('Que pena! Você perdeu!')
    elif escolhaDoUsuário == 'Pedra' and escolhaDoComputador == 'Tesoura':
        print('Parabéns! Você ganhou!')
    elif escolhaDoUsuário == 'Papel' and escolhaDoComputador == 'Pedra':
        print('Parabéns! Você ganhou!')
    elif escolhaDoUsuário == 'Papel' and escolhaDoComputador == 'Papel':
        print('Opa! Deu empate!')
    elif escolhaDoUsuário == 'Papel' and escolhaDoComputador == 'Tesoura':
        print('Que pena! Você perdeu!')
    elif escolhaDoUsuário == 'Tesoura' and escolhaDoComputador == 'Pedra':
        print('Que pena! Você perdeu!')
    elif escolhaDoUsuário == 'Tesoura' and escolhaDoComputador == 'Papel':
        print('Parabéns! Você ganhou!')
    elif escolhaDoUsuário == 'Tesoura' and escolhaDoComputador == 'Tesoura':
        print('Opa! Deu empate!')

else:

    print('\nJogada inválida!')
