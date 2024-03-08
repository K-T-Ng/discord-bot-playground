from pydantic import Field
from pydantic_settings import BaseSettings

class BotConfig(BaseSettings):
    token: str = Field(alias="DISCORD_BOT_TOKEN")
