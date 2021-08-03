from typing import List
from fastapi import APIRouter
from fastapi_sqlalchemy import db
from sqlalchemy.sql.expression import true
from newsbotApi.sql.sqlSchema import SourceLinks as sql
from newsbotApi.sql.dataSchema import SourceLinks as data

router = APIRouter(
    prefix='/v1/sourcelinks',
    tags=['SourceLinks']
)

@router.get('/get/all')
def getAll() -> List[sql]:
    res = db.session.query(sql).all()
    db.session.close()
    return res

@router.get('/get/all/bySourceName')
def getAllBySourceName(sourceName: str) -> List[sql]:
    res = db.session.query(sql).filter(sql.sourceName == sourceName).first()
    res.sourceData = db.session.query(sql).filter(sql.sourceID )
    db.session.close()
    return res

@router.get('/get/all/bySourceType')
def getAllBySourceName(sourceType: str) -> List[sql]:
    res = db.session.query(sql).filter(sql.sourceType == sourceType).first()
    db.session.close()
    return res

@router.get('/get/all/bySourceNameAndType')
def getAllBySourceName(sourceName:str, sourceType: str) -> List[sql]:
    res = db.session.query(sql).filter(
        sql.sourceName == sourceName and sql.sourceType == sourceType
        ).all()
    db.session.close()
    return res

@router.get('/exists')
def exists(item: data) -> sql:
    res = db.session.query(sql) \
        .filter(sql.sourceName == item.sourceName) \
        .filter(sql.sourceType == item.sourceType) \
        .filter(sql.discordName == item.discordName) \
        .first()
    db.session.close()
    if res == None:
        blank = sql()
        blank.id =  ''
        return blank
    else: 
        return res

@router.get('/get/bySourceNameAndSourceTypeAndDiscordName')
def getAllBySourceNameAndSourceTypeAndDiscordName(sourceName:str, sourceType:str,discordName:str) -> List[sql]:
    res = db.session.query(sql).filter(
        sql.sourceName == sourceName and sql.sourceType == sourceType and sql.discordName == discordName
    ).all()
    db.session.close()
    return res

@router.get('/get/all/bySourceName')
def getAllBySourceName(sourceId: str) -> List[sql]:
    res = db.session.query(sql).filter(sql.sourceName == sourceId).first()
    db.session.close()
    return res

@router.get('/get/all/byDiscordId')
def getAllByDiscordId(sourceId: str) -> List[sql]:
    res = db.session.query(sql).filter(sql.sourceName == sourceId).first()
    db.session.close()
    return res

@router.post('/add')
def add(item:data) -> None:
    s = sql().convertFromData(item)
    db.session.add(s)
    db.session.commit()
    db.session.close()

@router.post('/update/byId')
def update(id: str, item:data) -> None:
    res = db.session.query(sql).filter(sql.id == id).first()
    res.sourceID = item.sourceID
    res.sourceType = item.sourceType
    res.sourceName = item.sourceName
    res.discordID = item.discordID
    res.discordName = item.discordName
    db.session.add(res)
    db.session.commit()

@router.delete('/delete/byId')
def deleteById(id: str) -> None:
    s = db.session.query(sql).filter(sql.id == id).first()
    db.session.delete(s)
    db.session.commit()
    db.session.close()
