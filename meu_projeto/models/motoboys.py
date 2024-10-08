from models.enums.genero import Genero
from models.enums.setor import Setor
from models.enderecos import Endereco
from models.abstracts.funcionarios import Funcionario

class Motoboy(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco, cpf: str, rg: str, data_nascimento: str, sexo: Genero, matricula: str, setor: Setor, salario: float, cnh: str) -> None:
        super().__init__(nome, telefone, email, endereco, cpf, rg, data_nascimento, sexo, matricula, setor, salario)
        self.cnh = cnh

    def salario_final(self) -> float:
        resultado = self.salario_final
        return resultado
    
    def __str__(self) -> str:
        return (
            f"{super().__str__()}"
            f"\n\nProfissão: Motoboy"
            f"\nCNH: {self.cnh}")