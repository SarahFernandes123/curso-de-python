
"""
Peça um número e mostre a tabuada dele.

"""


numero = input('Digite um número: ')
numero_certo = int(numero)
multiplicador = 1

print(f'Tabuada do {numero_certo}')

while multiplicador<=10:
    resultado = numero_certo*multiplicador
    print(f'{numero_certo} x {multiplicador} = {resultado}')
    multiplicador +=1