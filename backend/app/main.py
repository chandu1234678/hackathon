import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router
from app.core.config import settings
from app.db.database import Base, engine
from app.db import models  # noqa: F401


def configure_logging() -> None:
    logging.basicConfig(
        level=getattr(logging, settings.log_level.upper(), logging.INFO),
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    )


configure_logging()
logger = logging.getLogger(__name__)


def create_database_tables() -> None:
    Base.metadata.create_all(bind=engine)


app = FastAPI(title=settings.app_name, version=settings.app_version)


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router)


@app.on_event("startup")
async def startup_event() -> None:
    create_database_tables()
    logger.info("Database tables initialized")


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Diabetic Ulcer AI System running"}