print("Simulador de Compras - Supermercado Mega-X")
print("-" * 42)
print("\r")

# Produtos disponíveis no catálogo
produtos = (
    {"codigo": 1, "descricao": "Arroz", "preco": 3.38},
    {"codigo": 2, "descricao": "Feijão", "preco": 6.98},
    {"codigo": 3, "descricao": "Macarrão", "preco": 6.38},
    {"codigo": 4, "descricao": "Farinha de Trigo", "preco": 2.59},
    {"codigo": 5, "descricao": "Farinha de Mandioca", "preco": 5.79},
    {"codigo": 6, "descricao": "Açucar", "preco": 2.15},
    {"codigo": 7, "descricao": "Sal", "preco": 1.78},
)

# Carrinho de compras vazio
carrinho_de_compras = []


def menu():
    print("Menu")
    print("\r")
    print("1 Adicionar Item ao Carrinho")
    print("2 Exibir Itens no Carrinho")
    print("3 Excluir Itens do Carrinho")
    print("4 Esvaziar Carrinho")
    print("5 Sair")
    print("\r")


def lista():
    for prod in produtos:
        print("Código: {} - Descrição: {} - Preço: {}".format(prod["codigo"], prod["descricao"], prod["preco"]))


def descricao(codigo):
    for prod in produtos:
        if prod["codigo"] == codigo:
            return prod["descricao"]


def adiciona():
    codigo = int(input("Digite o código do produto: "))
    quantidade = int(input("Digite a quantidade desejada: "))
    carrinho_de_compras.append({"codigo": codigo, "quantidade": quantidade})


def remove():
    codigo = int(input("Digite o código do produto a ser excluído: "))
    quantidade = int(input("Digite a quantidade a ser excluída: "))
    carrinho_de_compras.remove({"codigo": codigo, "quantidade": quantidade})


menu()
print("\r")
opcao = "0"

while opcao != "5":
    opcao = input("Digite uma opção do menu: ")

    # Lista os itens disponíveis no catálogo e permite que o usuário escolha os produtos e suas quantidades
    if opcao == "1":
        lista()
        print("\r")
        adiciona()

        decisao = input("Deseja adicionar mais itens? S/N ")

        while decisao:
            if decisao == "S":
                adiciona()
                decisao = input("Deseja adicionar mais itens? S/N ")
            else:
                print("\r")
                print("Obrigada! Para visualizar os itens adicionados ao carrinho selecione a opção 2 no menu.")
                print("\r")
                break

    # Permite que o usuário visualize os itens no carrinho
    if opcao == "2":
        soma = 0
        for item in carrinho_de_compras:
            for produto in produtos:
                if produto["codigo"] == item["codigo"]:
                    soma = soma + (produto["preco"] * item["quantidade"])
                    break

            print("Descrição: {0} - Quantidade: {1}".format(descricao(item["codigo"]), item["quantidade"]))
        print("Valor Total: {0}".format(soma))
        print("\r")

    # Permite que o usuário remova itens do carrinho
    if opcao == "3":
        remove()
        print("\r")

    # Permite que o usuário esvazie o carrinho por completo
    if opcao == "4":
        carrinho_de_compras = []