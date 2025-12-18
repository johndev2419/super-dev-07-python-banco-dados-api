from datetime import date
from sqlalchemy import DOUBLE, Column, Date, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base,  relationship

Base= declarative_base()

#temos uma classe chamada Categoria que herda as propriedades e métodos da base
class Categoria(Base):
    # Nome da tabela no banco de dados
    __tablename__ = "categorias"

    # Coluna da pk id do tipo inteiro auto incrementável
    id = Column(Integer, primary_key=True, autoincrement=True)
    #coluna do nome que nao permite nulo
    nome = Column(String(225), nullable=False)

    produto = relationship("Produto", back_populates="categoria")


class Cliente(Base):
    __tablename__ = "clientes"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(50), nullable= False )
    cpf = Column(String(14), nullable=False)
    data_nascimento = Column(Date, nullable=True)
    limite = Column(DOUBLE, nullable= True)   


class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)

    # FK que relaciona a PK (categorias.id)
    id_categoria = Column(Integer, ForeignKey("categorias.id"))

    categoria = relationship("Categoria", back_populates="produto")


class Livro(Base):
    __tablename__ = "livros" 

    id = Column(Integer, primary_key= True, autoincrement=True)
    titulo = Column(String(100), nullable=False)
    autor = Column(String(100), nullable= False)
    preco = Column(DOUBLE,nullable=False)
    isbn = Column(String(100), nullable=True)
    descricao = Column(String(500), nullable= True)
    quantidade_paginas = Column(Integer, nullable= True)



    

    # nullable=False campo é obrigatório
    # nullable=True campo não é obrigatório