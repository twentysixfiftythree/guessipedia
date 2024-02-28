from sqlalchemy import create_engine, Column, String, Integer, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy_utils import database_exists, create_database

DATABASE_URI = 'mysql+pymysql://user:iloveboobs@localhost/links_bidirectional'

engine = create_engine(DATABASE_URI, echo=True)

if not database_exists(engine.url):
    create_database(engine.url)

Base = declarative_base()

class WikipediaPage(Base):
    __tablename__ = 'wikipedia_page'
    id = Column(Integer, primary_key=True)
    title = Column(String(255), unique=True, nullable=False)
    surrounding_links = Column(Text, nullable=False)
    link = Column(Text, nullable=False)

Base.metadata.create_all(engine)
