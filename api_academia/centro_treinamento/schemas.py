from typing import Annotated
from pydantic import Field
from api_academia.contrib.schemas import BaseSchema

class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(description="Nome do centro de treinamento", example="Area 51", max_length=20)]
    endereco: Annotated[str, Field(description="Endereço do centro de treinamento", example="Rua X, Quadra Y", max_length=60)]
    proprietario: Annotated[str, Field(description="Proprietario do centro de treinamento", example="Ian", max_length=30)]