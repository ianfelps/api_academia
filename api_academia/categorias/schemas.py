from typing import Annotated
from pydantic import Field
from api_academia.contrib.schemas import BaseSchema

class Categoria(BaseSchema):
    nome: Annotated[str, Field(description="Nome da categoria", example="Musculacao", max_length=20)]