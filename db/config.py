from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

import json, os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SECRET_FILE = os.path.join(BASE_DIR, 'secret.json')
secrets = json.loads(open(SECRET_FILE).read())
DB = secrets["DB"]

DATABASE_URL = f"mysql+aiomysql://{DB['user']}:{DB['password']}@{DB['host']}:{DB['port']}/{DB['database']}?charset=utf8"

engine = create_async_engine(DATABASE_URL, pool_recycle=500, future=True, echo=True)
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

Base = declarative_base()

HASH_SALT = secrets["HASH_SALT"]