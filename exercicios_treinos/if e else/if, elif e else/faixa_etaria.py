'''
Faixa etária

Peça a idade de uma pessoa.

Menor que 12 → Criança
Entre 12 e 17 → Adolescente
Entre 18 e 59 → Adulto
60 ou mais → Idoso

'''

idade = input('Digite sua idade: ')
idade_certa = int(idade)

if idade_certa < 12:
    print('Criança')
elif 12 <= idade_certa <=17:
    print('Adolescente')
elif 18 <= idade_certa <=59:
    print('Adulto')
else:
    print('Idoso')