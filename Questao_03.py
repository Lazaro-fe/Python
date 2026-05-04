import os
os.system("cls || clear")

lista_de_produtos = []
lista_de_precos = []

while True:
    print(""""
          === SUPERMERCADO ASSUNÇÃO ===

          1 - CADASTRAR PRODUTO
          2 - MOSTRAR A LISTA DE COMPRAS (PRÉVIA)
          3 - MOSTRAR TOTAL DE COMPRAS
          4 - SAIR DO PROGRAMA
          """)
    
    try:
        opcao_super = float(input("Digite a opção desejada: "))
    except ValueError:
        print("Erro ao identificar o que deseja!\nDigite um número válido!")
        continue

    match opcao_super:

        case 1:
            while True:
                nome = input("Digite o nome do produto: ")

                try:
                    preco = float(input("Digite o preço do produto: R$ "))
                except ValueError:
                    print("Preço inválido!")
                    continue

                if preco == 0:
                    print("Entrada de Produtos encerrada...")
                    break

                lista_de_produtos.append(nome)
                lista_de_precos.append(preco)
                print(f"--> {nome} adicionado com sucesso")
        
        case 2:

            print("\n== Lista de Compras (Prévia) ==")
            if not lista_de_produtos:
                print("O carrinho está vazio!!")
            else:
                for i in range(len(lista_de_produtos)):
                    print(f"{lista_de_produtos[i]} -- R$ {lista_de_precos[i]:.2f}")
                print(f"Subtotal de Lista: R$ {sum(lista_de_precos)}")
            print("-" * 33)

        case 3:

            print("\n--- Finalizar Compra ---")
            if not lista_de_precos:
                print("Você ainda não comprou nenhum produto. Cadastre produtos antes de finalizar.")
                continue
            
            try:
                distancia = float(input("Digite a distância de entrega em km: "))
            except ValueError:
                print("Distância inválida! Tente novamente.")
                continue
            
            if distancia <= 50:
                frete = distancia * 2.00
            else:
                frete = distancia * 1.80
                
            total_produtos = sum(lista_de_precos)
            total_final = total_produtos + frete
            
            print("=== RECIBO FINAL ===")
            for i in range(len(lista_de_produtos)):
                print(f"- {lista_de_produtos[i]}: R$ {lista_de_precos[i]:.2f}")
            print("-" * 20)
            print(f"Subtotal dos produtos: R$ {total_produtos:.2f}")
            print(f"Valor do Frete ({distancia} km): R$ {frete:.2f}")
            print(f"TOTAL A PAGAR: R$ {total_final:.2f}")
            print("====================")
            print("Obrigado por comprar no Supermercado Assunção!\n")
            break

        case 4:
            print("\nSaindo do sistema... Até logo!")
            break

        case _:
            print("\nOpção inválida! Por favor, escolha uma opção entre 1 e 4.")