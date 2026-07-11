'''
Peça 5 números e informe o menor.

'''

menor = None

for i in range(1,6):
    num = input(f'Digite o {i} número: ')
    num_certo = int(num)

    if menor is None:
        menor = num_certo
    else:
        if num_certo<menor:
            menor = num_certo

if menor is not None:
    print(f'O menor número é:', menor)
