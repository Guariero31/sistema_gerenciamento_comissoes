class Usuario:
    def __init__(self, nome, contato):
        self.nome = nome
        self.contato = contato
    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Contato: {self.contato}")

class Cliente(Usuario):
    def __init__(self, nome, contato, endereco):
        super().__init__(nome, contato)
        self.endereco = endereco
    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"Endereço: {self.endereco}")

class Vendedor(Usuario):
    def __init__(self, nome, contato, id):
        super().__init__(nome, contato)
        self.id = id
    def exibir_informacoes(self):
        super().exibir_informacoes()
        print(f"ID: {self.id}")

class Contrato:
    def __init__(self, detalhes):
        self.detalhes = detalhes
    def exibir_informacoes(self):
        print(f"Detalhes do Contrato: {self.detalhes}")

class Venda:
    def __init__(self, cliente, vendedor, contrato, data, valor, status_de_pagamento):
        self.cliente = cliente
        self.vendedor = vendedor
        self.contrato = contrato
        self.data = data
        self.valor = valor
        self.status_de_pagamento = status_de_pagamento
    def calcular_comissao(self):
        if self.vendedor.id > 100:
            return self.valor * 0.07
        else:
            return self.valor * 0.04
    def exibir_informacoes(self):
        self.cliente.exibir_informacoes()
        self.vendedor.exibir_informacoes()
        self.contrato.exibir_informacoes()
        print(f"Data da Venda: {self.data}")
        print(f"Valor da Venda: {self.valor}")
        print(f"Status de Pagamento: {self.status_pagamento}")

def criar_cliente():
    nome = input("Digite o nome do cliente: ")
    contato = input("Digite o contato do cliente: ")
    endereco = input("Digite o endereço do cliente: ")
    return Cliente(nome, contato, endereco)


def criar_vendedor():
    nome = input("Digite o nome do vendedor: ")
    contato = input("Digite o contato do vendedor: ")
    id = int(input("Digite o ID do vendedor: "))
    return Vendedor(nome, contato, id)


def criar_contrato():
    detalhes = input("Digite os detalhes do contrato: ")
    return Contrato(detalhes)


def criar_venda(cliente, vendedor, contrato):
    data = input("Digite a data da venda: ")
    valor = float(input("Digite o valor da venda: "))
    status_pagamento = input("Digite o status de pagamento da venda: ")
    return Venda(cliente, vendedor, contrato, data, valor, status_pagamento)

def exibir_informacoes(obj):
    obj.exibir_informacoes()

def calcular_comissao(venda):
    comissao = venda.calcular_comissao()
    print(f"Comissão do vendedor: R${comissao:.2f}")

while True:
    print("\nMENU:")
    print("1 - Criar Cliente")
    print("2 - Criar Vendedor")
    print("3 - Criar Contrato")
    print("4 - Criar Venda")
    print("5 - Exibir Informações")
    print("6 - Calcular Comissão")
    print("7 - Sair")
    
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        cliente = criar_cliente()
        print("Cliente criado com sucesso!")
    elif opcao == '2':
        vendedor = criar_vendedor()
        print("Vendedor criado com sucesso!")
    elif opcao == '3':
        contrato = criar_contrato()
        print("Contrato criado com sucesso!")
    elif opcao == '4':
        if cliente is not None and vendedor is not None and contrato is not None:
            venda = criar_venda(cliente, vendedor, contrato)
            print("Venda criada com sucesso!")
        else:
            print("Você precisa criar um cliente, um vendedor e um contrato primeiro.")
    elif opcao == '5':
        if cliente is not None:
            exibir_informacoes(cliente)
        else:
            print("Nenhum cliente foi criado.")
    elif opcao == '6':
        if venda is not None:
            calcular_comissao(venda)
        else:
            print("Nenhuma venda foi criada.")
    elif opcao == '7':
        False
    else:
        print("Opção inválida. Tente novamente.")