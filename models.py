from sqlalchemy.dialects.postgresql import JSON
#from app import db
from sqlalchemy import Column, Integer, String
from database import Base

class Reports(Base):
    __tablename__ = 'reports'

    id = Column(Integer, primary_key=True)
    type = Column(String)

    def __init__(self, type, result_all):
        self.type = type

    def __repr__(self):
        return '<type {}>'.format(self.type)