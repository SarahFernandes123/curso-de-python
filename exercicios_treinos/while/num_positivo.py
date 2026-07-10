"""
Peça números positivos.

Se o usuário digitar um número negativo, ignore esse número e peça outro.

O programa termina quando digitar 0.

No final mostre a soma apenas dos positivos.

"""

soma = 0

while True:
    numero = input('Digite um número positivo: ')
    num_certo = float(numero)
   
    if num_certo == 0:
        break

    if num_certo < 0:
        print('Digite um número positivo.')
        continue
    
    soma += num_certo
    
print(soma)