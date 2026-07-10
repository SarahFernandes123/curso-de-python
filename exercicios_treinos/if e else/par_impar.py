"""
Par ou ímpar

Peça um número.
Se ele for par, mostre "Número par".
Caso contrário, "Número ímpar".

"""


numero = (input("Digite um número: "))
numero_certo = float(numero)

if numero_certo % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")