import os
from models.enderecos import Endereco
from models.juridicos import Juridico
from models.motoboys import Motoboy
from models.clientes import Cliente
from models.enums.unidade_federativa import Unidadefederativa
from models.enums.genero import Genero

os.system("cls||clear")

endereco_1 = Endereco("Rua A", "17", "Lado do posto", "1234-567", "Salvador", Unidadefederativa.BAHIA)
juridico_1 = Juridico("Lucas", "1234-5678", "lucas@email", endereco_1, "123456", "123")

endereco_2 = Endereco("Rua B", "29", "Perto da UPA", "8756-432", "Niterói", Unidadefederativa.RIO_DE_JANEIRO)
cliente_1 = Cliente("Gustavo", "9876-5432", "gus@email", endereco_2, "123.456.789.10", "12.345.678.90", "01/01/89", Genero.MASCULINO, 123)

print(juridico_1)
print(cliente_1)