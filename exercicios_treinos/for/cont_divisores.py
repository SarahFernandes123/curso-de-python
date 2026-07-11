'''
Peça um número e conte quantos divisores ele possui.

'''

divisores = 0
numero = input('Digite um número: ')
num = int(numero)

for i in range (1, num+1):
    if num % i == 0:
        divisores+=1

print(f'O numero de divisores são:', divisores)