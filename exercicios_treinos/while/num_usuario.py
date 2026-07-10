"""
Peça um número ao usuário e conte de 1 até esse número.

"""

numero = input('Digite um número: ')
num_certo = int(numero)
contador = 1 


while contador <= num_certo:
    print(contador)
    contador +=1
