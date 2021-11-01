from sqlalchemy.orm import Session

from . import models, schemas



def get_news(db: Session, user_id: int):
    return db.query(models.News).filter(models.News.id == user_id).first()


def create_news(db: Session, news: schemas.NewsCreate):

    db_news = models.News(news_id=news.id, tittle=news.tittle, date=news.date,url=news.url,media_outlet=news.media_outlet)
    db.add(db_news)
    db.commit()
    db.refresh(db_news)
    return db_news


def get_has_category(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Category).offset(skip).limit(limit).all()


def create_has_category(db: Session, category: schemas.CategoryCreate, news_id: int):
    db_category= models.Category(**item.dict(), category_id=news_id)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

