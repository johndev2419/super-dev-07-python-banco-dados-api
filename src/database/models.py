from datetime import date
from sqlalchemy import DOUBLE, Column, Date, Integer, String
from sqlalchemy.orm import declarative_base

Base= declarative_base()

#temos uma classe chamada Categoria que herda as propriedades e métodos da base
class Categoria(Base):
    # Nome da tabela no banco de dados
    __tablename__ = "categorias"

    # Coluna da pk id do tipo inteiro auto incrementável
    id = Column(Integer, primary_key=True, autoincrement=True)
    #coluna do nome que nao permite nulo
    nome = Column(String(225), nullable=False)


class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable= False )
    cpf = Column(String(14), nullable=False)
    data_nascimento = Column(Date, nullable=True)
    limite = Column(DOUBLE, nullable= True)