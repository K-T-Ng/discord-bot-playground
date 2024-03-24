"""Main entry point for the bot"""
import discord
from discord.ext import commands

from src.models.config import BotConfig
from src.instrumentation.initialize import init_opentelmetry

# Create a bot instance
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", description="", intents=intents)

@bot.event
async def on_ready():
    await bot.tree.sync()
    print(f"{bot.user} has connected to Discord!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    print(f"Message from {message.author}: {message.content}")
    await message.channel.send("Message received!")

@bot.tree.command(name="name", description="poc")
async def slash_command(interaction: discord.Interaction):
    await interaction.response.send_message("command")

if __name__ == "__main__":
    config = BotConfig()

    if config.otel_enable_instrumentation:
        init_opentelmetry(config, bot)

    bot.run(config.discord_bot_token)
