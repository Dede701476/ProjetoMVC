#Script para popular o banco de dados com usuarios admin

from app.database import Session
from app.models.usuarios import Usuario
from app.auth import hash_senha

#função para cadastrar os usuarios

def seed():
    db = Session()
    try:
        nome_usuario = "admin"
        email_usuario = "admin@teste.com"
        senha_usuario = "admin123"
        perfil = "admin"
        # Verificar se o usuário já existe
        usuario_existente = db.query(Usuario).filter_by(email=email_usuario).first()

        if not usuario_existente:
            #criar o usuario
            usuario = Usuario(
                nome_usuario = "admin",
        email_usuario = "admin@teste.com",
        senha_usuario = "admin123",
        perfil = "admin")
            db.add(usuario)
            db.commit()
            print(f"Usuário admin criado com sucesso {nome_usuario}!")
        else:
            print("Usuário admin já existe")

        
    except Exception as erro:
        print(f"Erro ao criar os usuarios: {erro}")
    finally:
        db.close()

seed()