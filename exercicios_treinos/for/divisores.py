'''
Peça um número e mostre todos os seus divisores.

'''

numero = input('Digite um número: ')
num = int(numero)

for i in range (1, num +1):
    if num % i == 0:
        print(i)