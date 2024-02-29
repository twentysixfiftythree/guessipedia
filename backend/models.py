from sqlalchemy import create_engine, Column, Integer, String, Text
from sqlalchemy.dialects.mysql import LONGTEXT
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database, drop_database
import json


with open('config.json', 'r') as f:
    config = json.load(f)

DATABASE_URI = config['DATABASE_URI']
engine = create_engine(DATABASE_URI, echo=False)

if database_exists(engine.url):
    drop_database(engine.url)
create_database(engine.url)
    

Base = declarative_base()

class WikipediaPage(Base):
    __tablename__ = 'wikipedia_page'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), unique=True, nullable=False)
    surrounding_links = Column(LONGTEXT, nullable=False)
    link = Column(Text, nullable=False)
    categories = Column(Text, nullable = False)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(engine)
