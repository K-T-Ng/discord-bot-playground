"""Application setting model"""
from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings

class BotConfig(BaseSettings):
    discord_bot_token: str = Field(alias="DISCORD_BOT_TOKEN")

    otel_enable_instrumentation: bool = Field(alias="OTEL_ENABLE_INSTRUMENTATION")
    otel_otlp_exporter_http_endpoint: Optional[str] = Field(alias="OTEL_OTLP_EXPORTER_HTTP_ENDPOINT")
