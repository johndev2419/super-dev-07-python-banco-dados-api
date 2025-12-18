from src.banco_dados import conectar2

from sqlalchemy.orm import session
from src.database.models import Livro

    # conexao = conectar2()
    # cursor = conexao.cursor()
    # sql = """INSERT INTO livros (titulo, autor, preco, isbn, descricao)
    # VALUES (%s,%s, %s, %s, %s)"""
    # dados = (titulo,autor,preco,isbn,descricao)
    # cursor.execute(sql, dados,)
    # conexao.commit()
    # cursor.close()
    # conexao.close()
   
def cadastrar(db: session, titulo: str, autor: str, preco: float, isbn: int, descricao: str, quantidade_paginas: int): 
     livro = Livro(
        titulo = titulo,
        autor = autor,
        preco = preco,
        isbn = isbn,
        descricao = descricao,
        quantidade_paginas = quantidade_paginas,
     )
     db.add(livro)
     db.commit()
     db.refresh(livro)
     return livro


def apagar(id_livro: int):
    conexao = conectar2()
    cursor = conexao.cursor()
    sql = "DELETE FROM livros WHERE id = %s"
    dados = (id_livro,)
    cursor.execute(sql,dados)
    conexao.commit()
    linhas_afetadas = cursor.rowcount
    cursor.close()
    conexao.close()
    return linhas_afetadas


def editar(id_livros: int, titulo: str, autor: str, preco: float, isbn: str, descricao: str):
    conexao = conectar2()
    cursor = conexao.cursor()
    sql = """UPDATE livros SET titulo=%s, autor=%s, preco=%s, isbn=%s, descricao=%s WHERE id=%s"""
    dados = (titulo, autor, preco, isbn, descricao, id_livros)
    cursor.execute(sql, dados)
    conexao.commit()
    linhas = cursor.rowcount
    cursor.close()
    conexao.close()
    return linhas



    # conexao = conectar2()
    # cursor = conexao.cursor()
    # cursor.execute("""SELECT id, titulo, autor, preco, isbn, descricao FROM livros""")
    # registros = cursor.fetchall()
    # cursor.close()
    # conexao.close()
    
    # listar_livros = []
    # for r in registros:
    #     listar_livro = {
    #         "id": r[0],
    #         "titulo": r[1],
    #         "autor": r[2],
    #         "preco": r[3],
    #         "isbn": r[4],
    #         "descricao": r[5]
    #     }
    #     listar_livros.append(listar_livro)
    
    # return listar_livros 
def obter_todos(db: session):
    livro = db.query(Livro).all()
    return livro

    

    # conexao = conectar2()
    # cursor = conexao.cursor()
    # sql = """SELECT id, titulo, autor, preco, isbn, descricao FROM livros WHERE ID = %s"""
    # dados = (id, )
    # cursor.execute(sql,dados)

    # registro = cursor.fetchone()
    # if not registro:
    #     return None
    # return{
    #     "id": registro[0],
    #     "titulo" : registro[1],
    #     "autor" : registro[2],
    #     "preco": registro[3],
    #     "isbn": registro[4],
    #     "descricao": registro[5],
    # }
    
def obter_por_id(db: session,id: int):
        livro = db.query(Livro).filter(Livro.id == id).firts()
        return livro

 


    