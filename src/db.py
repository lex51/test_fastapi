# import os
from os import getenv as os_ge

from databases import Database
from sqlalchemy import create_engine, MetaData


DATABASE_URL = os.getenv(f"DATABASE_URL")
DATABASE_URL = f"postgresql://{os_ge(POSTGRES_USER)}:{os_ge(POSTGRES_PASSWORD)}@{os_ge(POSTGRES_HOST)}:{os_ge(POSTGRES_PORT)}/{os_ge(POSTGRES_DB)}"

engine = create_engine(DATABASE_URL)
metadata = MetaData()


database = Database(DATABASE_URL)
