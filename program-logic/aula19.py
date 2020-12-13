"""
Operador ternario em Python
"""

logged_user = False
msg = 'Usuario logado.' if logged_user else 'Usuario precisa logar.'
print(msg)


idade = input('Qual a sua idade? ')

if not idade.isnumeric():
    print('Digite apenas numeros')
else:
    e_de_maior = (int(idade) >= 18)
    msg = 'Pode acessar.' if e_de_maior else 'Nao pode acessar.'
    print(msg)