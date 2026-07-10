"""
Peça números até digitar 0.

Mostre:

soma
média

"""

soma = 0
quantidade = 0

while True:
    numero = input('Digite um número: ')
    num_certo = int(numero)
    soma += num_certo
    quantidade +=1
    
    if quantidade > 0:
        media = soma/quantidade

    if num_certo == 0:
        print('A soma total de números foi: ',soma)
        print('A média dos números é:', media)
        break
    