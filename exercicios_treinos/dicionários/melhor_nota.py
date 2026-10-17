'''
Utilizando o dicionário:

notas = {
    "Ana": 8,
    "Carlos": 6,
    "Mariana": 9,
    "João": 7
}

Descubra:
quem tirou a maior nota;
qual foi a maior nota.


'''

notas = {
    "Ana": 8,
    "Carlos": 6,
    "Mariana": 9,
    "João": 7
}

maior_nota = None
melhor_aluno = None

maior_nota = None
quem_tirou = None

for nome, nota in notas.items():

    if maior_nota is None:
        maior_nota = nota
        quem_tirou = nome

    else:
        if nota > maior_nota:
            maior_nota = nota
            quem_tirou = nome

print("Quem tirou a maior nota:", quem_tirou)
print("Maior nota:", maior_nota)


## Outra forma de resolver:

maior_nota = max(notas.values())
quem_tirou = max(notas, key=notas.get)

print("Quem tirou a maior nota:", quem_tirou)
print("Maior nota:", maior_nota)