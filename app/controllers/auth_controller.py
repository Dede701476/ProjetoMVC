#rotas de autenticação
from fastapi import APIRouter, Depends, Request, Form, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from app.database import get_db
from app.models.usuarios import Usuario
from app.auth import hash_senha, verificar_senha

#apirouter agrupa as rotas dentro desse modulo com o prefixo /auth
router = APIRouter(prefix="/auth", tags=["Autenticação"])

templates = Jinja2Templates(directory="app/templates")

#tela de cadastro
@router.get("/cadastro")
def tela_cadastro(request: Request):
    return templates.TemplateResponse(
        request,
        "cadastro.html",
        {"request": request}
        )

#tela de login
@router.get("/login")
def tela_login(request: Request):
    return templates.TemplateResponse(
        request,
        "login.html",
        {"request": request}
        )


#Rota para criar o usuario
@router.post("/cadastro")
def fazer_cadastro(
    request: Request,
    nome: str = Form(...),
    email: str = Form(...),
    senha: str = Form(...),
    db: Session = Depends(get_db)
    
):
    #verificar se o email já existe
    usuario_existente = db.query(Usuario).filter(Usuario.email == email).first()
    if usuario_existente:
        return templates.TemplateResponse(
            request,
            "cadastro.html",
            {
                "request": request, "erro": "Email já está cadastrado"
            }
        )
    
    #criar o usuario
    novo_usuario = Usuario(
        nome=nome,
        email=email,
        senha_hash=hash_senha(senha)
    )
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)

    #redirecionar para a tela de login
    return RedirectResponse("/auth/login", status_code=302)