import discord
from discord.ext import commands

from .config import CogConfig

from config import (
    DiscordPyConfig,
    AppConfig
)


class Test(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.description = "Test cogs to demonstrate guild in database"

        self.cog_config = CogConfig

        self.default_guild_config = {"test_arg": True}

    @commands.command()
    async def he(self, ctx):
        await ctx.send("yolo")
