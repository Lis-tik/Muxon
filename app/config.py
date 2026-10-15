from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parent.parent


class Settings(BaseSettings):
    app_name: str = "Muxon"
    app_env: str = "development"
    app_debug: bool = True
    host: str = "0.0.0.0"
    port: int = 8000
    input_dir: str = str(BASE_DIR / "data" / "input")
    output_dir: str = str(BASE_DIR / "outputs")
    template_dir: str = str(BASE_DIR / "app" / "templates")
    log_level: str = "INFO"

    model_config = SettingsConfigDict(env_file=".env", env_prefix="", case_sensitive=False)


@lru_cache
def get_settings() -> Settings:
    return Settings()


settings = get_settings()
