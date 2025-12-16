from datetime import date
from src.banco_dados import conectar3




def obter_todos():
    conexao = conectar3()
    cursor = conexao.cursor()
    cursor.execute(""" SELECT id, nome, volume, autor, data_lancamento FROM mangas""")
    registros = cursor.fetchall()
    cursor.close()
    conexao.close()

    listar_mangas = []

    for r in registros:
        listar_manga = {
            "id": r[0],
            "nome": r[1],
            "volume": r[2],
            "autor": r[3],
            "data_lancamento": r[4],
            
        }
        listar_mangas.append(listar_manga)
    
    return listar_mangas


def Cadastrar(nome: str, volume: int, autor: str, data_lancamento: date):
    conexao = conectar3()
    cursor = conexao.cursor()
    sql = """INSERT INTO mangas (nome, volume, autor, data_lancamento) VALUES ( %s, %s, %s, %s)"""
    dados = (nome, volume, autor, data_lancamento )  
    cursor.execute(sql,dados)
    conexao.commit()
    cursor.close()
    cursor.close()


def editar(id_manga: int, nome: str, volume: int, autor: str, data_lancamento: date ):
    conexao = conectar3()
    cursor = conexao.cursor()
    sql = """UPDATE mangas SET nome=%s, volume=%s, autor=%s, 
     data_lancamento=%s WHERE id=%s"""
    dados = (nome, volume, autor, data_lancamento, id_manga)
    cursor.execute(sql, dados)
    conexao.commit()
    linhas = cursor.rowcount
    cursor.close()
    conexao.close()
    return linhas


def apagar(id: int):
    conexao = conectar3() 
    cursor = conexao.cursor()
    sql = "DELETE FROM mangas WHERE id = %s"
    dados = (id,)
    cursor.execute(sql, dados)
    conexao.commit()
    linhas = cursor.rowcount
    cursor.close()
    conexao.close()
    return linhas


def obter_por_id(id: int): 
    conexao = conectar3()
    cursor = conexao.cursor()
    sql = """SELECT id, nome, volume, autor, data_lancamento FROM mangas WHERE id = %s"""
    dados = (id, )
    cursor.execute(sql,dados)

    registro = cursor.fetchone()
    if not registro:
        return None
    return {
        "id": registro[0],
        "nome": registro[1],
        "volume" : registro[2],
        "autor": registro[3],
        "data_lancamento": registro[4]
    }
