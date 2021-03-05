import discord
from discord.ext import commands

from .config import Test
from config import DiscordPyConfig


class Misc(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.description = "abc"

        self.default_guild_config = {}

    @commands.command()
    async def hello(self, ctx):
        """Says hello"""
        await ctx.send(f"hi {Test.TEXT}, {DiscordPyConfig.TOKEN}")
