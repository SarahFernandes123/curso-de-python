'''
Peça uma senha ao usuário.

Enquanto a senha estiver errada, peça novamente.

A senha correta é:
123456
'''


senha_correta = '123456'

while True:
    senha = input('Digite sua senha: ')
    if senha == senha_correta:
        print('Acesso permitido')
        break
    else:
        print('Senha incorreta. Tente novamente.')

