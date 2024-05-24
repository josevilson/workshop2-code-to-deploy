from typing import Dict, List


class Produtos:
    produtos: List[Dict[str, any]] = [
        {
            "id": 1,
            "nome": "Smartphone",
            "descricao": "Descrição do produto 1",
            "preco": 11.00
        },
        {
            "id": 2,
            "nome": "Notebook",
            "descricao": "Descrição do produto 2",
            "preco": 13.00
        },
        {
            "id": 3,
            "nome": "Produto 3",
            "descricao": "Descrição do produto 3",
            "preco": 15.00
        }
    ]

    def listar_produtos(self):
        return self.produtos

    def buscar_produto(self, id: int):
        for produto in self.produtos:
            if produto["id"] == id:
                return produto
        return {"Status": 404, "Mensagem": "Produto não encontrado"}

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        return produto
