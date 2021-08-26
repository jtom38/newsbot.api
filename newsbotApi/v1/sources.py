from typing import List
from fastapi import APIRouter
from fastapi_sqlalchemy import db
from newsbotApi.sql.sqlSchema import Sources as sql
from newsbotApi.sql.dataSchema import Sources as data

router = APIRouter(
    prefix='/v1/sources',
    tags=['Sources']
)


@router.get('/get/all')
def getAll() -> List[sql]:
    res = db.session.query(sql).all()
    db.session.close()
    return res


@router.get("/get/all/byName")
def getAllByName(name: str) -> List[sql]:
    res = db.session.query(sql).filter(sql.name == name).all()
    db.session.close()
    return res


@router.get("/get/all/byType")
def getAllBySourceType(type: str) -> List[sql]:
    res = db.session.query(sql).filter(sql.type == type).all()
    db.session.close()
    return res


@router.get("/get/all/bySource")
def getAllBySource(source: str) -> List[sql]:
    res = db.session.query(sql).filter(sql.source == source).all()
    db.session.close()
    return res


@router.get('/get/all/byNameAndType')
def getAllByNameAndType(name: str, type: str) -> List[sql]:
    res = db.session.query(sql).filter(sql.name == name and sql.type == type).all()
    db.session.close()
    return res


@router.get('/get/all/byNameAndSource')
def getAllByNameAndSource(name: str, source: str) -> List[sql]:
    res = db.session.query(sql)\
        .filter(sql.name == name and sql.source == source)\
        .all()
    db.session.close()
    return res


@router.get('/get/byName')
def getByName(name: str) -> sql:
    res = db.session.query(sql).filter(sql.name == name).first()
    db.session.close()
    return res


@router.get('/get/byId')
def getById(id: str) -> sql:
    res = db.session.query(sql).filter(sql.id == id).first()
    db.session.close()
    return res


@router.get('/get/byNameAndSource')
def getByNameAndType(name: str, source: str) -> sql:
    res = db.session.query(sql).filter(sql.name == name and sql.source == source).first()
    db.session.close()
    return res


@router.get('/get/byNameSourceType')
def getByNameSourceType(name: str, source: str, type: str) -> sql:
    res = db.session.query(sql)\
        .filter(sql.name == name and sql.type == type and sql.source == source)\
        .first()
    db.session.close()
    return res


@router.get('/get/bySource')
def getBySource(source: str) -> sql:
    res = db.session.query(sql)\
        .filter(sql.source == source)\
        .first()
    db.session.close()
    return res


@router.get('/find')
def find(item: data) -> sql:
    res = db.session.query(sql) \
        .filter(sql.name == item.name) \
        .filter(sql.site == item.site) \
        .filter(sql.type == item.type) \
        .filter(sql.source == item.source) \
        .filter(sql.value == item.value) \
        .filter(sql.url == item.url) \
        .first()
    db.session.close()
    if res is None:
        b = sql()
        b.id = ''
        return b
    else:
        return res


@router.post("/add")
def add(item: data) -> None:
    s = sql().convertFromData(item)
    db.session.add(s)
    db.session.commit()
    db.session.close()


@router.post('/update/byId')
def updateById(id: str, item: data) -> sql:
    res = db.session.query(sql).filter(sql.id == id).first()
    res.name = item.name
    res.source = item.source
    res.type = item.type
    res.value = item.value
    res.enabled = item.enabled
    res.url = item.url
    res.tags = item.tags
    res.fromEnv = item.fromEnv
    db.session.add(res)
    db.session.commit()


@router.delete('/delete/byId')
def delete(id: str) -> None:
    s = db.session.query(sql).filter(sql.id == id).first()
    db.session.delete(s)
    db.session.commit()
    db.session.close()
