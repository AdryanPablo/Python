# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite seu nome completo: ')).strip()

primeiroNome = nome.split()[0]
últimoNome = nome.split()[-1]

print(f'Seu primeiro nome é: {primeiroNome.title()}')
print(f'Seu último nome é: {últimoNome.title()}')
