"""
Dia da semana
Peça um número de 1 a 7.
Mostre:

1 → Domingo
2 → Segunda-feira
3 → Terça-feira
4 → Quarta-feira
5 → Quinta-feira
6 → Sexta-feira
7 → Sábado

Se o usuário digitar outro número, informe que é inválido.

"""

numero = input('Escolha um número de 1 a 7: ')

if numero == "1":
    print('Domingo')
elif numero == '2':
    print('Segunda-Feira')
elif numero == '3':
    print('Terça-Feira')
elif numero == '4':
    print('Quarta-Feira')
elif numero == '5':
    print('Quinta-Feira')
elif numero == '6':
    print('Sexta-feira')
elif numero == '7':
    print('Sábado')
else:
    print('Digite um número válido')