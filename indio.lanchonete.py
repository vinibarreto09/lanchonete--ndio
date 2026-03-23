# DEF para o cardápio
def mostrar_cardapio(comida, bebida):
    print("\nCOMIDAS:")
    for i, item in enumerate(comida, start=1):
        print(f"{i} - {item}")

    print("\nBEBIDAS:")
    for i, item in enumerate(bebida, start=1):
        print(f"{i + len(comida)} - {item}")

# DEF para fazer os pedidos
def fazer_pedido(comida, bebida, pedido, total):
    escolha = int(input("Digite o número do item: "))

    if escolha == 1:
        pedido.append(comida[0])
        total += 6.0

    elif escolha == 2:
        pedido.append(comida[1])
        total += 7.5

    elif escolha == 3:
        pedido.append(comida[2])
        total += 7.0

    elif escolha == 4:
        pedido.append(bebida[0])
        total += 6.0

    elif escolha == 5:
        pedido.append(bebida[1])
        total += 5.0

    else:
        print("Opção inválida!")
        return total

    print("Ótima escolha!")
    return total

# DEF para salvar os pedidos no arquivo .txt
def salvar_pedido_txt(nome_cliente, pedido, total):
    with open("pedido.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"Cliente: {nome_cliente}\n")
        arquivo.write("Pedido:\n")
        for item in pedido:
            arquivo.write(f"- {item}\n")
        arquivo.write(f"Total: R${total:.2f}\n")
        arquivo.write("-" * 20 + "\n")

# Inicio da interface
print("LANCHONETE DO ÍNDIO")

# Nome do rapaz
nome_cliente = input("Seja bem-vindo a lanchonete do índio, gostariamos de saber o nome de vossa excelência. ")

# Cardápio
comida = ["Dogão - R$6.00", "Sanduíche - R$7.50", "Coxinha - R$7.00"]
bebida = ["Refrigerante - R$6.00", "Água - R$5.00"]

# Pedido e total
pedido = []
total = 0

# Menu
while True:
    print("\n=== MENU ===")
    print("1 - Ver cardápio")
    print("2 - Fazer pedido")
    print("3 - Ver total")
    print("4 - Finalizar e salvar")
    print("0 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("\n~~~~ COMIDAS: ~~~~")
        for i, item in enumerate(comida, start=1):
            print(f"{i} - {item}")

        print("\n~~~~ BEBIDAS: ~~~~")
        for i, item in enumerate(bebida, start=1):
            print(f"{i+len(comida)} - {item}")

    elif opcao == 2:
        escolha = int(input("Digite o número do item: "))

        if escolha == 1:
            pedido.append(comida[0])
            total += 6.0
            print("Ótima escolha!")

        elif escolha == 2:
            pedido.append(comida[1])
            total += 7.5
            print("Ótima escolha!")

        elif escolha == 3:
            pedido.append(comida[2])
            total += 7.0
            print("Ótima escolha!")

        elif escolha == 4:
            pedido.append(bebida[0])
            total += 6.0
            print("Ótima escolha!")

        elif escolha == 5:
            pedido.append(bebida[1])
            total += 5.0
            print("Ótima escolha!")

        else:
            print("Opção inválida!")

    elif opcao == 3:
        print("\nSEU PEDIDO:")
        for item in pedido:
            print("-", item)
        print(f"Total: R${total:.2f}")

    elif opcao == 4:
        salvar_pedido_txt(nome_cliente, pedido, total)
        print("Pedido salvo com sucesso! Volte sempre!")

    elif opcao == 0:
        print("Volte sempre... Obrigado!")
        break

    else:
        print("Opção inválida!")