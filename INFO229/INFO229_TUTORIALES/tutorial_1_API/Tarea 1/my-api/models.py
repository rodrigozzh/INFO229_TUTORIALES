from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base 

class News(Base): 

    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    tittle=Column(String(100))
    date=(String(25))
    url=(String(100))
    media_outlet=(String(100))
    
    category = relationship("Category", back_populates="news")

class Category(Base):

    __tablename__ = "Category"

    id = Column(Integer, primary_key=True, index=True)
    categoria = Column(String(50))
    news = relationship("News", back_populates="category")
