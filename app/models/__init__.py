from app.models import categoria
from app.models import produto
from app.models import usuarios

#gerar migration
#python -m alembic revision --autogenerate -m "Criar tabelas de categorias e produtos"
# aplicar a migration

#python -m alembic upgrade head