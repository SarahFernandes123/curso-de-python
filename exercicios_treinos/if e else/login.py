'''
Login simples

Defina um usuário e uma senha.
Peça ambos ao usuário.
Se estiverem corretos, mostre "Login realizado".
Caso contrário, "Usuário ou senha incorretos".

'''

usuario_certo = 'Sarah'
senha_certa = '123456'

usuario = input('Digite o nome do usuário: ')
senha = input('Digite a senha do usuário: ')

if senha == senha_certa and usuario == usuario_certo:
    print('Login realizado')
else:
    print('Usuário ou senha incorreta')