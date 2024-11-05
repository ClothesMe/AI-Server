from sqlalchemy import Column, TEXT, INT, BIGINT, ForeignKey
from sqlalchemy.ext.declarative import declartive_base

Base = declartive_base()

class Test(Base):
    __tablename__ = "test"

    id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
    name = Column(TEXT, nullable=False)
    number = Column(INT, nullable=False)

class Clothes(Base):
    __tablename__ = "clothes"

    id = Column(BIGINT, nullable=False, autoincrement=True, primary_key=True)
    clothes_name = Column(TEXT, nullable=False)
    clothes_type = Column(TEXT, nullable=False)
    clothes_color = Column(TEXT, nullable=False)
    clothes_pattern = Column(TEXT, nullable=False)
    member_id = Column(TEXT, ForeignKey('Member.id'), nullable=False)

class Member(Base):
    __tablename__ = "member"

    id = Column(TEXT, nullable=False, unique=True, index=True)