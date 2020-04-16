# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

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

número = int(input('Digite um número: '))

quantidadeDeDivisões = 0

for contador in range(1, número + 1):

    if número % contador == 0:

        quantidadeDeDivisões += 1

        # Verifica se é o último número.
        if contador == número:

            print(f'{cores["ciano"]}{contador}{cores["limpar"]}.')

        else:

            print(f'{cores["ciano"]}{contador}{cores["limpar"]}, ', end='')

    else:

        print(f'{cores["vermelho"]}{contador}{cores["limpar"]}, ', end='')

if quantidadeDeDivisões == 2:

    print(f'\n{número} é um número primo.')

else:

    print(f'\n{número} não é um número primo.')
