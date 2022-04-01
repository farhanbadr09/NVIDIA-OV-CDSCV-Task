from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Paste(Base):
    """Paste Objects storing generic content"""

    __tablename__ = "pastes"

    _id = Column(Integer, primary_key=True)
    content = Column(String)

    def __init__(self, content):
        self.content = content

    def __repr__(self):
        return f"\npaste-id: {self._id}\npaste: {self.content}"

    def json(self):
        """ json representation for easy returning """
        return {"_id": self._id, "content": self.content}
