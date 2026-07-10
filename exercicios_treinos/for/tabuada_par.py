'''
Peça ao usuário um número e mostre a tabuada apenas dos números pares.

'''

num = input('Digite um número: ')
num_certo = int(num)

for i in range (1,11): 
    if i %2 ==0:
        resultado = num_certo*i
        print(f'O resultado é {num_certo} *{i}:', resultado)