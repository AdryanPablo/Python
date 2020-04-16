# Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

número = int(input('Digite um número: '))

print(f'\n===== TABUADA de {número} =====\n')

for tabuada in range(1, 11):

    print(f'{número} x {tabuada:>2} = {número * tabuada}')
