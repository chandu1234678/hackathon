import os
from functools import lru_cache

from pydantic import BaseModel


class Settings(BaseModel):
	app_name: str = os.getenv("APP_NAME", "Diabetic Ulcer AI System")
	app_version: str = os.getenv("APP_VERSION", "1.0.0")
	log_level: str = os.getenv("LOG_LEVEL", "INFO")
	database_url: str = os.getenv("DATABASE_URL", "sqlite:///./hackathon.db")
	cors_origins: str = os.getenv("CORS_ORIGINS", "*")

	@property
	def cors_origins_list(self) -> list[str]:
		if self.cors_origins.strip() == "*":
			return ["*"]
		return [origin.strip() for origin in self.cors_origins.split(",") if origin.strip()]


@lru_cache
def get_settings() -> Settings:
	return Settings()


settings = get_settings()
