# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário
# ou então o empréstimo será negado.

valorDaCasa = float(input('Qual o valor da casa? R$'))
salário = float(input('Qual é o seu salário? R$'))
duraçãoEmAnos = int(input('Em quantos anos você deseja pagar? '))
númeroDePrestações = duraçãoEmAnos * 12

mensalidade = valorDaCasa / númeroDePrestações

print(f'\nValor: R${valorDaCasa}')
print(f'Salário: R${salário}')
print(f'Duração: {duraçãoEmAnos} anos.')
print(f'Prestações: {númeroDePrestações}')
print(f'Mensalidade: R${mensalidade:.2f}')

if mensalidade > salário * 0.3:
    print('\nInfelizmente o empréstimo foi RECUSADO!')
else:
    print('\nParabéns! Seu empréstimo foi APROVADO!.')
