from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# SQLALCHEMY_DATABASE_URL = "sqlite:///todos.db" # Connection string for SQLite database


# engine = create_engine(
#   POSTGRES_DATABASE_URL, connect_args={"check_same_thread": False} # SQLite engine
# )

POSTGRES_DATABASE_URL = "postgresql://dark-lord:database@localhost/TodoAppDB" # Connection string for PostgreSQL database

engine = create_engine(
  POSTGRES_DATABASE_URL # PostgreSQL engine
)

SessionLocal = sessionmaker(bind=engine, autoflush=False, expire_on_commit=False)

Base = declarative_base()