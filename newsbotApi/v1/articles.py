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
    res = db.session.query(sql) \
        .filter(sql.id == id) \
        .first()
    db.session.close()
    return res


@router.get('/get/byUrl')
def urlExists(url: str) -> sql:
    """
    Checks the DB to see if the requested url can be found in the table
    """
    try:
        res = db.session.query(sql).filter(sql.url == url).first()
    except Exception as e:
        print(e)
    finally:
        db.session.close()
    if res is None:
        a = sql()
        a.id = ''
        return a
    else:
        return res


@router.get('/find')
def find(item: data) -> sql:
    res = db.session.query(sql) \
        .filter(sql.url == item.url) \
        .first()
    db.session.close()
    if res is None:
        b = sql()
        b.id = ''
        return b
    else:
        return res


@router.post('/add')
def add(item: data) -> sql:
    a = sql().convertFromData(item)
    db.session.add(a)
    db.session.commit()
    db.session.close()
