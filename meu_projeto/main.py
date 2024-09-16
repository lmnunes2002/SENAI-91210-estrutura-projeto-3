import os
from models.enderecos import Endereco
from models.juridicos import Juridico
from models.clientes import Cliente
from models.motoboys import Motoboy
from models.enums.unidade_federativa import Unidadefederativa
from models.enums.setor import Setor
from models.enums.genero import Genero

os.system("cls||clear")

endereco_1 = Endereco("Rua A", "17", "Lado do posto", "1234-567", "Salvador", Unidadefederativa.BAHIA)
juridico_1 = Juridico("Lucas", "1234-5678", "lucas@email", endereco_1, "123456", "123")

endereco_2 = Endereco("Rua B", "29", "Perto da UPA", "8756-432", "Niterói", Unidadefederativa.RIO_DE_JANEIRO)
cliente_1 = Cliente("Gustavo", "9876-5432", "gus@email", endereco_2, "123.456.789.10", "12.345.678.90", "01/01/1989", Genero.MASCULINO, 123)

endereco_3 = Endereco("Rua C", "33", "Casa verde", "1122-333", "Botucatu", Unidadefederativa.SAO_PAULO)
motoboy_1 = Motoboy("Gabriel", "4321-8765", "Gabriel@email", endereco_3, "109.876.543-21", "09.876.543.21", "07/09/1998", Genero.MASCULINO, "12345", Setor.OPERACOES, 4000, "CNH")

print(juridico_1)
print(cliente_1)
print(motoboy_1)