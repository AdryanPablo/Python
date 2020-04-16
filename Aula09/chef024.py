# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "Santo".

cidade = str(input('Digite o nome de uma cidade: ')).strip()

print(f'Essa cidade começa com "Santo"? {"Santo" in (cidade.title().split()[0])}')
