# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.

from random import shuffle  # Importa a função shuffle.

aluno1 = str(input('Digite o nome do 1º aluno: '))  # Pede ao usuário para informar os nomes dos alunos.
aluno2 = str(input('Digite o nome do 2º aluno: '))
aluno3 = str(input('Digite o nome do 3º aluno: '))
aluno4 = str(input('Digite o nome do 4º aluno: '))

alunos = [aluno1, aluno2, aluno3, aluno4]  # Cria uma lista ("de chamada") com os nomes dos alunos.

shuffle(alunos)  # Embaralha um lista.

print(f'A ordem de apresentação é: \n1º: {alunos[0]} \n2º: {alunos[1]} \n3º: {alunos[2]} \n4º: {alunos[3]}')
