from typing import List
from fastapi import APIRouter
from fastapi_sqlalchemy import db
from sqlalchemy import sql
from newsbotApi.common.messages import *
from newsbotApi.sql.sqlSchema import DiscordWebHooks as sql
from newsbotApi.sql.dataSchema import DiscordWebHooks as data

router = APIRouter(
    prefix='/v1/discordwebhooks'
)

@router.get('/get/all')
def getAll() -> List[sql]:
    res = db.session.query(sql).all()
    db.session.close()
    return res

@router.post('/add')
def add(item:data) -> BaseMessage:
    a = sql().convertFromData(item)
    db.session.add(a)
    db.session.commit()
    db.session.close()

@router.get('/get/all/byName')
def getAllByName(name: str) -> sql:
    res = db.session.query(sql).filter(sql.name == name)
    
