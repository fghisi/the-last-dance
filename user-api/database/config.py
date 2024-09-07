from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from environment import get_database_url

engine = create_engine(get_database_url())


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


def get_session():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
