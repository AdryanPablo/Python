# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salário superiores a R$1250,00, calcule um aumento de 10%.
# Para os inferiores ou iguais o aumento é de 15%.

salário = float(input('\nInforme o salário: R$ '))
porcentagem = ''

if salário > 1250:

    aumento = salário * 0.1
    porcentagem = '10%'

else:

    aumento = salário * 0.15
    porcentagem = '15%'

print(f'\nO novo salário será de R${salário + aumento:.2f}.')
print(f'Um aumento de R${aumento:.2f}, ou seja, {porcentagem}.')
