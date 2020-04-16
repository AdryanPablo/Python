# Desenvolva um programa que pergunte a distância de uma viagem em km.
# Calcule o preço da passagem, cobrando R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.

distânciaDaViagem = int(input('\nInforme a distância da viagem em km: '))

if distânciaDaViagem <= 200:

    preçoDaPassagem = distânciaDaViagem * 0.5

else:

    preçoDaPassagem = (distânciaDaViagem - 200) * 0.45 + 100

print(f'\nA viagem será de {distânciaDaViagem} km.')
print(f'O preço da passagem é R${preçoDaPassagem:.2f}.')
