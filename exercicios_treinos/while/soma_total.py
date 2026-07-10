"""
Peça números ao usuário e some todos eles.

Quando ele digitar 0, mostre a soma total.

"""

encerra = 0
soma = 0


while True:
    numero = input('Digite um número: ')
    num_certo = int(numero)
    soma += num_certo

    if num_certo == 0:
        print('A soma total de números foi: ',soma)
        break
    
   