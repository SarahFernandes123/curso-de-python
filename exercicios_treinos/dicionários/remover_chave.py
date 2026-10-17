'''
Considere:

usuario = {
    "nome": "João",
    "idade": 25,
    "email": "joao@email.com",
    "cidade": "Quixadá"
}

Remova a chave "email" e mostre o dicionário atualizado.

'''

usuario = {
    "nome": "João",
    "idade": 25,
    "email": "joao@email.com",
    "cidade": "Quixadá"
}

usuario.pop('email')

print(usuario)