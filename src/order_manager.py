# src/order_manager.py
from collections import deque
from src.payment import Pagamento
from src.kitchen import Cozinha

class GerenciadorDePedidos:
    def __init__(self):
        self.fila_pedidos = deque()
        self.contador_pedidos = 1
        self.cozinha = Cozinha()

    def adicionar_pedido(self, pedido):
        self.fila_pedidos.append(pedido)
        print(f"Pedido #{pedido.id_pedido} para a Mesa {pedido.numero_mesa} adicionado à fila.")

    def selecionar_pedido(self):
        if not self.fila_pedidos:
            print("Nenhum pedido na fila.")
            return None
        
        self.listar_pedidos()
        pedido_id = int(input("Informe o ID do pedido que deseja processar: "))
        for pedido in self.fila_pedidos:
            if pedido.id_pedido == pedido_id:
                return pedido
        print(f"Pedido #{pedido_id} não encontrado.")
        return None

    def listar_pedidos(self):
        print("\n--- Lista de Pedidos ---")
        for pedido in self.fila_pedidos:
            print(f"Pedido #{pedido.id_pedido} - Mesa {pedido.numero_mesa} - Status: {pedido.status}")

    def exibir_status_pedidos(self):
        print("\n--- Status dos Pedidos ---")
        for pedido in self.fila_pedidos:
            print(f"Pedido #{pedido.id_pedido} - Mesa {pedido.numero_mesa} - Status: {pedido.status}")

    def processar_pagamento_pedido(self):
        pedido = self.selecionar_pedido()
        if pedido:
            if not pedido.pagamento_confirmado:
                total = pedido.calcular_total()
                pagamento = Pagamento()
                pedido.pagamento_confirmado = pagamento.confirmar_pagamento(total)
                if pedido.pagamento_confirmado:
                    pedido.atualizar_status("pago")
                    print(f"Pagamento do Pedido #{pedido.id_pedido} confirmado.")
                    pedido.entregar_bebidas_imediatamente()
                else:
                    print(f"Falha no pagamento do Pedido #{pedido.id_pedido}.")
            else:
                print(f"Pagamento do Pedido #{pedido.id_pedido} já foi confirmado.")

    def processar_cozinha_pedido(self):
        pedido = self.selecionar_pedido()
        if pedido and pedido.pagamento_confirmado:
            print("\n1. Cozinha Aceitar Pedido")
            print("2. Pedido Pronto")
            etapa = input("Escolha a etapa do processamento: ")

            if etapa == "1" and pedido.status == "pago":
                self.cozinha.preparar_pedido(pedido)
            elif etapa == "2" and pedido.status == "cozinha aceitou":
                self.cozinha.entregar_para_garcom(pedido)
            else:
                print("Etapa inválida ou pedido não está no estado correto.")
        else:
            print("Selecione um pedido válido e confirme o pagamento primeiro.")

    def processar_garcom_pedido(self):
        pedido = self.selecionar_pedido()
        if pedido and pedido.status == "pronto para entrega":
            self.cozinha.entregar_para_garcom(pedido)