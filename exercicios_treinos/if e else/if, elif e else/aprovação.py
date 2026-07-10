"""
Aprovação

Peça a nota do aluno.

Se a nota for maior ou igual a 7, mostre "Aprovado".
Se a nota estiver entre 5 e 6,9, mostre "Recuperação".
Caso contrário, mostre "Reprovado".

"""

nota = input('Digite sua nota: ')
nota_certa = float(nota)

if nota_certa >= 7:
    print('Você foi aprovado.')
elif 5 <= nota_certa <=6.9:
    print('Você está de recuperação')
else:
    print('Você foi reprovado.')