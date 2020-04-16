# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uma frase: '))

fraseInversa = ''

for letras in range(len(frase) - 1, -1, -1):

    fraseInversa += f'{frase[letras]}'

frase = frase.capitalize()
fraseInversa = fraseInversa.capitalize()

print(f'\n\"{frase}\" ao contrário é \"{fraseInversa.replace(" ", "")}\".')

if frase.replace(' ', '') == fraseInversa.replace(' ', ''):

    print(f'\"{frase}\" é um palíndromo.')

else:

    print(f'\"{frase}\" não é um palíndromo.')
