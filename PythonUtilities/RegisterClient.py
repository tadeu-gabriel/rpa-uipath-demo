class Cliente:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

class CadastroClientes:
    def __init__(self):
        self.clientes = {}

    def adicionar_cliente(self, cliente):
        if cliente.email not in self.clientes:
            self.clientes[cliente.email] = cliente
            print("Cliente adicionado com sucesso!")
        else:
            print("Erro: O cliente já está cadastrado.")

    def buscar_cliente(self, email):
        if email in self.clientes:
            return self.clientes[email]
        else:
            return None

    def atualizar_cliente(self, email, novo_cliente):
        if email in self.clientes:
            self.clientes[email] = novo_cliente
            print("Cliente atualizado com sucesso!")
        else:
            print("Erro: Cliente não encontrado.")

    def excluir_cliente(self, email):
        if email in self.clientes:
            del self.clientes[email]
            print("Cliente excluído com sucesso!")
        else:
            print("Erro: Cliente não encontrado.")

# Função auxiliar para exibir os detalhes de um cliente
def exibir_cliente(cliente):
    print(f"Nome: {cliente.nome}")
    print(f"Idade: {cliente.idade}")
    print(f"Email: {cliente.email}")
    print()

# Simulação
cadastro = CadastroClientes()

while True:
    print("1. Adicionar cliente")
    print("2. Buscar cliente")
    print("3. Atualizar cliente")
    print("4. Excluir cliente")
    print("5. Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do cliente: ")
        idade = int(input("Idade do cliente: "))
        email = input("Email do cliente: ")
        cliente = Cliente(nome, idade, email)
        cadastro.adicionar_cliente(cliente)

    elif opcao == "2":
        email = input("Digite o email do cliente a ser buscado: ")
        cliente_encontrado = cadastro.buscar_cliente(email)
        if cliente_encontrado:
            exibir_cliente(cliente_encontrado)
        else:
            print("Cliente não encontrado.")

    elif opcao == "3":
        email = input("Digite o email do cliente a ser atualizado: ")
        cliente_encontrado = cadastro.buscar_cliente(email)
        if cliente_encontrado:
            nome = input("Novo nome do cliente: ")
            idade = int(input("Nova idade do cliente: "))
            novo_cliente = Cliente(nome, idade, email)
            cadastro.atualizar_cliente(email, novo_cliente)
        else:
            print("Cliente não encontrado.")

    elif opcao == "4":
        email = input("Digite o email do cliente a ser excluído: ")
        cadastro.excluir_cliente(email)

    elif opcao == "5":
        break

    else:
        print("Opção inválida.")

print("Encerrando o programa.")
