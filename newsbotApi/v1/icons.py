from typing import List
from fastapi import APIRouter
from fastapi_sqlalchemy import db
from sqlalchemy import sql
from newsbotApi.common.messages import *
from newsbotApi.sql.sqlSchema import Icons as sql
from newsbotApi.sql.dataSchema import Icons as data

router = APIRouter(
    prefix='/v1/icons',
    tags=['Icons']
)

@router.get('/get/all')
def getAll() -> List[sql]:
    res = db.session.query(sql).all()
    db.session.close()
    return res

@router.get('/get/bySite')
def getBySite(site: str) -> sql:
    res = db.session.query(sql).filter(sql.site == site).first()
    db.session.close()
    return res

@router.get('/find')
def find(item:data) -> None:
    res = db.session.query(sql) \
        .filter(sql.filename == item.filename) \
        .filter(sql.site == item.site) \
        .first()
    db.session.close()
    if res == None:
        b = sql()
        b.id = ''
        return b
    else: 
        return res

@router.post('/add')
def add(item: data) -> None:
    a = sql().convertFromData(item)
    db.session.add(a)
    db.session.commit()
    db.session.close()

@router.post('/update/byId')
def updateById(id: str, item:data) -> sql:
    a = db.session.query(sql).filter(sql.id == id).first()
    a.site = item.site
    a.filename = item.filename
    db.session.add(a)
    db.session.commit()
    db.session.close()

@router.delete('/delete/bySite')
def delete(site: str) -> None:
    res = db.session.query(sql).filter(sql.site == site).first()
    db.session.delete(res)
    db.session.commit()
    db.session.close()
