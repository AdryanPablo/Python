# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e mostre a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta, pinta uma área de 2m².

largura = float(input("\nQual a largura da parede (em metros)? "))
altura = float(input("Qual a altura da parede (em metros)? "))

area = largura * altura
tinta = area / 2

print("\nCom {}m de largura e {} de altura, a área da parede é de {:.2f}m.".format(largura, altura, area))
print("Para pintá-la você precisará de {:.2f}l de tinta.".format(tinta))
