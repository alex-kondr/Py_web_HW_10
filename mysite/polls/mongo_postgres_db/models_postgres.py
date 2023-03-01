from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy import Column, String, DateTime, Text, ForeignKey, ARRAY, Integer


engine = create_engine("postgresql://postgres:password@localhost:5432/HW_10")
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Author(Base):
    
    __tablename__ = "polls_author"
    id = Column(Integer(), primary_key=True)    
    fullname = Column(String(250))
    born_date = Column(DateTime())
    born_location =Column(String())
    description = Column(Text())
    

class Quote(Base):
    
    __tablename__ = "polls_quote"
    id = Column(Integer(), primary_key=True)
    tags = Column(ARRAY(item_type=String()))
    author_id = Column(Integer(), ForeignKey("polls_author.id"))
    author = relationship("Author")
    quote = Column(Text())