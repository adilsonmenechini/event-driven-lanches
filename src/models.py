# src/models.py

class Lanche:
    def __init__(self, nome, preco, tempo_preparo):
        self.nome = nome
        self.preco = preco
        self.tempo_preparo = tempo_preparo  # Tempo de preparo em minutos

class Bebida:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

class Pedido:
    def __init__(self, id_pedido, numero_mesa):
        self.id_pedido = id_pedido
        self.numero_mesa = numero_mesa
        self.itens = []
        self.pagamento_confirmado = False
        self.status = "solicitado"  # Status inicial do pedido

    def adicionar_item(self, item):
        self.itens.append(item)

    def calcular_total(self):
        return sum(item.preco for item in self.itens)

    def exibir_pedido(self):
        print(f"\nPedido #{self.id_pedido} - Mesa {self.numero_mesa}:")
        for item in self.itens:
            print(f" - {item.nome} : R${item.preco:.2f}")
        total = self.calcular_total()
        print(f"Total: R${total:.2f}")

    def atualizar_status(self, novo_status):
        self.status = novo_status
        print(f"Pedido #{self.id_pedido} status atualizado para: {self.status}")

    def entregar_bebidas_imediatamente(self):
        print(f"Entregando bebidas imediatamente para o Pedido #{self.id_pedido}:")
        for item in self.itens:
            if isinstance(item, Bebida):
                print(f" - {item.nome} : R${item.preco:.2f}")
        self.itens = [item for item in self.itens if not isinstance(item, Bebida)]