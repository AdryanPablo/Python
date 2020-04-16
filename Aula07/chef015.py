# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60,00 por dia e R$0,15 por km rodado.

km = int(input("\nQuantos km foram percorridos? "))
dias = int(input("Por quantos dias o carro foi usado? "))

valor = km * 0.15 + dias * 60

print("\nComo você rodou {}km e usou o carro por {} dias, o valor a pagar é R${:.2f}.".format(km, dias, valor))
