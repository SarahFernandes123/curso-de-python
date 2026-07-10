"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário descrito exiba a saudação apropriada.
Exemplo: Bom dia 0-11, boa tarde 12-17, boa noite, 18 -23.7
"""

entrada = (input("Digite a hora em numeros inteiros: "))

try:
    hora = int(entrada)
    if hora >= 0 and hora <=11:
        print('Bom dia, querido usuário')
    elif hora >=12 and hora <=17:
       print('Boa tarde, querido usuário')
    elif hora >=18 and hora <=23:
        print('Boa noite, querido usuário')
    else:
        print('Não conheço essa hora')
except:
    print('Por favor, digite apenas números inteiros')