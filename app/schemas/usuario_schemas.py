from pydantic import BaseModel

class UsuarioBase(BaseModel):
    """Classe base para usuários."""
    nome: str
    esporte: str
    cidade: str

class UsuarioCreate(UsuarioBase):
    """Schema para criação de usuários."""
    senha: str


class UsuarioOut(UsuarioBase):
    """Schema para resposta de usuários."""
    id: int
    class Config:
      orm_mode =True