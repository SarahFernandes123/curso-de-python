print("Gerenciador de Tarefas") #nome do programa para o usuário

print()

tarefas = []

while True: 
    opcoes = int(input('Escolha uma das opções: \n''1)Cadastrar tarefas\n' '2)Listar tarefas\n' '3)Concluir tarefas\n'
                '4)Buscar tarefas\n' '5)Ver estatísticas\n' '0) Sair\n'
               ))  #escolha das opções de funcionamento do gerenciador

    if opcoes == 1:
        nova_tarefa = input('Digite o nome da sua tarefa: ')
        tarefas.append(nova_tarefa)
        
    elif opcoes ==2:
        for i, tarefa in enumerate(tarefas, start=1):
            print(f'{i})',tarefa)   
    elif opcoes ==3:
        ...
    elif opcoes ==4:
        ...
    elif opcoes ==5:
        ...
    ##else: 
        ##break

print(tarefa)