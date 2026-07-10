"""
Número positivo ou negativo

Peça um número.
Se for maior ou igual a 0, informe que é positivo.
Caso contrário, informe que é negativo.

"""

numero = input('Digite um número: ')
numero_certo = float(numero)

if numero_certo >=0:
    print('O número informado é positivo.')
else:
    print('O numero informado é negativo.')