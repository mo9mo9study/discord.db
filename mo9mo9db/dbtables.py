from datetime import datetime

from sqlalchemy import Column, String, Integer, DateTime, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Studytimelogs(Base):
    __tablename__ = "studytimelogs"
    no = Column(Integer, primary_key=True, autoincrement=True)
    study_dt = Column(DateTime, unique=False)
    guild_id = Column(String(20), unique=False)
    member_id = Column(String(20), unique=False)
    voice_id = Column(String(20), unique=False)
    studytime_min = Column(Integer, unique=False)
    tag_id = Column(String(20), unique=False)

    def __init__(self, study_dt=None, guild_id=None, member_id=None, voice_id=None, studytime_min=None, studytag_no=None):
        self.study_dt = study_dt
        self.guild_id = guild_id
        self.member_id = member_id
        self.voice_id = voice_id
        self.studytime_min = studytime_min
        self.studytag_no = studytag_no


class Studymembers(Base):
    __tablename__ = "studymembers"
    update_dt = Column(DateTime(timezone=True), onupdate=datetime.now(), unique=False)
    guild_id = Column(String(20), unique=False)
    member_id = Column(String(20), unique=True, primary_key=True)
    member_name = Column(String(40), unique=True)
    selfintroduction_id = Column(String(20), unique=True)
    times_id = Column(String(20), unique=True)
    joined_dt = Column(DateTime, unique=False)
    organize = Column(Boolean)
    enrollment = Column(Boolean) 
    
    def __init__(self, guild_id=None, member_id=None, member_name=None, selfintroduction_id=None, times_id=None, joined_dt=None, organize=None, enrollment=None):
    #def __init__(self, update_dt=None, guild_id=None, member_id=None, member_name=None, selfintroduction_id=None, attendance=None):
        #self.update_dt = update_dt
        self.guild_id = guild_id
        self.member_id = member_id
        self.member_name = member_name
        self.selfintroduction_id = selfintroduction_id
        self.times_id = times_id
        self.joined_dt = joined_dt 
        self.organize = organize 
        self.enrollment = enrollment
    

class Studytags(Base):
    __tablename__ = "studytags"
    no = Column(Integer, primary_key=True, autoincrement=True)
    update_dt = Column(DateTime(timezone=True), onupdate=datetime.now(), unique=False)
    member_id = Column(String(20), unique=True)
    tag_name = Column(String(40), unique=True)
    tag_default = Column(Boolean)

    def __init__(self, member_id=None, tag_name=None, tag_default=None):
        self.member_id = member_id
        self.tag_name = tag_name
        self.tag_default = tag_default