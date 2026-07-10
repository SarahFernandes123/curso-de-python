"""
4. Conceito escolar

Peça uma nota.

9 a 10 → Conceito A
8 a 8,9 → Conceito B
7 a 7,9 → Conceito C
6 a 6,9 → Conceito D
Abaixo de 6 → Conceito E

"""

nota = input('Digite a sua nota: ')
nota_certa = float (nota)

if 9 <= nota_certa <= 10:
    print('Conceito A')
elif 8 <= nota < 9:
    print('Conceito B')
elif 7 <= nota < 8:
    print('Conceito C')
elif 6<= nota <7:
    print('Conceito D')
else: 
    print('Conceito E')