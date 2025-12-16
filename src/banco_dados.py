from mysql.connector import connect

def conectar():
    conexao = connect(
       host = "127.0.0.1",
       port = "3306",
       user = "root",
       password= "adimn",
       database="mercado",
   )
    return conexao


def conectar2():
    conexao = connect(
       host = "127.0.0.1",
       port = "3306",
       user = "root",
       password= "adimn",
       database="biblioteca",
   )
    return conexao


def conectar3():
    conexao = connect(
       host = "127.0.0.1",
       port = "3306",
       user = "root",
       password= "adimn",
       database="mangas",
   )
    return conexao