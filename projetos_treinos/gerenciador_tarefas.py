print("Gerenciador de Tarefas") #nome do programa para o usuário

print()

tarefas = []

while True: 
    opcoes = int(input('Escolha uma das opções: \n''1)Cadastrar tarefas\n' '2)Listar tarefas\n' '3)Concluir tarefas\n'
                '4)Buscar tarefas\n' '5)Ver estatísticas\n' '0) Sair\n'
               ))  #escolha das opções de funcionamento do gerenciador

    if opcoes == 1:
        nova_tarefa = input('Digite o nome da sua tarefa: ')
        tarefas_adicionadas = {
            "nome_tarefa": nova_tarefa,
            "concluida": False
        }
        tarefas.append(tarefas_adicionadas)
        
    elif opcoes ==2:
            for i, tarefa in enumerate(tarefas, start=1):
             print(f'{i})',tarefa['nome_tarefa'], tarefa['concluida'])   
    
    elif opcoes ==3:
        numero = int(input('Digite o número da tarefa que deseja concluir: '))
        if numero <1 or numero > len(tarefas):
            print('Escolha um número válido.')
        
        else:
            tarefas_escolhidas = tarefas[numero-1]
            if tarefas_escolhidas['concluida']:
                print('Tarefa já concluida.')
            else:
                tarefas_escolhidas['concluida'] = True
                print('A tarefa selecionada: ', tarefas_escolhidas['nome_tarefa'], 'foi concluida.')

           
    elif opcoes ==4:
        ...
    elif opcoes ==5:
        ...
    sair = input('Caso deseje sair escolha 5: ').startswith('5')
    
    if sair is True:
        print('Programa encerrado.')
        break

print(tarefa)