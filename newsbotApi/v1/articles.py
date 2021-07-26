from typing import List
from fastapi import APIRouter
from fastapi_sqlalchemy import db
from newsbotApi.sql.sqlSchema import Articles

router = APIRouter(
    prefix='/v1/articles'
)

@router.get('/getAll')
def getAll() -> List[Articles]:
    res = db.session.query(Articles).all()
    db.session.close()
    return res

@router.get('/getSingleById')
def getById(id: str) -> Articles:
    """
    Returns a single Article, by ID.
    """
    res = db.session.query(Articles).filter(Articles.id == id)
    db.session.close()
    return res

@router.get('/urlExists')
def urlExists(url: str) -> bool:
    """
    Checks the DB to see if the requested url can be found in the table
    """
    res = db.session.query(Articles).filter(Articles.url == url)
    try:
        if (len(res) == 0):
            return {"exists": False}
        else:
            return {"exists": True}
    except:
        return {"exists": False}

