# Manipulando chaves e valores em dicionários
pessoa = {}

##
##

chave = 'nome'   #criação de chave dentro do dicionário

pessoa[chave] = 'Luiz Otávio'  #atribuindo o valor a chave criada
pessoa['sobrenome'] = 'Miranda'


print(pessoa[chave])   #caso a chave não exista no dicionário, ao ser chamada acontecerá uma exceção que para o programa.

pessoa[chave] = 'Maria'

del pessoa['sobrenome']  #serve para apagar chave do dicionário
print(pessoa)
print(pessoa['nome'])

# print(pessoa.get('sobrenome'))
if pessoa.get('sobrenome') is None:    
    print('NÃO EXISTE')
else:
    print(pessoa['sobrenome'])

# print('ISSO Não vai')