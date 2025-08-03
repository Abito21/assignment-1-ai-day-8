from fastapi import FastAPI

from app.settings import settings

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    docs_url=settings.DOC_URL,
    redoc_url=settings.REDOC_URL,
)
