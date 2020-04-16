# Escreva um programa que leia a velocidade de um carro.
# Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
# A multa vai custar R$7,00 para cada km acima do limite.

velocidadeDoCarro = int(input('\nInforme a velocidade do carro: '))

if velocidadeDoCarro > 80:

    print('\nMULTADO!')
    print('Você ultrapassou o limite de velocidade!')

    multa = (velocidadeDoCarro - 80) * 7

    print(f'Por isso deverá pagar uma multa de R${multa},00')

else:

    print('\nDirija com cuidado!')
