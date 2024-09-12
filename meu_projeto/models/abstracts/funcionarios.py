from abc import ABC, abstractmethod
from models.enums.setor import Setor
from models.enums.genero import Genero
from models.enderecos import Endereco
from models.abstracts.fisicas import Fisica

class Funcionario(Fisica, ABC):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cpf: str, rg: str, data_nascimento: str, sexo: Genero, matricula : str, setor: Setor, salario: float) -> None:
        super().__init__(nome, telefone, email, endereco, cpf, rg, data_nascimento, sexo)
        self.matricula = matricula
        self.setor = setor
        self.salario = salario

    @abstractmethod
    def salario_final(self) -> float:
        pass

    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\n\nFuncionário: "
            f"\nMatrícula: {self.matricula}"
            f"\nSetor: {self.setor.value}"
            f"\nSalário: {self.salario}")