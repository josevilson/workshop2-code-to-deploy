from fastapi import FastAPI
from typing import List, Dict

app = FastAPI()

@app.get("/")
def ola_mundo():
    return {"mensagem": "Olá mundo!"}

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

@app.get("/produtos")
def listar_produtos():
    return produtos

