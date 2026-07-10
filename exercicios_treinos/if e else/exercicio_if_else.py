"""
Maior de idade

Peça a idade do usuário.
Se a idade for maior ou igual a 18, mostre "Maior de idade".
Caso contrário, mostre "Menor de idade".

"""

idade = input('Digite sua idade: ')
idade_certa = int(idade)

if idade_certa >= 18:
    print('Você é maior de idade')
else:
    print('Você é menor de idade')