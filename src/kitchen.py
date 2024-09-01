# src/kitchen.py
import time
from src.models import Pedido, Lanche

class Cozinha:
    def __init__(self):
        self.pedidos_preparados = []

    def preparar_pedido(self, pedido):
        if pedido.status == "pago":
            pedido.atualizar_status("cozinha aceitou")
            print(f"\nCozinha: Pedido #{pedido.id_pedido} recebido. Preparando...")
            tempo_total_preparo = 0
            for item in pedido.itens:
                if isinstance(item, Lanche):
                    tempo_total_preparo += item.tempo_preparo
                    print(f" - {item.nome}: Tempo de preparo {item.tempo_preparo} minutos")
            
            print(f"Tempo total estimado para o Pedido #{pedido.id_pedido}: {tempo_total_preparo} minutos.")
            time.sleep(tempo_total_preparo * 0.1)  # Simulação rápida
            print(f"Pedido #{pedido.id_pedido} da Mesa {pedido.numero_mesa} pronto para entrega.")
            pedido.atualizar_status("pronto para entrega")
            self.pedidos_preparados.append(pedido)
        else:
            print(f"Pedido #{pedido.id_pedido} precisa ser pago antes de ser preparado.")

    def entregar_para_garcom(self, pedido):
        if pedido.status == "pronto para entrega":
            print(f"Cozinha: Pedido #{pedido.id_pedido} está pronto para o garçom levar à Mesa {pedido.numero_mesa}.")
            pedido.atualizar_status("entregue na mesa")
        else:
            print(f"Pedido #{pedido.id_pedido} ainda não está pronto para entrega.")