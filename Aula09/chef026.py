# Faça um programa que leia uma frase pelo teclado e mostre:
#
# 1) Quantas vezes aparece a letra 'A';
# 2) Em que posição ela aparece a primeira vez;
# 3) Em que posição ela aparece pela última vez.

frase = str(input('Digite uma frase: ')).lower().strip()

print(f'A letra "A" aparece {frase.count("a")} vezes.')
print(f'Ela aparece pela primeira vez na {frase.find("a") + 1}ª posição.')
print(f'Ela aparece pela última vez na {frase.rfind("a") + 1}ª posição.')
