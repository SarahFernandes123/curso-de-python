"""
Nota
Peça uma nota.
Se for maior ou igual a 7, mostre "Aprovado".
Caso contrário, "Reprovado".

"""
nota = input('Digite sua nota: ')
nota_1 = float(nota)

if nota_1 >=7:
    print('Você está aprovado.')
else:
    print('Você está reprovado.')