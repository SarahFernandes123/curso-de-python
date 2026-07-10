"""
Crie um jogo onde o usuário precisa adivinhar um número.

Enquanto não acertar:
Digite um número:

Quando acertar:
Parabéns! Você acertou!

"""

numero_secreto = '20'
numero = input('Advinhe um número secreto: ')

while numero != numero_secreto:
    numero = input('Advinhe um número secreto: ')
    
    if numero == numero_secreto:
        print('Parabéns! Você acertou.')