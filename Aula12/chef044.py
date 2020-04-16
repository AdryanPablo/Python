# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# à vista dinheiro / cheque: 10% de desconto;
# à vista no cartão: 5% de desconto;
# em até 2x no cartão: preço normal;
# 3x ou mais no cartão: 20% de juros.

print(f'\n{" Lojas Guanabara ":=^40}\n')

preço = float(input('Informe o preço do produto: R$'))
print('\n[ 1 ] À vista no dinheiro / cartão \n[ 2 ] À vista no cartão \n[ 3 ] 2x no cartão \n[ 4 ] 3x ou mais no cartão')
formaDePagamento = int(input('\nQual será a forma de pagamento? '))

if formaDePagamento == 1:

    desconto = preço * 0.1

    print('\nPagamento a vista com dinheiro ou cheque.')
    print(f'O preço do produto será de R${(preço - desconto):.2f}, um desconto de 10% (R${desconto:.2f}).')

elif formaDePagamento == 2:

    desconto = preço * 0.05

    print('\nPagamento a vista no cartão.')
    print(f'O preço do produto será de R${(preço - desconto):.2f}, um desconto de 5% (R${desconto:.2f}).')

elif formaDePagamento == 3:

    print('\nPagamento em 2x no cartão.')
    print(f'O preço do produto será de R${preço:.2f} (preço normal).')
    print(f'Cada prestação terá o valor de R${(preço / 2):.2f}.')

elif formaDePagamento == 4:

    númeroDeParcelas = int(input('Qual o número de parcelas? '))

    juros = preço * 0.2

    print(f'\nPagamento em {númeroDeParcelas}x no cartão.')
    print(f'O preço total do produto será de R${(preço + juros):.2f}, com juros de 20% (R${juros:.2f}).')
    print(f'Cada prestação terá o valor de R${((preço + juros) / númeroDeParcelas):.2f}.')

else:
    print('\nOpção inválida!')
