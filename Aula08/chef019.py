# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.

from random import choice

aluno1 = str(input("Digite o nome do 1º aluno: "))  # Recebe os nomes dos quatro alunos.
aluno2 = str(input("Digite o nome do 2º aluno: "))
aluno3 = str(input("Digite o nome do 3º aluno: "))
aluno4 = str(input("Digite o nome do 4º aluno: "))

alunos = [aluno1, aluno2, aluno3, aluno4]       # Reune todos os alunos em uma lista.
sorteio = choice(alunos)       # Realiza o sorteio.

print(f'Dentre os alunos {aluno1}, {aluno2}, {aluno3} e {aluno4}, {sorteio} apagará o quadro.')
