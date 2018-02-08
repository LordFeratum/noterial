from sqlalchemy import Column, DateTime, Integer, String, Text, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Note(Base):
    __tablename__ = 'messages'
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String(40), nullable=True)
    message = Column(Text)
    timestamp = Column(DateTime(), server_default=func.now(), nullable=True)


notes = Note.__table__
