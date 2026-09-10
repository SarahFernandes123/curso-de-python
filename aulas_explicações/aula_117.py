"""
Closure e funções que retornam outras funções
No closure a função interna leva consigo as variáveis que ela precisa do ambiente externo.

Closure é uma função que mantém acesso às variáveis do ambiente onde foi criada, mesmo depois que a função externa terminou.

"""


def criar_saudacao(saudacao):
    def saudar(nome):
        return f'{saudacao}, {nome}!'
    return saudar


falar_bom_dia = criar_saudacao('Bom dia')
falar_boa_noite = criar_saudacao('Boa noite')

for nome in ['Maria', 'Joana', 'Luiz']:
    print(falar_bom_dia(nome))
    print(falar_boa_noite(nome))