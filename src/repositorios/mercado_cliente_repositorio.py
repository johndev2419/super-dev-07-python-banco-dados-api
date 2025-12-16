from sqlalchemy.orm import session
from datetime import date

from src.database.models import Cliente

def cadastrar(db: session, nome: str, cpf: str, data_nascimento: date, limite: float):
    cliente = Cliente(
        nome = nome,
        cpf=cpf,
        data_nascimento = data_nascimento,
        limite= limite
     )
    
    db.add(cliente)
    db.commit()
    db.refresh(cliente)
    return cliente


def obter_todos(db: session):
    cliente = db.query(Cliente).all()
    return cliente


def obter_por_id(db: session, id: int):
    cliente = db.query(Cliente).filter(Cliente.id == id).first()
    return cliente


def apagar(db: session, id: int):
    cliente = db.query(Cliente).filter(Cliente.id == id).first()
    if not cliente:
        return 0 #gambiarra
    db.delete(cliente)
    db.commit()
    return 1 #gambiarra


def editar(db: session, id: int, data_nascimento: date, limite: float):
    cliente = db.query(Cliente).filter(Cliente.id == id).first()
    if not cliente:
        return 0
    
    cliente.data_nascimento = data_nascimento
    cliente.limite = limite
    db.commit()
    return 1