import uuid
from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.types import Date
from newsbotApi.sql.database import Base
from newsbotApi.common.constant import SourceName, SourceType


class Articles(Base):
    __tablename__ = "articles"
    id = Column(String, primary_key=True)
    sourceId: str = Column(String)
    tags = Column(String)
    title = Column(String)
    url = Column(String)
    pubDate = Column(String)
    video = Column(String)
    videoHeight = Column(Integer)
    videoWidth = Column(Integer)
    thumbnail = Column(String)
    description = Column(String)
    authorName = Column(String)
    authorImage = Column(String)

    def __init__(
        self,
        sourceId: str = '',
        tags: str = "",
        title: str = "",
        url: str = "",
        pubDate: str = "",
        video: str = "",
        videoHeight: int = 0,
        videoWidth: int = 0,
        thumbnail: str = "",
        description: str = "",
        authorName: str = "",
        authorImage: str = "",
    ) -> None:
        self.id = str(uuid.uuid4())
        self.sourceId = sourceId
        self.tags = tags
        self.title = title
        self.url = url
        self.pubDate = pubDate
        self.video = video
        self.videoHeight = videoHeight
        self.videoWidth = videoWidth
        self.thumbnail = thumbnail
        self.description = description
        self.authorName = authorName
        self.authorImage = authorImage

    def convertFromData(self, item: object) -> object:
        a = Articles()
        a.sourceId = item.sourceId
        a.tags = item.tags
        a.title = item.title
        a.url = item.url
        a.pubDate = item.pubDate
        a.video = item.video
        a.videoHeight = item.videoHeight
        a.videoWidth = item.videoWidth
        a.thumbnail = item.thumbnail
        a.description = item.description
        a.authorName = item.authorName
        a.authorImage = item.authorImage
        return a


class DiscordQueue(Base):
    __tablename__ = "discordQueue"
    id = Column(String, primary_key=True)
    articleId: str = Column(String)

    def __init__(self) -> None:
        self.id = str(uuid.uuid4())

    def convertFromData(self, data: object) -> None:
        res = DiscordQueue()
        res.articleId = data.articleId
        return res


class DiscordQueueV1():
    __tablename__ = "discordQueue"
    id = Column(String, primary_key=True)
    articlesId: str
    # siteName = Column(String)
    # title = Column(String)
    # link = Column(String)
    # tags = Column(String)
    # thumbnail = Column(String)
    # description = Column(String)
    # video = Column(String)
    # videoHeight = Column(Integer)
    # videoWidth = Column(Integer)
    # authorName = Column(String)
    # authorImage = Column(String)
    # sourceName = Column(String)
    # sourceType = Column(String)

    def __init__(self) -> None:
        self.id = str(uuid.uuid4())

    def convertFromData(self, data: object) -> None:
        res = DiscordQueue()
        res.siteName = data.siteName
        res.title = data.title
        res.link = data.link
        res.tags = data.tags
        res.thumbnail = data.thumbnail
        res.description = data.description
        res.video = data.video
        res.videoHeight = data.videoHeight
        res.videoWidth = data.videoWidth
        res.authorName = data.authorName
        res.authorImage = data.authorImage
        res.sourceName = data.sourceName
        res.sourceType = data.sourceType
        return res


class DiscordWebHooks(Base):
    __tablename__ = "discordwebhooks"
    id = Column(String, primary_key=True)
    name = Column(String)
    key = Column(String)
    url = Column(String)
    server = Column(String)
    channel = Column(String)
    enabled = Column(Boolean)
    fromEnv = Column(Boolean)

    def __init__(
        self,
        name: str = "",
        key: str = "",
        server: str = "",
        channel: str = "",
        url: str = "",
        fromEnv: bool = False
    ) -> None:
        self.name = name
        self.id = str(uuid.uuid4())
        self.server = server
        self.channel = channel
        if name == "":
            self.name = self.__generateName__()
        else:
            self.name = name
        self.key = key
        self.url = url
        self.enabled = True
        self.fromEnv: bool = fromEnv

    def convertFromData(self, data: object) -> None:
        res = DiscordWebHooks()
        if data.id != '':
            res.id = data.id
        res.name = data.name
        res.key = data.key
        res.url = data.url
        res.server = data.server
        res.channel = data.channel
        res.enabled = data.enabled
        res.fromEnv = data.fromEnv
        return res

    def __generateName__(self) -> str:
        return f"{self.server} - {self.channel}"


class Icons(Base):
    __tablename__ = "icons"
    id = Column(String, primary_key=True)
    filename = Column(String)
    site = Column(String)

    def __init__(self, fileName: str = "", site: str = "") -> None:
        self.id = str(uuid.uuid4())
        self.filename = fileName
        self.site = site

    def convertFromData(self, data: object) -> object:
        res = Icons(
            fileName=data.filename,
            site=data.site
        )
        return res


class Settings(Base):
    __tablename__ = "settings"
    id = Column("id", String, primary_key=True)
    key = Column("key", String)
    value = Column("value", String)
    options = Column("options", String)
    notes = Column("notes", String)

    def __init__(
        self, key: str = "", value: str = "", options: str = "", notes: str = ""
    ):
        self.id = str(uuid.uuid4())
        self.key = key
        self.value = value
        self.options = options
        self.notes = notes

    def convertFromData(self, item: object) -> object:
        res = Settings()
        res.key = item.key
        res.notes = item.notes
        res.options = item.options
        res.value = item.value
        return res


class Sources(Base):
    __tablename__ = "sources"
    id: str = Column(String, primary_key=True)
    site: str = Column(String)
    name: str = Column(String)
    source: str = Column(String)
    type: str = Column(String)
    value: str = Column(String)
    enabled: bool = Column(Boolean)
    url: str = Column(String)
    tags: str = Column(String)
    fromEnv: bool = Column(Boolean)

    def __init__(
        self,
        id: str = "",
        site: str = "",
        name: str = "",
        source: str = "",
        type: str = "",
        value: str = "",
        enabled: bool = True,
        url: str = "",
        tags: str = "",
        fromEnv: bool = False
    ) -> None:
        self.id = str(uuid.uuid4())
        self.site: str = site
        self.name: str = name
        self.source: str = source
        self.type: str = type
        self.value: str = value
        self.enabled: bool = enabled
        self.url: str = url
        self.tags: str = tags
        self.fromEnv: bool = fromEnv

    def convertFromData(self, item: object) -> object:
        s = Sources()
        s.site = item.site
        s.name = item.name
        s.source = item.source
        s.type = item.type
        s.value = item.value
        s.enabled = item.enabled
        s.url = item.url
        s.tags = item.tags
        s.fromEnv = item.fromEnv
        return s


class SourceLinks(Base):
    __tablename__ = "sourcelinks"
    id = Column("id", String, primary_key=True)
    sourceID: str = Column("sourceID", String)
    sourceType: str = Column('sourceType', String)
    sourceName: str = Column("sourceName", String)
    discordName: str = Column("discordName", String)
    discordID: str = Column("discordID", String)

    def __init__(self, sourceName: SourceName = "", sourceID: str = "", sourceType: str = '', discordName: str = '', discordID: str = ""):
        self.id = str(uuid.uuid4())
        self.sourceID = sourceID
        self.sourceType = sourceType
        self.sourceName = sourceName
        # self.sourceData = Source
        self.discordID = discordID
        self.discordName = discordName

    def convertFromData(self, item: object) -> object:
        s = SourceLinks()
        s.sourceID = item.sourceID
        s.sourceType = item.sourceType
        s.sourceName = item.sourceName
        s.discordID = item.discordID
        s.discordName = item.discordName
        return s
