"""
Peça 5 números ao usuário e mostre a soma deles.

"""

soma = 0

for i in range(5):
    num_1 = int(input('Digite um número: '))
    soma += num_1

    print('A soma dos 5 números são: ', soma)