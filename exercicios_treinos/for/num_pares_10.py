'''
Peça 10 números e conte quantos são pares.

'''

pares = 0

for i in range(1,11):
    num = input(f'Digite o {i} número: ')
    num_certo = int(num)
    if num_certo % 2==0:
        pares +=1

print('A quantidade de números pares foi:', pares)