from typing import Annotated
from pydantic import BaseModel, Field, PositiveFloat
from api_academia.contrib.schemas import BaseSchema

class Atleta(BaseSchema):
    nome: Annotated[str, Field(description="Nome do atleta", example="Ian", max_length=50)]
    cpf: Annotated[str, Field(description="CPF do atleta", example="12345678910", max_length=11)]
    idade: Annotated[int, Field(description="Idade do atleta", example=19)]
    peso: Annotated[PositiveFloat, Field(description="Peso do atleta", example=74.2)]
    altura: Annotated[PositiveFloat, Field(description="Altura do atleta", example=1.70)]
    sexo: Annotated[str, Field(description="Sexo do atleta", example="M", max_length=1)]