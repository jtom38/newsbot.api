from typing import List
from fastapi import APIRouter
from fastapi_sqlalchemy import db
from sqlalchemy import sql
from newsbotApi.common.messages import *
from newsbotApi.sql.sqlSchema import DiscordQueue as sql
from newsbotApi.sql.dataSchema import DiscordQueue as data

router = APIRouter(
    prefix='/v1/discordqueue',
    tags=['DiscordQueue']
)

@router.get('/get/all')
def getAll() -> List[sql]:
    res = db.session.query(sql).all()
    db.session.close()
    return res

@router.post('/add')
def add(item: data) -> None:
    a = sql().convertFromData(item)
    db.session.add(a)
    db.session.commit()
    db.session.close()

@router.delete('/delete/id')
def deleteById(id: str) -> None:
    res = db.session.query(sql)\
        .filter(sql.id == id)
    db.session.delete(res)
    db.session.commit()
    db.session.close()

