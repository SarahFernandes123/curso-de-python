'''
Peça 5 números e informe o maior.
'''

maior = None

for i in range (1,6):
    num = input(f'Digite o {i} número: ')
    num_certo = int(num)

    if maior is None:
        maior = num_certo
    else:
        if num_certo > maior:
            maior = num_certo

if maior is not None:
    print('O maior número digitado foi:', maior)