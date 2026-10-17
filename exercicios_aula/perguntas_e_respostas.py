#Exercicio - sistemas de pergunta e resposta


perguntas = [
    {
        'Pergunta': 'Quanto é 2 + 2?',
        'Opções': ["1", '2', '3', '4', '5'],
        'Resposta': "4",
    },
    {
        'Pergunta': 'Quanto é 5*5?',
        'Opções': ['1','10','25','55'],
        'Resposta': '25',
    },
    {
        'Pergunta': 'Quanto é 10-5?',
        'Opções': ['1', '10', '5','8'],
        'Resposta': '5',
    }

]

qte_acertos = 0
for pergunta in perguntas:
    print('Pergunta:', pergunta['Pergunta'])

    print()

    opçoes = pergunta['Opções']

    for i, opcao in enumerate(opçoes):   #enumerate para colocar os indices de opções nas perguntas
        print(f'{i})', opcao)

    print()

    escolha = input('Escolha uma opção: ')

    acertou = False
    escolha_int = None
    qte_opcoes = len(opçoes)

    if escolha.isdigit():
        escolha_int = int(escolha)

    if escolha_int is not None:
        if escolha_int >=0 and escolha_int < qte_opcoes:
            if opçoes[escolha_int] == pergunta['Resposta']:
                acertou = True

    print()

    if acertou:
        qte_acertos +=1
        print('Acertou')
    else:
        print('Errou')

    print()


print('Você acertou', qte_acertos)
print('de', len(perguntas), 'perguntas')