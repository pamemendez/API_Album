from pydantic import BaseModel
from typing import Optional


class AlbumLanaDelRey(BaseModel):
    nome: str
    ano_lancamento: int
    capa_url: str
    descricao: Optional[str] = None