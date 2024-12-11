from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from sqlalchemy import Column, TEXT, INT, BIGINT, ForeignKey, String
# from sqlalchemy.ext.declarative import declartive_base
from config.db_config import DB_URL;

# 데이터베이스 연결 설정
# engine = create_engine(DB_URL) 
# 테이블 삭제

engine = create_engine("sqlite:///clothesme.db")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 테이블 모델 정의
Base = declarative_base()

class Clothes(Base):
    __tablename__ = "clothes"

    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    clothes_name = Column(TEXT, nullable=False)
    clothes_type = Column(TEXT, nullable=False)
    clothes_color = Column(TEXT, nullable=False)
    clothes_pattern = Column(TEXT, nullable=False)
    member_id = Column(Integer, ForeignKey('member.id'), nullable=False)

class Member(Base):
    __tablename__ = "member"

    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    uuid = Column(String(100), nullable=False, unique=True)

# 테이블 생성
Base.metadata.create_all(engine)

# CREATE
def create_member(db: Session, uuid: String):
    new_member = Member(uuid=str(uuid))
    db.add(new_member)
    db.commit()
    db.refresh(new_member)
    print(f"Member created: {new_member}")

# CREATE
def create_clothes(db: Session, clothes_name: String, clothes_type: String, clothes_color: String, clothes_pattern: String, member_id: Integer):
    new_clothes = Clothes(clothes_name=clothes_name, clothes_type=clothes_type, clothes_color=clothes_color, clothes_pattern=clothes_pattern, member_id=member_id)
    db.add(new_clothes)
    db.commit()
    db.refresh(new_clothes)
    print(f"Clothes created: {new_clothes}")

# class egineconn:
#     def __init__(self):
#         self.engine = create_engine(DB_URL, pool_recycle = 500)

#     def sessionmaker(self):
#         Session = sessionmaker(bind=self.engine)
#         session = Session()
#         return session
    
#     def connectio(self):
#         conn = self.engine.connect()
#         return conn