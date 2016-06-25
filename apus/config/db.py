from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .settings import PACKAGE_DIR, DATABASE_NAME

__all__=('Base', 'session',)

Base = declarative_base()
engine = create_engine('sqlite:///{}/{}'.format(PACKAGE_DIR, DATABASE_NAME))
Session = sessionmaker(bind=engine)
session = Session()
Base.metadata.create_all(engine)