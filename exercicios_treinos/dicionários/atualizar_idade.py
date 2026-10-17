'''
Considere:

aluno = {
    "nome": "Maria",
    "idade": 20,
    "curso": "Sistemas de Informação"
}

Altere a idade para 21 e depois mostre o dicionário atualizado.

'''

aluno = {
    "nome": "Maria",
    "idade": 20,
    "curso": "Sistemas de Informação"
}


aluno.update( {
    'idade': 21
})

aluno.update(idade=21)

print(aluno)