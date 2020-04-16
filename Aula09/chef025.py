# Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome.

nome = str(input('Digite seu nome completo: ')).strip()

print(f'Seu nome é {nome}.')
print(f'Tem "Silva" no seu nome? {"Silva " in nome}')
