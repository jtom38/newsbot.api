from pydantic import BaseModel
from datetime import date
from typing import Optional
from uuid import uuid4


class Articles(BaseModel):
    id: str
    sourceId: Optional[str]
    tags: Optional[str]
    title: Optional[str]
    url: Optional[str]
    pubDate: Optional[str]
    video: Optional[str]
    videoHeight: Optional[int]
    videoWidth: Optional[int]
    thumbnail: Optional[str]
    description: Optional[str]
    authorName: Optional[str]
    authorImage: Optional[str]

    class Config:
        orm_mode = True


class ArticlesV1(BaseModel):
    """
    This model was phased out in 0.8.0
    """
    id: Optional[str]
    siteName: Optional[str]
    sourceName: Optional[str]
    sourceType: Optional[str]
    tags: Optional[str]
    title: Optional[str]
    url: Optional[str]
    pubDate: Optional[str]
    video: Optional[str]
    videoHeight: Optional[int]
    videoWidth: Optional[int]
    thumbnail: Optional[str]
    description: Optional[str]
    authorName: Optional[str]
    authorImage: Optional[str]

    class Config:
        orm_mode = True


class DiscordQueue(BaseModel):
    """
    This was added in 0.8.0
    """
    id: str
    articleId: str

    # search for the articleId
    # then search the article for the sourceId
    # Take the sourceId and search DiscordLinks for the links between discord and sources

    class Config:
        orm_mode = True


class DiscordQueueV1(BaseModel):
    """
    This model was phased out in 0.8.0
    """
    id: str
    siteName: Optional[str]
    title: Optional[str]
    link: Optional[str]
    tags: Optional[str]
    thumbnail: Optional[str]
    description: Optional[str]
    video: Optional[str]
    videoHeight: Optional[int]
    videoWidth: Optional[int]
    authorName: Optional[str]
    authorImage: Optional[str]
    sourceName: Optional[str]
    sourceType: Optional[str]

    class Config:
        orm_mode = True


class DiscordWebHooks(BaseModel):
    id: Optional[str]
    name: Optional[str]
    key: Optional[str]
    url: Optional[str]
    server: Optional[str]
    channel: Optional[str]
    enabled: bool
    fromEnv: bool

    class Config:
        orm_mode = True


class Icons(BaseModel):
    id: Optional[str]
    filename: Optional[str]
    site: Optional[str]

    class Config:
        orm_mode = True


class Settings(BaseModel):
    id: Optional[str]
    key: Optional[str]
    value: Optional[str]
    options: Optional[str]
    notes: Optional[str]

    class Config:
        orm_mode = True


class Sources(BaseModel):
    id: Optional[str]
    site: Optional[str]
    name: Optional[str]
    source: Optional[str]
    type: Optional[str]
    value: Optional[str]
    enabled: bool
    url: Optional[str]
    tags: Optional[str]
    fromEnv: bool

    class Config:
        orm_mode = True


class DiscordLinks():
    """
    This class is a table that shows how a DiscordWebHook links back to a Source object.
    """
    id: str
    sourceId: str
    discordId: str

    class Config:
        orm_mode = True


class SourceLinks(BaseModel):
    id: Optional[str]
    sourceID: Optional[str]
    sourceType: Optional[str]
    sourceName: Optional[str]
    # sourceData: Optional[Sources]
    discordName: Optional[str]
    discordID: Optional[str]
    # discordData: Optional[DiscordWebHooks]

    class Config:
        orm_mode = True
