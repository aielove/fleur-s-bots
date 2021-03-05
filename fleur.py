import importlib
import os

import discord

from discord.ext import commands

from config import (
    DiscordPyConfig,
    AppConfig
)

from app.core.bot import BotUtils


client = commands.Bot(command_prefix=BotUtils.get_prefix)


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))

# Loading jishaku a dev tool
client.load_extension("jishaku")

# Loading cogs
for ext in os.listdir("app/ext"):
    if not ext.startswith("_"):
        ext = importlib.import_module(f"app.ext.{ext}")
        client.add_cog(ext.setup(client))


client.run(DiscordPyConfig.TOKEN)
