# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.

from random import randint
from time import sleep

cores = {
    'branco': '\033[0;30m',
    'vermelho': '\033[0;31m',
    'verde': '\033[0;32m',
    'amarelo': '\033[0;33m',
    'azul': '\033[0;34m',
    'magenta': '\033[0;35m',
    'ciano': '\033[0;36m',
    'cinza': '\033[0;37m',
    'brancoNegrito': '\033[1;30m',
    'vermelhoNegrito': '\033[1;31m',
    'verdeNegrito': '\033[1;32m',
    'amareloNegrito': '\033[1;33m',
    'azulNegrito': '\033[1;34m',
    'magentaNegrito': '\033[1;35m',
    'cianoNegrito': '\033[1;36m',
    'cinzaNegrito': '\033[1;37m',
    'limpar': '\033[m',
}

númeroAleatório = randint(0, 5)
númeroDoUsuário = int(input('\nPensei em um número inteiro entre 0 e 5. Tente advinhar qual é: '))

print('\nProcessando...')
sleep(2)

if númeroDoUsuário == númeroAleatório:
    print(f'\n{cores["cianoNegrito"]}Você venceu!!!{cores["limpar"]}')
else:
    print(f'\n{cores["vermelhoNegrito"]}Você perdeu!{cores["limpar"]}')

print(f'Eu pensei no número: {númeroAleatório}')
print(f'Você disse: {númeroDoUsuário}')
