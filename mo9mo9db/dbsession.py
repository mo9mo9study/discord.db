# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy_utils import database_exists, create_database, drop_database
from sqlalchemy.ext.declarative import declarative_base

import dbconfig as cfg


Base = declarative_base()

def get_db_session():
    """
    SQL Alchemy のDBセッションを生成して使い回す
    :rtype : scoped_session
    """
    # DBセッションの生成
    engine = get_db_engine()
    db_session = scoped_session(sessionmaker(autocommit=False,
                                             autoflush=False,
                                             bind=engine))
    return db_session


def get_db_engine():
    db_path = f'mysql+pymysql://{cfg.DB_user}:{cfg.DB_password}@{cfg.DB_host}:{cfg.DB_port}/{cfg.DB_database}'
    engine = create_engine(db_path, 
                           encoding='utf-8', 
                           pool_size=5, 
                           convert_unicode=True, 
                           echo=True)
    if not database_exists(engine.url): # DBの存在チェックと作成用
        create_database(engine.url)
    return engine