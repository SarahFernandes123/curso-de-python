'''
Peça um número ao usuário e exiba sua tabuada de 1 a 10.

'''

numero = input('Digite um número: ')
num_certo = int(numero)

for i in range(1,11):
    resultado = num_certo *i
    print(f'o resultado é {num_certo} * {i}:', resultado)