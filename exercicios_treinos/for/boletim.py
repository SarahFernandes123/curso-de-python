'''
Crie um programa que:

pergunte quantos alunos existem na turma;
utilize um for para ler a nota de cada aluno;
ao final, informe:
maior nota;
menor nota;
média da turma;
quantidade de alunos aprovados (nota ≥ 7);
quantidade de alunos reprovados.

'''

alunos = int(input('Quantos alunos existem na turma: '))

maior_nota = None
menor_nota = None
qte_aprovados = 0
qte_reprovados = 0
qte_medias = 0
soma = 0

for i in range (1,alunos +1):
    nota = float(input(f'Qual a nota do aluno {i}: '))
    qte_medias +=1
    soma += nota
    
    media = soma / qte_medias
    
    if nota >= 7:
        qte_aprovados +=1
    else:
        qte_reprovados +=1

    if maior_nota is None and menor_nota is None:
        maior_nota = nota
        menor_nota = nota
    
    else:
        if nota > maior_nota:
            maior_nota = nota
        if nota < menor_nota:
            menor_nota = nota

if maior_nota and menor_nota is not None:
    print('A maior nota foi:', maior_nota)
    print('A menor nota foi:', menor_nota)

print('A quantidade de alunos aprovados foi:', qte_aprovados)
print('A quantidade de alunos reprovados foi:', qte_reprovados)
print('A média da sala foi de:', media)