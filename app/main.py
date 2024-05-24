from fastapi import FastAPI

from .data import Produtos
from .schema import ProdutosSchema

app = FastAPI()
lista_de_produtos = Produtos()


@app.get("/")
def ola_mundo():
    return {"mensagem": "Olá mundo!"}


@app.get("/produtos", response_model=list[ProdutosSchema])
def listar_produtos():
    return lista_de_produtos.listar_produtos()


@app.get("/produtos/{id}", response_model=ProdutosSchema)
def pegar_produto(id: int):
    for produto in lista_de_produtos.listar_produtos():
        if produto["id"] == id:
            return produto
    return {"Status": 404, "Mensagem": "Produto não encontrado"}


@app.post("/produtos", response_model=ProdutosSchema)
def adicionar_produto(produto: ProdutosSchema):
    return lista_de_produtos.adicionar_produto(produto.model_dump())