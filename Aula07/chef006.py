# Crie um programa que leia um número e mostre o seu dobro, triplo e raiz quadrada.

print("Se for digitar um número decimal, use ponto ao invés de vírgula!")
num = float(input("Digite um número: "))

print("\nO dobro de {} é {}, seu triplo é {} e sua raiz quadrada é {:.2f}.".format(num, num * 2, num * 3, num ** (1/2)))
