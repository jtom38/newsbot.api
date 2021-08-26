from pydantic import BaseModel
from enum import Enum


class MessageStatus(Enum):
    OK = 'ok'
    FAIL = 'fail'


class BaseMessage(BaseModel):
    status: MessageStatus


class OkMessage(BaseMessage):
    status: MessageStatus = MessageStatus


class ErrorMessage(BaseMessage):
    status: MessageStatus = MessageStatus.FAIL
    exception: str = ''
