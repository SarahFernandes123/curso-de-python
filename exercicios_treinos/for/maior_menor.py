'''
Peça 10 números e informe:

maior;
menor.

'''

maior = None
menor = None

for i in range(1,11):
    num = input(f'Digite o {i} numero: ')
    num_certo = int(num)

    if maior is None and menor is None:
        maior = num_certo
        menor = num_certo
    else:
        if num_certo > maior:
            maior = num_certo
        if num_certo < menor:
            menor = num_certo

if maior and menor is not None:
    print('O menor número é:', menor)
    print('O maior número é:', maior)