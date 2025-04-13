from sqlalchemy import Column, VARCHAR, CHAR, Integer

from model import Base


class User(Base):
    name = Column(VARCHAR(120), nullable=False)
    cpf = Column(CHAR(11), nullable=False)
    email = Column(VARCHAR(260), nullable=False)
    phone_number = Column(Integer, nullable=False)
