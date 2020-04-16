# Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

salario = float(input("\nInforme o salário do colaborador: R$"))

aumento = salario + (salario * 0.15)

print("\nO novo salário com 15% de aumento é R${}.".format(aumento))
