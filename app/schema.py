from datetime import datetime
from typing import Optional

from pydantic import BaseModel


# Model untuk respon API (GET)
class BookRead(BaseModel):
    id: int
    title: str
    author: str
    description: str
    created_at: datetime
    updated_at: datetime
    review: Optional[str] = None
    category: Optional[str] = None


# Model untuk payload pembuatan buku (POST)
class BookCreate(BaseModel):
    title: str
    author: str
    description: str
    review: Optional[str] = None
    category: Optional[str] = None


# Model untuk payload pembaruan buku (PATCH)
class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    description: Optional[str] = None
    review: Optional[str] = None
    category: Optional[str] = None
