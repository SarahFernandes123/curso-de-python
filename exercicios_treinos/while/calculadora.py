'''
Faça uma calculadora.

Enquanto o usuário não escolher sair, mostre:

1 - Somar
2 - Subtrair
3 - Multiplicar
4 - Dividir
5 - Sair

Após cada operação, o menu deve aparecer novamente.

'''

while True:
    num_1= input('Digite um número: ')
    num_2 = input('Digite um segundo número: ')
    operador = input('Escolha um operador (1 - Somar, 2 - Subtrair, 3 - Multiplicar*, 4 - Dividir): ')
    
    
    num_1_certo = float(num_1)
    num_2_certo = float(num_2)

    print('Estamos realizando sua conta, confira abaixo: ')

    if operador == '1':
        print(f'A soma de {num_1_certo} + {num_2_certo} é:', num_1_certo + num_2_certo)
    elif operador == '2':
        print(f'A subtração do {num_1_certo} - {num_2_certo} é:', num_1_certo - num_2_certo)
    elif operador == '3':
        print(f'A multiplicação do {num_1_certo} * {num_2_certo} é:', num_1_certo*num_2_certo)
    elif operador == '4':
        print(f'A divisão entre {num_1_certo} / {num_2_certo} é:', num_1_certo/num_2_certo)
    else:
        print('Escolha um operador válido.')
    
    sair = input('Caso deseje sair escolha 5: ').startswith('5')

    if sair is True:
        print('Programa encerrado.')
        break