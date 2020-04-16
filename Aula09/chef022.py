# Crie um programa que leia o nome completo de uma pessoa e mostre:
#
# 1) O nome com todas as letras maiúsculas.
# 2) O nome com todas as letras minúsculas.
# 3) Quantas letras ao todo (sem considerar espaços)
# 4) Quantas letras tem o primeiro nome.

nome = str(input('Digite o seu nome completo: ')).strip()

print(f'\nSeu nome é {nome.title()}.')
print(f'Seu nome em letras maiúsculas: {nome.upper()}.')
print(f'Seu nome em letras minúsculas: {nome.lower()}.')
print(f"Seu nome completo tem {len(nome.replace(' ', ''))} letras.")
print(f"Seu primeiro nome é {nome.split()[0]} e tem {len(nome.split()[0])} letras.")
