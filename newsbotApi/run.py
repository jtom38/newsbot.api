from os import system
from typing import Optional
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware
from fastapi_sqlalchemy import db
from newsbotApi.v1 import *
import newsbotApi.sql.sqlSchema as sqlSchema
import newsbotApi.sql.dataSchema as dataSchema


app = FastAPI()
app.title = "Newsbot"
app.add_middleware(DBSessionMiddleware, db_url="sqlite:///newsbot.api.db")
app.include_router(v1ArticlesRouter)
app.include_router(v1DiscordQueueRouter)
app.include_router(v1DiscordWebHooksRouter)

system("alembic upgrade head")

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/test/post")
def postTest() -> None:
    a = sqlSchema.Articles(siteName='test')
    db.session.add(a)
    db.session.commit()
    items = db.session.query(sqlSchema.Articles).all()
    db.session.close()
    return items



