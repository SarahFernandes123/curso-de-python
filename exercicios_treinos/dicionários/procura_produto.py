"""
Crie um dicionário chamado estoque:

estoque = {
    "arroz": 10,
    "feijao": 5,
    "macarrao": 8
}

Peça ao usuário para digitar o nome de um produto.

Verifique se esse produto existe no dicionário.

"""


estoque = {
    "arroz": 10,
    "feijao": 5,
    "macarrao": 8
    
}


produto = input('Digite o produto que deseja consultar: ')


if produto in estoque:
    print('Produto encontrado.')
else:
    print('Produto não encontrado.')