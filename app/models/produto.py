# Tabela de produtos

from sqlalchemy import Column, Integer, String, Float, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(String(255), nullable=True)
    preco = Column(Float, nullable=False)
    estoque = Column(Integer, nullable=False, default=0)
    ativo = Column(Boolean, default=True)

    #imagem
    imagem_path = Column(String(255), nullable=True)
    
    #chave estrangeira para categoria
    categoria_id = Column(Integer, ForeignKey("categorias.id", ondelete="SET NULL"), nullable=False)

    #relacionamento
    categoria = relationship("Categoria", back_populates="produtos", lazy="select")

    @property
    def imagem_url(self):
        if self.imagem_path:
            return f"/static/{self.imagem_path}"
        else:
            return "/static/img/produto-placeholder.png"
        
    @property
    def estoque_baixo(self):
        return self.estoque <= 10
        