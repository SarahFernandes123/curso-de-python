"""
Peça vários números.

O programa termina somente quando o usuário digitar 0.

"""

numero_finalizador = 0

while True:
    numero = input('Digite um número: ')
    numero_certo = int(numero)
    print(numero_certo)

    if numero_certo == numero_finalizador:
        print('Você achou o número que encerra o programa')
        break

