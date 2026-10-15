
tarefas = []


def cadastrar_tarefa():
    print("\n--- CADASTRAR TAREFA ---")

    while True:
        titulo = input("Título: ").strip()

        if titulo != "":
            break

        print("Erro: o título não pode ficar vazio.")

    descricao = input("Descrição: ").strip()

    while True:
        prioridade = input(
            "Prioridade (Alta, Média ou Baixa): "
        ).strip().lower()

        if prioridade == "alta":
            prioridade = "Alta"
            break
        elif prioridade in ("média", "media"):
            prioridade = "Média"
            break
        elif prioridade == "baixa":
            prioridade = "Baixa"
            break
        else:
            print("Erro: prioridade inválida.")

    data_limite = input("Data limite: ").strip()

    tarefa = {
        "titulo": titulo,
        "descricao": descricao,
        "prioridade": prioridade,
        "data_limite": data_limite,
        "status": "Pendente"
    }

    tarefas.append(tarefa)

    print("\nTarefa cadastrada com sucesso!")


def visualizar_tarefas():
    print("\n--- TAREFAS CADASTRADAS ---")

    if len(tarefas) == 0:
        print("Não existem tarefas cadastradas.")
        return

    for numero, tarefa in enumerate(tarefas, start=1):
        print(f"\nTarefa {numero}")
        print(f"Título: {tarefa['titulo']}")
        print(f"Descrição: {tarefa['descricao']}")
        print(f"Prioridade: {tarefa['prioridade']}")
        print(f"Data limite: {tarefa['data_limite']}")
        print(f"Status: {tarefa['status']}")


def main():
    while True:
        print("\n===== TASKTRACKER =====")
        print("1. Cadastrar nova tarefa")
        print("2. Visualizar tarefas cadastradas")
        print("3. Sair da aplicação")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_tarefa()
        elif opcao == "2":
            visualizar_tarefas()
        elif opcao == "3":
            print("Encerrando o TaskTracker...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
