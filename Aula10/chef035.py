# Desenvolva um programa que leia o comprimento de 3 retas e diga ao usuário se elas podem ou não formar um triângulo.

reta1 = int(input('\nInforme o valor da 1ª reta: '))
reta2 = int(input('Informe o valor da 2ª reta: '))
reta3 = int(input('Informe o valor da 3ª reta: '))

if reta1 < reta2 + reta3 and reta2 < reta1 + reta2 and reta3 < reta1 + reta2:

    print(f'\nAs retas {reta1}, {reta2} e {reta3} podem formar um triângulo.')

else:

    print(f'\nAs reta {reta1}, {reta2} e {reta3} não podem formar um triângulo.')
