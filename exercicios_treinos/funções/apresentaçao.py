"""
Crie uma função chamada apresentar() que receba um nome e uma profissão.

"""
#Forma 1 de resolver

def apresentar (nome, profissao):
    
    return f'Olá! Meu nome é {nome}, e minha profissão é {profissao}'
    

falar_nome = apresentar('teste', 'teste')



print(falar_nome)




#Forma 2 de resolver


nome = input('Digite seu nome: ')
profissao = input('Digite sua profissão: ')

def apresentar (nome, profissao):
    
    return f'Olá! Meu nome é {nome}, e minha profissão é {profissao}'
    

print(apresentar(nome,profissao))
