from typing import Optional

from pydantic import BaseModel, PositiveInt


class ProdutosSchema(BaseModel):
    id: int
    nome: str
    descricao: Optional[str] = None
    preco: PositiveInt
