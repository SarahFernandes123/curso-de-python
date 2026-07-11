"""
Peça um número e desenhe um quadrado de asteriscos.

"""

quadrado = input('Digite o tamanho que deseja para seu quadrado: ')
quadra_certo = int(quadrado)

for _ in range (quadra_certo):
    print('*'*quadra_certo)