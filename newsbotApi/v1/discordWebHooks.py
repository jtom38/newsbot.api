from typing import List
from fastapi import APIRouter
from fastapi_sqlalchemy import db
from sqlalchemy import sql
from newsbotApi.common.messages import *
from newsbotApi.sql.sqlSchema import DiscordWebHooks as sql
from newsbotApi.sql.dataSchema import DiscordWebHooks as data

router = APIRouter(
    prefix='/v1/discordwebhooks',
    tags=['DiscordWebHooks']
)

@router.get('/get/all')
def getAll() -> List[sql]:
    res = db.session.query(sql).all()
    db.session.close()
    return res

@router.get('/get/all/byName')
def getAllByName(name: str) -> sql:
    res = db.session.query(sql).filter(sql.name == name).all()
    db.session.close()
    return res

@router.get('/get/byId')
def getById(id: str) -> sql:
    res = db.session.query(sql).filter(sql.id == id).first()
    db.session.close()
    return res

@router.get('/get/byName')
def getByName(name: str) -> sql:
    res = db.session.query(sql).filter(sql.name == name).first()
    db.session.close()
    return res

@router.get('/get/byUrl')
def getByName(url: str) -> sql:
    res = db.session.query(sql).filter(sql.url == url).first()
    db.session.close()
    return res

@router.get('/get/byServer')
def getByName(name: str) -> sql:
    res = db.session.query(sql).filter(sql.name == name).first()
    db.session.close()
    return res

@router.post('/add')
def add(item:data) -> BaseMessage:
    a = sql().convertFromData(item)
    db.session.add(a)
    db.session.commit()
    db.session.close()

@router.post('/update/byId')
def updateById(id: str, item: data) -> None:
    res = db.session.query(sql).filter(sql.id == id).first()
    res.name = item.name
    res.key = item.key
    res.url = item.url
    res.server = item.server
    res.channel = item.channel
    res.enabled = item.enabled
    res.fromEnv = item.fromEnv
    db.session.add(res)
    db.session.commit()

@router.delete('/delete/byId')
def deleteById(id: str) -> None:
    res = db.session.query(sql).filter(sql.id == id).all()
    db.session.delete(res)
    db.session.commit()
    db.session.flush()
