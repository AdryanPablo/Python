# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

nome = str(input("Digite o nome do(a) aluno(a): "))
not1 = float(input("Digite a 1ª nota de {}: ".format(nome)))
not2 = float(input("Digite a 2ª nota de {}: ".format(nome)))

media = (not1 + not2) / 2

print("Já que {} tirou {} e {}, sua média é {:.2f}.".format(nome, not1, not2, media))
