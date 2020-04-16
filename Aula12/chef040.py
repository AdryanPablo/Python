# Crie um programa que leia duas notas de um aluno e calcule a sua média,
# mostrando uma mensagem no final, de acordo com a média atingida.
# Média abaixo de 5.0 = Reprovado;
# Média entre 5.0 e 6.9 = Em Recuperação;
# Média acima de 7.0 = Aprovado.

nota1 = float(input('\nInforme o valor da 1ª nota: '))
nota2 = float(input('Informe o valor da 2ª nota: '))

média = (nota1 + nota2) / 2

print(f'\nCom as notas {nota1} e {nota2} a média foi {média:.1f}.')

if média < 5.0:
    print('\nREPROVADO!')
elif média > 7.0:
    print('\nAPROVADO!')
else:
    print('\nEM RECUPERAÇÃO!')
