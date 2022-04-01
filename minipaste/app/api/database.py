import sqlite3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


def create_session(connection_string) -> Session:
    """Create session and engine on request"""
    engine = create_engine(connection_string)
    Session = sessionmaker(bind=engine)
    session = Session()
    session._model_changes = {}
    return Session()
