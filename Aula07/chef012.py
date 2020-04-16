# Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

preco = float(input("\nDigite o preço do produto: R$"))
desconto = preco - (preco * 0.05)

print("\nO novo preço do produto com 5% de desconto é R${:.2f}.".format(desconto))
