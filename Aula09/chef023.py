# Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

número = int(input('Digite um número [0 a 9999]: '))

'''milhar = número % 10000 // 1000
centena = número % 1000 // 100
dezena = número % 1000 % 100 // 10
unidade = número % 1000 % 100 % 10'''

unidade = número // 1 % 10      # Exemplo: 1234 // 1 == 1234;   1234 % 10 = 4
dezena = número // 10 % 10      # Exemplo: 1234 // 10 = 123;    123 % 10 = 3
centena = número // 100 % 10    # Exemplo: 1234 // 100 = 12;    12 % 10 = 2
milhar = número // 1000 % 10    # Exemplo: 1234 // 1000 = 1;    1 % 10 = 1

print(f'Milhar:  {milhar}')
print(f'Centena: {centena}')
print(f'Dezena:  {dezena}')
print(f'Unidade: {unidade}')
