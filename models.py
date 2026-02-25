# Importando as bibliotecas do SQLalchemist
from sqlalchemy import (
    Column, Integer, String, Float, create_engine
)
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

# Conexão com o banco:
db_url = "mysql+pymysql://root:@localhost:8080/OpenMeteor_db?charset=utf8mb4"

# Criando a engine de dados e verificando se existe um banco com o mesmo nome:
engine = create_engine(db_url, echo=True)
if not database_exists(engine.url):
    create_database(engine.url)
Base = declarative_base()

# Classe clima (Atributos: id, time, temperature_2m, relative_humidity_2m, weather_code)
class Clima(Base):
    __tablename__ = "clima"
    id = Column(Integer, primary_key=True, autoincrement=True) # Coluna id: Tipo inteiro, chave primária e auto incremento
    time = Column(String(16), nullable=False, unique=True) # Coluna time: String de até 16 caracteres, não pode ser nula e deve ser única
    temperature_2m = Column(Integer, nullable=False) # Coluna temperature_2m: Tipo inteiro e não pode ser nula
    relative_humidity_2m = Column(Float(10), nullable=False) # Coluna relative_humidity_2m: Tipo Float(10) e não pode ser nula
    weather_code = Column(Integer,nullable=False) # Coluna weather_code: Tipo inteiro e não pode ser nula

# Criando o banco:
Base.metadata.create_all(engine)