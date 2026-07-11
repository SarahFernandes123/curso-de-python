"""
Peça 10 números e conte quantos são positivos.

"""

positivos = 0

for i in range(1,11):
    num_1 = int(input(f'Digite o {i} número: '))
    if num_1>0:
        positivos += 1
    

print('A quantidade de positivos são:', positivos)