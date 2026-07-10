"""
9. Caixa eletrônico

Peça o saldo e o valor do saque.

Se o saque for menor ou igual ao saldo, permita o saque.
Se o saque for maior que o saldo, informe saldo insuficiente.
Se o saque for menor ou igual a zero, informe valor inválido.

"""

saldo = input('Informe o valor do seu saldo: ')
saque = input('Informe o valor que deseja retirar: ')

saldo_certo = float(saldo)
saque_certo = float(saque)

if saque_certo <= 0:
    print('Valor inválido')
elif saque_certo <= saldo_certo:
    print('Saque permitido')
else:
    print('Saldo insuficiente')