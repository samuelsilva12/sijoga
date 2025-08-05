"""Módulo de rotas para gerenciamento de usuários."""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.models.usuario_models import Usuario
from app.schemas.usuario_schemas import UsuarioCreate, UsuarioOut
from app.core.security import hash_senha

router = APIRouter(prefix="/usuarios", tags=["Usuarios"])

@router.post("/", response_model=UsuarioOut)
def criar_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db)):
    usuario_existente = db.query(Usuario).filter(Usuario.nome == usuario.nome).first()
    if usuario_existente:
        raise HTTPException(status_code=400, detail="Usuario já existente!")

    novo_usuario = Usuario(
        nome = usuario.nome,
        esporte = usuario.esporte,
        cidade = usuario.cidade,
        senha_hash = hash_senha(usuario.senha)
    )

    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario