from typing import List
from fastapi import APIRouter
from fastapi_sqlalchemy import db
from sqlalchemy import sql
from newsbotApi.common.messages import *
from newsbotApi.sql.sqlSchema import DiscordQueue as SqlDiscordQueue
from newsbotApi.sql.dataSchema import DiscordQueue as DataDiscordQueue

router = APIRouter(
    prefix='/v1/discordqueue',
    tags=['DiscordQueue']
)

@router.get('/get/all')
def getAll() -> List[SqlDiscordQueue]:
    res = db.session.query(SqlDiscordQueue).all()
    db.session.close()
    return res

@router.post('/add')
def add(item: DataDiscordQueue) -> None:
    a = SqlDiscordQueue().convertFromData(item)
    db.session.add(a)
    db.session.commit()
    db.session.close()

@router.delete('/delete/url')
def deleteByUrl(url: str) -> None:
    res = db.session.query(SqlDiscordQueue).filter(SqlDiscordQueue.link == url)

