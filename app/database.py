import os
from datetime import datetime
from typing import Optional

from dotenv import load_dotenv
from sqlalchemy import Column, DateTime
from sqlalchemy.sql import func
from sqlmodel import Field, Session, SQLModel, create_engine

load_dotenv(override=True)

engine = create_engine(os.environ.get("DATABASE_URL", "sqlite:///./dev.db"))


def get_db_session():
    with Session(engine) as session:
        yield session


class Book(SQLModel, table=True):
    __tablename__ = "books"

    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    author: str = Field(index=True)
    description: str
    review: Optional[str] = None
    category: Optional[str] = None
    created_at: datetime = Field(
        sa_column=Column(DateTime(timezone=True), server_default=func.now())
    )
    updated_at: datetime = Field(
        sa_column=Column(
            DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
        )
    )
