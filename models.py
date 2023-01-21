from sqlalchemy import DATE, INTEGER, NUMERIC, VARCHAR, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class dataset(Base):
    __tablename__ = "dataset"

    id = Column(INTEGER, primary_key=True)
    regiao_sigla = Column(VARCHAR(255))
    estado_sigla = Column(VARCHAR(2))
    municipio = Column(VARCHAR(255))
    revenda = Column(VARCHAR(255))
    cnpj_revenda = Column(VARCHAR(18))
    rua = Column(VARCHAR(255))
    numero = Column(VARCHAR(10))
    complemento = Column(VARCHAR(255))
    bairro = Column(VARCHAR(255))
    cep = Column(VARCHAR(10))
    produto = Column(VARCHAR(50))
    data_coleta = Column(DATE)
    valor_venda = Column(NUMERIC(17, 2))
    valor_compra = Column(NUMERIC(17, 2))
    unidade_de_medida = Column(VARCHAR(25))
    bandeira = Column(VARCHAR(255))
