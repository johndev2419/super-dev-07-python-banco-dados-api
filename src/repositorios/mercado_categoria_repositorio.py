from src.banco_dados import conectar
from sqlalchemy.orm import session

from src.database.models import Categoria



def cadastrar(db: session, nome: str):
    categoria = Categoria(nome = nome)
    db.add(categoria)# INSERT INTO categoria (nome) VALUES (%s)
    db.commit()# Concretização do insert no bamc
    db.refresh(categoria)#Atribuir para categoria o id que foi gerado
    return categoria




def editar(db: session, id: int, nome: str):
    # conexao = conectar()


    # cursor = conexao.cursor()

    # sql = "UPDATE categorias Set nome = %s WHERE id = %s"
    # dados = (nome,id)

    # cursor.execute(sql,dados)

    # conexao.commit()

    # linhas_afetadas = cursor.rowcount

    # cursor.close()

    # conexao.close()

    # return linhas_afetadas
   
   # Buscar a categoria pelo id (retorno a prineira eencotrada ou none)
    categoria = db.query(Categoria).filter(Categoria.id == id).first()
   # Senão encontrou a categoria 
    if not categoria:
        return 0 # retornamos 0 indicando que nada foi alterado
    categoria.nome = nome # atualiza o nome do objeto em memoria(sqlalchemy detecta mundança)
    db.commit()# persiste a alteração no banco
    return 1 # retorna 1 indicando sucesso na edição
        


def apagar(db: session,id: int): 
    # conexao = conectar()
    # cursor  = conexao.cursor()
    # sql = "DELETE FROM categorias WHERE id = %s"
    # dados = (id,)
    # cursor.execute(sql,dados)

    # conexao.commit()

    # linhas_afetadas = cursor.rowcount
    # cursor.close()
    # conexao.close()
    # return linhas_afetadas

    categoria = db.query(Categoria).filter(Categoria.id == id).first()

    if not categoria:
        return 0 
    

    db.delete(categoria)
    db.commit()
    return 1 
  


def obter_todos(db: session):
    # conexao = conectar()
    
    # cursor = conexao.cursor()

    # cursor.execute("SELECT id, nome FROM categorias")

    # registros = cursor.fetchall()

    # cursor.close()
    # cursor.close()
    # categorias = []


    # for registro in registros:
    #     categoria = {
    #         "id": registro[0],
    #         "nome": registro[1]
    #     }
    #     categorias.append(categoria)

    # return categorias

  categorias = db.query(Categoria).all()
  return categorias



def obter_por_id(db: session, id: int):
    # conexao = conectar()
    # cursor = conexao.cursor()
    # sql = "SELECT id, nome FROM categorias WHERE id = %s"
    # dados= (id, )
    # cursor.execute(sql,dados)

    # registro = cursor.fetchone()
    # if not registro:
    #     return None
    
    # return {
    #     "id" : registro[0],
    #     "nome" : registro[1]
    # }

  categoria = db.query(Categoria).filter(Categoria.id == id ).first()
  return categoria