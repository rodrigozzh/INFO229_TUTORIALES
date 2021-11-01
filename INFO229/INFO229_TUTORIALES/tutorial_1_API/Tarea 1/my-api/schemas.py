from typing import List, Optional

from pydantic import BaseModel




class NewsBase(BaseModel):
    tittle: str


class NewsCreate(NewsBase):
    pass



class News(NewsBase):
    id:int
    url:str
    date:str
    media_outlet:str
    category: List[Category] = []

    class Config:
        orm_mode = True


class CategoryBase(BaseModel):
    categoria: str



class CategoryCreate(ItemBase):
    pass


class Category(ItemBase):
    id: int
    news_id: int

    class Config:
        orm_mode = True

