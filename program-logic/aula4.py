"""
Variaveis
"""

nome = 'Kaique'
idade = 18
altura = 1.76
peso = 60
data_atual = 2020
imc = peso / (altura ** 2)

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)

"""
Formatacao de sting
"""

print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')  # :.2f arrendondar numeros decimais
print('{} tem {} anos de idade e seu imc é {:.2f}'.format(nome, idade, imc))
print('{0} tem {2} anos de idade e seu imc é {1:.2f}'.format(nome, idade, imc))  # define a ordem das variaveis
print('{n} tem {p} anos de idade e seu imc é {q:.2f}'.format(n=nome, p=idade, q=imc))  # nomeia as variaveis
