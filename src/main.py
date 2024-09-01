from .order_manager import GerenciadorDePedidos
from .models import Lanche, Bebida, Pedido

def menu():
    gerenciador = GerenciadorDePedidos()
    while True:
        print("\n--- Lanchonete ---")
        print("1. Fazer Pedido")
        print("2. Processar Pedido")
        print("3. Status")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            numero_mesa = input("Número da mesa: ")
            pedido = Pedido(gerenciador.contador_pedidos, numero_mesa)
            gerenciador.contador_pedidos += 1
            while True:
                print("\nAdicionar item ao pedido:")
                print("1. Hambúrguer Smash (3 min)")
                print("2. Hambúrguer Artesanal (6 min)")
                print("3. Bebida - agua")
                print("4. Bebida - refrigerante")
                print("5. Finalizar Pedido")
                opcao_item = input("Escolha uma opção: ")

                if opcao_item == "1":
                    lanche = Lanche("Hambúrguer Smash", 15.00, 3)
                    pedido.adicionar_item(lanche)
                elif opcao_item == "2":
                    lanche = Lanche("Hambúrguer Artesanal", 20.00, 6)
                    pedido.adicionar_item(lanche)
                elif opcao_item == "3":
                    bebida = Bebida("Agua", 5.00)
                    pedido.adicionar_item(bebida)
                elif opcao_item == "4":
                    bebida = Bebida("Refrigerante", 7.00)
                    pedido.adicionar_item(bebida)
                elif opcao_item == "5":
                    gerenciador.adicionar_pedido(pedido)
                    break
                else:
                    print("Opção inválida.")

        elif opcao == "2":
            print("\n--- Processar Pedido ---")
            print("1. Confirmar Pagamento")
            print("2. Cozinha Aceitar Pedido")
            print("3. Garçom Levar à Mesa")
            processar_opcao = input("Escolha uma opção: ")
            
            if processar_opcao == "1":
                gerenciador.processar_pagamento_pedido()
            elif processar_opcao == "2":
                gerenciador.processar_cozinha_pedido()
            elif processar_opcao == "3":
                gerenciador.processar_garcom_pedido()
            else:
                print("Opção inválida.")

        elif opcao == "3":
            gerenciador.exibir_status_pedidos()

        elif opcao == "4":
            print("Encerrando sistema...")
            break

        else:
            print("Opção inválida.")
