"""Runtime configuration defaults for the rt-recall service."""

from __future__ import annotations

import os
from dataclasses import dataclass, field

SERVICE_NAME = "rt-recall"
DEFAULT_HOST = "0.0.0.0"
DEFAULT_PORT = 8000
DEFAULT_LOG_LEVEL = "INFO"
DEFAULT_ENV = "development"
DEFAULT_API_PREFIX = "/api"
DEFAULT_ALLOWED_ORIGINS = "*"


def _get_bool(name: str, default: bool) -> bool:
    value = os.getenv(name)
    if value is None:
        return default
    return value.strip().lower() in {"1", "true", "yes", "on"}


def _get_int(name: str, default: int) -> int:
    value = os.getenv(name)
    if value is None:
        return default
    try:
        return int(value)
    except ValueError:
        return default


@dataclass(frozen=True)
class Settings:
    """Application configuration with environment overrides."""

    app_name: str = field(default=SERVICE_NAME)
    env: str = field(default_factory=lambda: os.getenv("RT_RECALL_ENV", DEFAULT_ENV))
    debug: bool = field(default_factory=lambda: _get_bool("RT_RECALL_DEBUG", False))
    host: str = field(default_factory=lambda: os.getenv("RT_RECALL_HOST", DEFAULT_HOST))
    port: int = field(default_factory=lambda: _get_int("RT_RECALL_PORT", DEFAULT_PORT))
    log_level: str = field(
        default_factory=lambda: os.getenv("RT_RECALL_LOG_LEVEL", DEFAULT_LOG_LEVEL)
    )
    api_prefix: str = field(
        default_factory=lambda: os.getenv("RT_RECALL_API_PREFIX", DEFAULT_API_PREFIX)
    )
    allowed_origins: str = field(
        default_factory=lambda: os.getenv(
            "RT_RECALL_ALLOWED_ORIGINS", DEFAULT_ALLOWED_ORIGINS
        )
    )


settings = Settings()

APP_NAME = settings.app_name
ENV = settings.env
DEBUG = settings.debug
HOST = settings.host
PORT = settings.port
LOG_LEVEL = settings.log_level
API_PREFIX = settings.api_prefix
ALLOWED_ORIGINS = settings.allowed_origins

__all__ = [
    "Settings",
    "settings",
    "APP_NAME",
    "ENV",
    "DEBUG",
    "HOST",
    "PORT",
    "LOG_LEVEL",
    "API_PREFIX",
    "ALLOWED_ORIGINS",
]
