import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# DATABASE_URL will be read from environment variables if set
# Otherwise, it falls back to local Postgres with defaults
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "postgresql+psycopg://devuser:devpass@localhost:5432/appdb"
)

engine = create_engine(DATABASE_URL, echo=False)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)
