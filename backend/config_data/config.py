from pydantic_settings import BaseSettings
from pydantic import PostgresDsn, EmailStr, Field
from pathlib import Path
from typing import Optional

BASE_DIR = Path(__file__).resolve().parent.parent


class DjangoConfig(BaseSettings):
    secret_key: Optional[str] = Field(default=None, validation_alias="SECRET_KEY")
    debug: bool = Field(default=True, validation_alias="DEBUG")
    allowed_hosts: Optional[str] = Field(default=None, validation_alias="ALLOWED_HOSTS")
    db_url: Optional[PostgresDsn] = Field(default=None, validation_alias="PRIMARY_DATABASE_URL")

    superuser_username: Optional[str] = Field(
        default=None, validation_alias="DJANGO_SUPERUSER_USERNAME"
    )
    superuser_password: Optional[str] = Field(
        default=None, validation_alias="DJANGO_SUPERUSER_PASSWORD"
    )
    superuser_email: Optional[EmailStr] = Field(
        default=None, validation_alias="DJANGO_SUPERUSER_EMAIL"
    )

    model_config = {
        "env_file": str(Path(__file__).resolve().parents[2] / ".env"),
        "extra": "ignore"
        }
