# Escreva um programa que leia um valor em metros e exiba convertido em centímetros e milímetros.

print("\nSe for informar valores decimais, use o ponto ao invés da vírgula.")

'''metro = float(input("Digite uma medida em metros (m): "))

cent = metro * 100      # Converte o valor digitado em metro para centímetros.
mili = metro * 1000     # [...] para milimetros.

print("\n{}m é o mesmo que {}cm ou {}mm.".format(metro, cent, mili))'''

m = float(input("Digite uma media em metros (m): "))

km = m * 1000
hm = m * 100
dam = m * 10
dm = m / 10
cm = m / 100
mm = m / 1000

print("\n{:.0f}m == {:.0f}km".format(m, km))
print("{:.0f}m == {:.0f}hm".format(m, hm))
print("{:.0f}m == {:.0f}dam".format(m, dam))
print("{:.0f}m == {}dm".format(m, dm))
print("{:.0f}m == {}cm".format(m, cm))
print("{:.0f}m == {}mm".format(m, mm))
