from typing import List
from fastapi import APIRouter
from fastapi_sqlalchemy import db
from newsbotApi.sql.sqlSchema import Articles as sql
from newsbotApi.sql.dataSchema import Articles as data

router = APIRouter(
    prefix='/v1/articles',
    tags=['Articles']
)

@router.get('/getAll')
def getAll() -> List[sql]:
    res = db.session.query(sql).all()
    db.session.close()
    return res

@router.get('/get/byId')
def getById(id: str) -> sql:
    """
    Returns a single Article, by ID.
    """
    res = db.session.query(sql).filter(sql.id == id)
    db.session.close()
    return res

@router.get('/urlExists')
def urlExists(url: str) -> bool:
    """
    Checks the DB to see if the requested url can be found in the table
    """
    res = db.session.query(sql).filter(sql.url == url)
    try:
        if (len(res) == 0):
            return {"exists": False}
        else:
            return {"exists": True}
    except:
        return {"exists": False}

@router.get('/find')
def find(item: data) -> sql:
    res = db.session.query(sql) \
        .filter(sql.url == item.url) \
        .first()
    db.session.close()
    if res == None:
        b = sql()
        b.id = ''
        return b
    else: 
        return res

@router.post('/add')
def add(item:data) -> None:
    a = sql().convertFromData(item)
    db.session.add(a)
    db.session.commit()
    db.session.close()
