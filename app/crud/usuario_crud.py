from sqlalchemy.orm import Session
from app.models.usuario_models import Usuario
from app.schemas.usuario_schemas import UsuarioCreate
from app.core.security import hash_senha


def criar_usuario(db: Session, usuario: UsuarioCreate):
    senha_criptografada = hash_senha(usuario.senha)
    novo = Usuario(
        nome=usuario.nome,
        esporte=usuario.esporte,
        cidade=usuario.cidade,
        senha_hash=senha_criptografada
    )
    db.add(novo)
    db.commit()
    db.refresh(novo)
    return novo
