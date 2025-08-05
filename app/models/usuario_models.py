from sqlalchemy import Column,String,Integer
from app.core.config import Base
class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    esporte = Column(String, nullable=False)
    cidade = Column(String, nullable=False)
    senha_hash = Column(String, nullable=False)