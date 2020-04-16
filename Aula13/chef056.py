# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
#
# 1) A média de idade do grupo;
# 2) Qual é o nome do homem mais velho;
# 3) Quantas mulheres têm menos de 20 anos.
#

idadeDoGrupo = 0
idadeDoHomemMaisVelho = 0
nomeDoHomemMaisVelho = 'ninguém'
mulheresMenores = 0

for pessoas in range(0, 4):

    nome = str(input(f'Qual é o nome da {pessoas + 1}ª pessoa? '))
    idade = int(input('Qual é a idade dela? '))
    sexo = str(input('Qual é o sexo dela? [M / F]: ')).upper()

    idadeDoGrupo += idade

    if sexo == 'M' and idade > idadeDoHomemMaisVelho:

        idadeDoHomemMaisVelho = idade
        nomeDoHomemMaisVelho = nome

    if sexo == 'F' and idade < 20:

        mulheresMenores += 1


print(f'\nA média de idade do grupo é {idadeDoGrupo / 4}.')
print(f'O homem mais velho é {nomeDoHomemMaisVelho} que tem {idadeDoHomemMaisVelho} anos.')
print(f'{mulheresMenores} mulheres têm menos de 20 anos.')
