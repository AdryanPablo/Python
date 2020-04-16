# Desenvolva uma lógica que calcule o peso e a altura de uma pessoa, calcule seu IMC
# e mostre seu status, de acordo com a tabela abaixo:
# Abaixo de 18.5: Abaixo do Peso;
# Entre 18.5 e 25: Peso ideal;
# 25 até 30: Sobrepeso;
# 30 até 40: Obesidade;
# Acima de 40: Obesidade Mórbida.

peso = float(str(input('\nInforme o seu peso (em quilogramas): ')).replace(',', '.'))
altura = float(str(input('Informe a sua altura (em metros): ')).replace(',', '.'))

imc = peso / altura ** 2

print(f'\nCom o peso {peso} kg e altura {altura} m o IMC é {imc}.')

if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc < 25:
    print('Você está no peso ideal.')
elif imc < 30:
    print('Você está em sobrepeso.')
elif imc < 40:
    print('Você está em obesidade.')
else:
    print('Você está em obesidade mórbida.')
