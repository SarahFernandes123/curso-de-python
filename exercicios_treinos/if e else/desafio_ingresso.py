"""
Compra de ingresso
Peça a idade.
Se a pessoa tiver 12 anos ou menos, informe que paga meia-entrada.
Caso contrário, paga inteira.

"""

valor_ingresso = 35.0
desconto = valor_ingresso *0.5

idade = input('Digite sua idade: ')
idade_certa = int(idade)

if idade_certa <=12:
    print('Você paga meia entrada. No valor de R$', desconto)
else:
    print('Você paga o valor inteiro de R$', valor_ingresso)