from enum import Enum

class Genero(Enum):
    MASCULINO = ("M", "Masculino")
    FEMININO = ("F", "Feminino")

    def __init__(self, caractere: str, texto: str) -> None:
        self.caractere = caractere
        self.texto = texto