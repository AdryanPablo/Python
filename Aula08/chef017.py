# Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo,
# calcule e mostre o comprimento da hipotenusa.

from math import hypot

catop = float(input('Digite o valor do cateto oposto: '))
catad = float(input('Digite o valor do cateto adjacente: '))

hipot = hypot(catop, catad)

print(f'Com os catetos {catop} e {catad} a hipotenusa vale {hipot}.')
