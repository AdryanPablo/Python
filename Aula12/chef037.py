# Escreva um programa que leia um número inteiro e peça para o usuário escolher qual será a base de conversão:
# 1) Binário    2) Octal    3) Hexadecimal

número = int(input('\nDigite um número inteiro: '))
baseDeConversão = int(input('[ 1 ] Binário; [ 2 ] Octal; [ 3 ] Hexadecimal: '))

if baseDeConversão == 1:
    print('\n === Binário ===\n')
    print(f'{número} = {str(bin(número))[2:]}')
elif baseDeConversão == 2:
    print('\n === Octal ===\n')
    print(f'{número} = {str(oct(número))[2:]}')
elif baseDeConversão == 3:
    print('\n === Hexadecimal ===\n')
    print(f'{número} = {str(hex(número))[2:].upper()}')
else:
    print('\nOpção inválida!')
