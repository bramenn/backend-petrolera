from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

from .config import POSTGRES_URI

conn = create_engine(POSTGRES_URI)

Session = sessionmaker(bind=conn)

session = Session()
Base = declarative_base()
