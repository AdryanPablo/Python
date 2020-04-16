# Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.

c = float(input("Informe a temperatura em ºC: "))
f = c * (9 / 5) + 32

print("\n{}ºC = {}ºF".format(c, f))
