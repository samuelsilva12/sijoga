from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from dotenv import load_dotenv
import os


#carrega as variaveis do arquivo .env
load_dotenv()

# lÊ a url de conexão com o postgres
DATABASE_URL = os.getenv('DATABASE_URL')

# Adiciona parâmetros de codificação UTF-8 se não estiverem presentes
if DATABASE_URL and '?' not in DATABASE_URL:
    DATABASE_URL += "?client_encoding=utf8"

#cria o mecanismo de conexão com o bd
engine = create_engine(
    DATABASE_URL,
    echo=True,
    connect_args={"options": "-c client_encoding=utf8"}
)

SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()