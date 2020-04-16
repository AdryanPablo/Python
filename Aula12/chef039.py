# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade:
# 1) Se ele ainda vai se alistar ao serviço militar;
# 2) Se é a hora de se alistar;
# 3) Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date

anoDeNascimento = int(input('\nEm que ano você nasceu? '))
sexo = int(input('Qual é o seu sexo? [ 1 ] Feminino; [ 2 ] Masculino: '))

anoAtual = date.today().year

idade = anoAtual - anoDeNascimento

if idade == 1:

    print('\nVocê tem 1 ano de idade.')

else:

    print(f'\nVocê tem {idade} anos.')

if sexo == 1:  # Feminino

    print('Por ser do sexo feminino, você não precisava fazer o alistamento militar obrigatório.')

elif sexo == 2:  # Masculino

    if idade < 18:

        tempo = 18 - idade

        if tempo == 1:
            print(f'Você se alistá daqui há 1 ano, em {anoAtual + tempo}.')
        else:
            print(f'Você se alistará daqui há {tempo} anos, em {anoAtual + tempo}.')

    elif idade == 18:

        print('Está na hora de se alistar ao serviço militar.')

    else:

        tempo = idade - 18

        if tempo == 1:

            print(f'Já passou 1 ano do seu alistamento, foi em {anoAtual - tempo}.')

        else:

            print(f'Já passou {tempo} anos do seu alistamento, foi em {anoAtual - tempo}.')

else:

    print('Opção inválida!')
