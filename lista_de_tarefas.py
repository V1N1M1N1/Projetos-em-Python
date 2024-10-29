def adicionar_tarefa(lista_tarefas, tarefa):
    lista_tarefas.append(tarefa)
    print(f"Tarefa '{tarefa}' adicionada com sucesso!")

def visualizar_tarefas(lista_tarefas):
    if lista_tarefas:
        print("Lista de Tarefas:")
        for i, tarefa in enumerate(lista_tarefas, start=1):
            print(f"{i}. {tarefa}")
    else:
        print("A lista de tarefas está vazia.")

def marcar_concluida(lista_tarefas, numero_tarefa):
    if 1 <= numero_tarefa <= len(lista_tarefas):
        tarefa_concluida = lista_tarefas.pop(numero_tarefa - 1)
        print(f"Tarefa '{tarefa_concluida}' marcada como concluída!")
    else:
        print("Número de tarefa inválido.")

def lista_de_tarefas():
    tarefas = []
    
    while True:
        print("\n=== Lista de Tarefas ===")
        print("1. Adicionar Tarefa")
        print("2. Visualizar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            tarefa = input("Digite a tarefa a ser adicionada: ")
            adicionar_tarefa(tarefas, tarefa)
        elif opcao == '2':
            visualizar_tarefas(tarefas)
        elif opcao == '3':
            visualizar_tarefas(tarefas)
            numero_tarefa = int(input("Digite o número da tarefa a ser marcada como concluída: "))
            marcar_concluida(tarefas, numero_tarefa)
        elif opcao == '4':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

lista_de_tarefas()
