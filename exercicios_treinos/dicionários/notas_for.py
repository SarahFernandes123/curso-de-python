'''
9. Percorrendo um dicionário

Considere:

notas = {
    "Ana": 8,
    "Carlos": 6,
    "Mariana": 9,
    "João": 7
}

Utilize um for para mostrar:


'''

notas = {
    "Ana": 8,
    "Carlos": 6,
    "Mariana": 9,
    "João": 7
}

for aluno, nota in notas.items():
    print(f'A nota do {aluno} foi:', nota )