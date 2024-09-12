from abc import ABC, abstractmethod
from models.enums.genero import Genero
from models.enderecos import Endereco
from models.abstracts.pessoas import Pessoa

class Fisica(Pessoa, ABC):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cpf: str, rg: str, data_nascimento: str, sexo: Genero) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.cpf = cpf
        self.rg = rg
        self.data_nascimento = data_nascimento
        self.sexo = sexo

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"CNPJ: {self.cpf}"
            f"RG: {self.rg}"
            f"Data de nascimento: {self.data_nascimento}"
            f"Sexo: {self.sexo.texto}"
            f"Sigla: {self.sexo.caractere}")
        