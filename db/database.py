from sqlalchemy import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_URL = 'mysql+pymysql://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DBNAME}'

class egineconn:
    def __init__(self):
        self.engine = create_engine(DB_URL, pool_recycle = 500)

    def sessionmaker(self):
        Session = sessionmaker(bind=self.engine)
        session = Session()
        return session
    
    def connectio(self):
        conn = self.engine.connect()
        return conn