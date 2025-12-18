
from fastapi import Depends, FastAPI, HTTPException

from src.database.conexao import get_db, get_db_livro

from sqlalchemy.orm import session

from src.classes import (
    AlunoCalcularMedia, 
    AlunoFrequencia, 
    CarroAutonomia, 
    CategoriaCriar,
    CategoriaEditar,
    ClienteCriar,
    ClienteEditar,
    LivroCriar,
    LivroEditar,
    MangaCriar, 
    PedidoTotal,
    ProdutoCriar,
    ProdutoEdita, 
    ProdutosDesconto,
)
from src.repositorios import biblioteca_livro_repositorios, mangas_repositorios, mercado_categoria_repositorio, mercado_cliente_repositorio, mercado_produto_repositorio

app = FastAPI()
# pip intall pymysql
#pip freeze > requirement.txt
@app.get("/greetings")
def saudacoes():
    return {"mensagem": "hello world"}


#query param 
#/calculadora?numero1=10&numero2=10
@app.get("/calculadora")
def calculadora(numero1:int, numero2: int):
    soma = numero1 + numero2
    return{"resultado": soma}


#query vai depois da ? ex: /calculadora/expert?operacao=soma&n1=100&n2=200

@app.get("/calculadora/expert")
def calculadora_expert(operacao: str, n1: int, n2: int):
    if operacao not in ["somar", "subtrair"]:
        raise HTTPException(
            status_code=400,
            detail="Operação invalída. Opções disponiveis [somar/subtrair]"
        )




    if operacao == "somar":
        resultado = n1 + n2
        return {
            "n1": n1,
            "n2": n2,
            "operacao": operacao,
            "resultado": resultado
        }
    elif operacao == "subtrair":
        resultado = n1 - n2
        return {
            "n1": n1,
            "n2": n2,
            "operacao": operacao,
            "resultado": resultado
        }


# Criar um endpoint 'pessoa/nome-completo' para concatenar o nome da pessoa
#   Receber dois query params: nome e sobrenome
#   Retornar no seguinte formato {"nomeCompleto": "John Doe"}
# Criar um endpoint 'pessoa/calcular-ano-nascimento' para calcular o ano de nascimento
#   Query param: idade
#   Calcular o ano de nascimento
#   Retornar {"anoNascimento": 1991}
# Criar um endpoint 'pessoa/imc' para calcular o imc da pessoa
#   Query param: altura, peso
#   Calcular o imc
#   Retornar {"imc": 20.29}
# Alterar o endpoint 'pessoa/imc' para retornar o status do imc
#   Descobrir o status do IMC
#   Retornar {"imc"': 20.29, "Obesidade III"}




# fastapi dev main.py

# 127.0.0.1:8000/docs
# 127.0.0.1:8000/greetings



@app.get("/pessoa/nome-completo")
def nome_comppleto(nome: str, sobrenome: str):
    nome_comppleto = nome + sobrenome
    return {
        "nome": nome,
        "sobrenome": sobrenome,
        "nome completo": nome_comppleto
        }


@app.get("/pessoa/calcular-ano-nascimento")
def calcular_ano_nascimento (idade: int):
    ano_atual = 2025
    ano_de_nascimento = ano_atual - idade
    return{
        "idade" : idade,
        "ano de nascimento": ano_de_nascimento
    }   



@app.get("/pessoa/imc")
def calcular_imc(altura: float, peso: float):
    imc = peso / (altura * altura)

    return {
        "imc": round(imc, 2)
    }


def status_imc(imc: float) -> str:
    if imc < 18.5:
        return "Magreza"
    if imc < 25:
        return "Normal"
    if imc < 30:
        return "Sobrepeso"
    if imc < 35:
        return "Obesidade I"
    if imc < 40:
        return "Obesidade II"
    return "Obesidade III"

@app.get("/pessoa/imc")
def calcular_imc(altura: float, peso: float):
    imc = peso / (altura * altura)
    status = status_imc(imc)

    return {
        "imc": round(imc, 2),
        "status": status
    }



@app.post("/aluno/calcular-media")
def calcular_media(aluno_dados: AlunoCalcularMedia):
    nota1 = aluno_dados.nota1
    nota2 = aluno_dados.nota2
    nota3 = aluno_dados.nota3
    media =(nota1 + nota2 + nota3) / 3
    return{
        "media" : media,
        "nome_completo" : aluno_dados.nome_completo
    }



@app.post("/aluno/calcular-frequencia")
def calcular_frequencia(aluno_dados:  AlunoFrequencia):
    qtd_letivos = aluno_dados.quantidade_letivos
    qtd_presencas = aluno_dados.quantidade_presencas

    frequencia = (qtd_presencas * qtd_letivos) / qtd_letivos

    return{
        "nome: ": aluno_dados.nome,
        "frequencia: ": frequencia
    }


@app.post("/produto/calcular-desconto")
def calcular_descontos(produto: ProdutosDesconto):

    preco_original = produto.preco_original
    percentual = produto.percentual_desconto

    valor_desconto = (preco_original * percentual) /100
    preco_final = preco_original - valor_desconto

    return{
        "nome: ": produto.nome,
        "preco-original: ": preco_original,
        "percentual_desconto": percentual,
        "preco_final: " : preco_final
    }


@app.post("/carro/calcular-autonomia")
def calcular_autonomia(carro: CarroAutonomia):
    consumo = carro.consumo
    combustivel = carro.quantidade_combustivel

    autonomia = consumo *  combustivel

    return{
        "modelo: ": carro.modelo,
        "autonomia": autonomia
    }




@app.post("/pedido/calcular-total")
def calcular_total(pedido: PedidoTotal):

    quantidade = pedido.quantidade
    valor_unitario = pedido.valor_unitario

    subtotal = quantidade * valor_unitario
    taxa = subtotal * 0.05  
    total = subtotal + taxa

    return {
        "descricao": pedido.descricao,
        "subtotal": subtotal,
        "taxa": taxa,
        "total": total
    }



@app.get("/api/v1/categorias", tags=["Categorias"])
def listar_categorias(db: session = Depends(get_db)):
    categorias = mercado_categoria_repositorio.obter_todos(db)
    return categorias

#/api/v1/categorias
#metodo post
#body: {"nome" : "batatinha"}
@app.post("/api/v1/categorias", tags=["Categorias"])
def cadastrar_categorias(categoria: CategoriaCriar, db: session = Depends(get_db)):
    mercado_categoria_repositorio.cadastrar(db, categoria.nome)
    return{
        "status:" : "ok"
    }


#
#/api/v1/categorias/10
# metodo DELETE
@app.delete("/api/v1/categorias/{id}", tags=["Categorias"])
def apagar_categorias(id: int, db: session = Depends(get_db)):
    linhas_afetadas = mercado_categoria_repositorio.apagar(db,id)

    if linhas_afetadas == 1:
        return{
            "status": "Ok"
        }
    else:
        raise HTTPException(status_code=404, detail = "Categoria não listada")
    


# /api/v1/categorias/10
# metodo PUT
# Body {"nome": "batatona 2.0"}
@app.put("/api/v1/categorias/{id}",tags=["Categorias"])
def alterar_categoria(id:int, categoria: CategoriaEditar, db: session = Depends(get_db)):
    linhas_afetadas = mercado_categoria_repositorio.editar(db, id, categoria.nome,)
    if linhas_afetadas == 1:
        return{
            "status" : "ok"
        }
    else:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    


@app.get("/api/v1/categorias/{id}", tags=["Categorias"])
def buscar_categoria_por_id(id: int, db: session= Depends(get_db)):
    categoria = mercado_categoria_repositorio.obter_por_id(db, id)
    if categoria is None:
        raise HTTPException(status_code=404, detail="não encontrado")
    return categoria



@app.get("/api/v1/produtos", tags=["Produtos"])
def listar_todos_produtos(db: session = Depends (get_db)):
 produtos = mercado_produto_repositorio.obter_todos(db)
 return produtos
    


# Cadastrar
@app.post("/api/v1/produtos", tags=["Produtos"])
def cadastrar_podutos(produto: ProdutoCriar, db : session = Depends(get_db)):
    mercado_produto_repositorio.cadastrar(db,produto.nome, produto.id_categoria)
    return{"status": "ok"}

#editar
@app.put("/api/v1/produtos/{id}", tags=["Produtos"] )
def editar_produtos(produto: ProdutoEdita, id: int, db: session = Depends(get_db)):
    linhas_afetadas = mercado_produto_repositorio.editar(db, id, produto.nome, produto.id_categoria)
    if linhas_afetadas !=1 : 
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return{
        "status" : "ok"
    }


@app.get("/api/v1/produtos/{id}", tags=["Produtos"] )
def obter_produto_por_id(id:int, db: session = Depends(get_db)):
    produto = mercado_produto_repositorio.obter_por_id(db, id)
    if produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto



# Apagar
@app.delete("/api/v1/produtos/{id}",  tags=["Produtos"] )
def apagar_produto(id: int, db: session = Depends(get_db)):
    linhas_afetadas = mercado_produto_repositorio.apagar(db, id)
    if linhas_afetadas != 1:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return{"status" : "ok"}



# Criar a API para livro, manga e revista
#

@app.get("/api/v1/livros", tags=["Livros"])
def listar_livros(db: session = Depends(get_db_livro)):
    livro = biblioteca_livro_repositorios.obter_todos(db)
    return livro


@app.get("/api/v1/livros/{id}",  tags=["Livros"])
def obter_livros_id(id: int, db:session = Depends(get_db_livro)):
    livro = biblioteca_livro_repositorios.obter_por_id(db,id)
    if livro is None :
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return livro


@app.post("/api/v1/livros", tags=["Livros"] )
def cadastrar_livros(livro : LivroCriar, db: session = Depends(get_db_livro)):
    biblioteca_livro_repositorios.cadastrar(db, livro.titulo, livro.autor, livro.preco, livro.isbn, livro.descricao, livro.quantidade_paginas)
    return{
        "status" : "ok"
    }


@app.put("/api/v1/livros/{id}",  tags=["Livros"] )
def editar_livro(livro: LivroEditar, id: int):
    linhas_afetadas = biblioteca_livro_repositorios.editar(id, livro.titulo,livro.autor,livro.preco,livro.isbn,livro.descricao)
    if linhas_afetadas == 1:
        return{
            "status" : "ok"
        }
    else:
        raise HTTPException(status_code=404, detail="Categoria não encontrada")
    

@app.delete("/api/v1/livros/{id}",  tags=["Livros"])
def apagar_livro(id: int):
    linhas_afetadas = biblioteca_livro_repositorios.apagar(id)
    if linhas_afetadas != 1 :
        raise HTTPException(status_code=404, detail="Livro não encontrado")
    return {
        "status" : "ok"
    }
    

@app.get("/api/v1/mangas", tags=["Mangas"])
def listar_mangas():
    manga = mangas_repositorios.obter_todos()
    return manga 

@app.post("/api/v1/mangas", tags=["Mangas"])
def cadastrar_manga(manga: MangaCriar):
    mangas_repositorios.Cadastrar(manga.nome, manga.volume, manga.autor,manga.data_lancamento)
    return {
        "status" : "ok"
    }









# passos para criar um novo endpoint 
# criar a tabela sql > create table
# adicionae a classe no src/repositorio/mercado_<nome>_repositorio 
#
#

@app.post("/api/v1/clientes", tags=["clientes"])
def cradastrar_clientes(cliente: ClienteCriar,db: session = Depends(get_db)):
    cliente = mercado_cliente_repositorio.cadastrar(
        db,
        cliente.nome,
        cliente.cpf,
        cliente.data_nascimento,
        cliente.limite, 
    )
    return cliente


@app.get("/api/v1/clientes", tags=["clientes"])
def listar_cliente(db: session = Depends(get_db)):
    clientes = mercado_cliente_repositorio.obter_todos(db)
    return clientes



@app.delete("/api/v1/clientes/{id}", tags=["clientes"])
def apagar_cliente(id: int, db: session = Depends(get_db)):
    linha_afetadas = mercado_cliente_repositorio.apagar(db, id)
    if not linha_afetadas:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return {"status" : "ok"}


@app.put("/api/v1/clientes/{id}", tags=["clientes"])
def editar_cliente(id: int, cliente: ClienteEditar, db: session = Depends(get_db) ):
    linhas_afetadas = mercado_cliente_repositorio.editar(
        db, id, cliente.data_nascimento, cliente.limite
    )
    if not linhas_afetadas:
     raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return {"status":"ok"}


@app.get("/api/v1/clientes/{id}", tags=["clientes"])
def listar_cliente_id(id: int, db:session = Depends(get_db)):
    cliente = mercado_cliente_repositorio.obter_por_id(db, id)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente não encontrado")
    return cliente
        

