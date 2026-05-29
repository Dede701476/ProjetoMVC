from fastapi import APIRouter, Depends, Request
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth import get_admin
from fastapi.templating import Jinja2Templates
from app.models.usuarios import Usuario

router = APIRouter(prefix="/usuario", tags=["Usuário"])

templates = Jinja2Templates(directory="app/templates")

@router.get("/")
def listar_usuarios(
    request: Request,
    db: Session = Depends(get_db),
    admin = Depends(get_admin) #c=bloqueia quem nao é adm
):
    
    usuarios = db.query(Usuario).order_by(Usuario.nome).all()

    return templates.TemplateResponse(
        request,
        "usuarios/index.html",
        {
            "request": request,
            "usuarios": usuarios,
            "admin": admin 
        }
    )