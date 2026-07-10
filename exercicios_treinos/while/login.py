"""
Crie um menu de login.

Usuário: admin
Senha: 1234

Enquanto algum dos dois estiver errado, peça novamente.

Quando acertar:

Bem-vindo!
"""

usuário ='admin'
senha = '1234'


while True:
    usu_digitado = input('Digite seu usuário: ')
    senha_digi = input('Digite sua senha: ')
    
    if usuário != usu_digitado or senha != senha_digi:
       print('Senha ou usuário inválido.')
       continue
    if usuário == usu_digitado and senha == senha_digi:
        print('Bem-vindo')
        break

