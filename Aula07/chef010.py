# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere US$1.00 = R$3.27.

reais = float(input("Quantos reais você tem na carteira? R$"))
cotdol = float(input("Qual a cotação do dólar hoje? 1$ == R$"))

dolares = reais / cotdol

print("Com R${:.2f} você pode comprar ${:.2f}.".format(reais, dolares))
