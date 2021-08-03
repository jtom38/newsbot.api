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
app.version = '0.8.0'
app.add_middleware(DBSessionMiddleware, db_url="sqlite:///newsbot.api.db")
app.include_router(v1ArticlesRouter)
app.include_router(v1DiscordQueueRouter)
app.include_router(v1DiscordWebHooksRouter)
app.include_router(v1IconsRouter)
app.include_router(v1SettingsRouter)
app.include_router(v1SourceLinksRouter)
app.include_router(v1SourcesRouter)

system("alembic upgrade head")

@app.get("/")
def read_root():
    return {"Hello": "World"}


