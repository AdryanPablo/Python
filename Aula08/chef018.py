# Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente.

from math import sin, cos, tan, radians

ang = int(input('Digite um ângulo: '))

sen = sin(radians(ang))
cos = cos(radians(ang))
tan = tan(radians(ang))

print(f'O ângulo digitado foi {ang}º.')
print(f'Sen de {ang}º = {sen:.2f}')
print(f'Cos de {ang}º = {cos:.2f}')
print(f'Tan de {ang}º = {tan:.2f}')
