"""
Desconto

Peça o valor de uma compra.
Se o valor for maior ou igual a R$100, aplique 10% de desconto.
Caso contrário, mantenha o valor original.

"""

valor = input('Digite o valor da sua compra: ')
valor_certo = float(valor)
valor_desconto = (valor_certo * 0.9)

if valor_certo >= 100:
    valor_desconto = (valor_certo * 0.9)
    print('O valor a pagar com desconto é de:R$', valor_desconto)
else:
    print('O valor a pagar é de:R$', valor_certo)