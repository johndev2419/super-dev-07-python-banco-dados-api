from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# TODO: ultilizar variavel de ambiente ou arquivo .env
# Não é a forma correta de fazer

DATABASE_URL = "mysql+pymysql://root:adimn@127.0.0.1:3306/mercado"

engine = create_engine(DATABASE_URL, echo=False)

sessionlocal = sessionmaker(bind=engine, autocommit = False, autoflush=False)


def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()

