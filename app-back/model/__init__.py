from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import os

# importando os elementos definidos no modelo
from model.base import Base
from model.wine import Wine
from model.preprocessador import PreProcessador
from model.pipeline import Pipeline
from model.modelo import Model
from model.preprocessador import PreProcessador
from model.avaliador import Avaliador
from model.carregador import Carregador

# 🔁 Configura banco dependendo do ambiente
if os.getenv("FLASK_ENV") == "testing":
    db_url = "sqlite:///:memory:"  # banco em memória para testes
else:
    db_path = "database/"
    if not os.path.exists(db_path):
        os.makedirs(db_path)
    db_url = f'sqlite:///{db_path}/db.sqlite3'


# cria a engine de conexão com o banco
engine = create_engine(db_url, echo=False)

# Instancia um criador de seção com o banco
Session = sessionmaker(bind=engine)

# apenas cria o banco se não for in-memory (evita erro no pytest)
if db_url != "sqlite:///:memory:" and not database_exists(engine.url):
    create_database(engine.url)

# cria as tabelas do banco, caso não existam
Base.metadata.create_all(engine)
