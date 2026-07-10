"""
Senha

Defina uma senha (por exemplo: 1234).
Peça ao usuário para digitá-la.
Se estiver correta, mostre "Acesso permitido".
Caso contrário, "Senha incorreta".

"""

senha_certa = '123456'
senha = input('Digite uma senha númerica: ')

if senha == senha_certa:
    print('Acesso permitido')
else:
    print('Senha incorreta')


