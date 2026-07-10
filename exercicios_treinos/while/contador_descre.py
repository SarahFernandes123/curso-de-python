"""
Peça um número inteiro positivo.

Depois faça uma contagem regressiva até zero.

"""

# contador = 10
# numero = input('Digite um número inteiro: ')
# num_certo = int(numero)

# while contador >=0:
#     print(contador)
#     contador -=1
    
#     if num_certo < 0:
#         print('Digite um número inteiro.')
    
  
numero = input('Digite um número inteiro: ')
num_certo = int(numero)
contador = num_certo

while contador >=0:
    print(contador)
    contador -=1
    
    if num_certo < 0:
        print('Digite um número inteiro.')
    
    