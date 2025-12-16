from datetime import date
from pydantic import BaseModel


class AlunoCalcularMedia(BaseModel):
    nota1: float
    nota2: float
    nota3: float
    nome_completo : str



class AlunoFrequencia(BaseModel):
    nome: str
    quantidade_letivos: int
    quantidade_presencas: int


class ProdutosDesconto(BaseModel):
    nome: str
    preco_original: float
    percentual_desconto: float



class CarroAutonomia(BaseModel):
    modelo: str
    consumo : float
    quantidade_combustivel: float



class PedidoTotal(BaseModel):
    descricao: str
    quantidade: int
    valor_unitario: float


class CategoriaCriar(BaseModel):
    nome: str


class CategoriaEditar(BaseModel):
    nome: str 


class ProdutoCriar(BaseModel):
    nome : str 
    id_categoria: int


class ProdutoEdita(BaseModel):
    nome: str
    id_categoria: int


class LivroCriar(BaseModel):
    titulo : str
    autor : str
    preco: float
    isbn : str 
    descricao: str


class LivroEditar(BaseModel):
    titulo : str
    autor : str
    preco: float
    isbn : str 
    descricao: str


class MangaCriar(BaseModel):
    nome: str
    volume: int 
    autor: str 
    data_lancamento: date


class MangaEditar(BaseModel):
    nome: str
    volume: int 
    autor: str 
    data_lancamento: date


class ClienteCriar(BaseModel):
    nome : str
    cpf: str
    data_nascimento: date
    limite: float


class ClienteEditar(BaseModel):
    data_nascimento: date
    limite: float


    