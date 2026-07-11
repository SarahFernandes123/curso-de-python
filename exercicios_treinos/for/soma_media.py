'''
Peça 8 números e informe:

soma;
média.

'''

soma = 0
quantidade = 0

for i in range(1,9):
    num = input(f'Digite o {i} numero: ')
    num_certo = int(num)
    soma += num_certo
    quantidade +=1
    
    if quantidade > 0:
        media = soma / quantidade

print(f'A soma dos numeros foi {soma}, e a média foi {media}')