from typing import List
from fastapi import APIRouter
from fastapi_sqlalchemy import db
from sqlalchemy import sql
from sqlalchemy.util.compat import b
#from newsbotApi.common.messages import *
from newsbotApi.sql.sqlSchema import Settings as sql
from newsbotApi.sql.dataSchema import Settings as data

router = APIRouter(
    prefix='/v1/settings',
    tags=['Settings']
)

@router.get('/get/all')
def getAll() -> List[sql]:
    res = db.session.query(sql).all()
    db.session.close()
    return res

@router.get('/get/byKey')
def getByKey(key: str) -> sql:
    res = db.session.query(sql).filter(sql.key == key).first()
    db.session.close()
    return res

@router.get('/find')
def find(item:data) -> sql:
    res = db.session.query(sql) \
        .filter(sql.key == item.key) \
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
def update(id: str, item: data) -> None:
    res = db.session.query(sql) \
        .filter(sql.id == id) \
        .first()
    res.key = item.key
    res.value = item.value
    res.options = item.options
    res.notes = item.notes
    db.session.add(res)
    db.session.close()

@router.delete('/delete/byId')
def delete(id: str) -> None:
    res = db.session.query(sql) \
        .filter(sql.id == id) \
        .first()
    db.session.delete(res)
    db.session.commit()
    db.session.close()

