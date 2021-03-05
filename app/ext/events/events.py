import discord
from discord.ext import commands

from .config import CogConfig

from config import (
    DiscordPyConfig,
    AppConfig
)


class Events(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.description = "Base event for the bot, there is no features here just needed listeners"

        self.cog_config = CogConfig

        self.default_guild_config = {}

    @commands.Cog.listener()
    async def on_guild_join(self, guild):

        guild_dict = AppConfig.GUILD_CTX_SAMPLE

        guild_dict["name"] = guild.name
        guild_dict["id"] = guild.id

        for _, extension_obj in self.client.cogs.items():
            if not extension_obj.cog_config.BOT_COGS:
                extension_dict = AppConfig.GUILD_CTX_EXTENSIONS_SAMPLE

                extension_dict["name"] = extension_obj.cog_config.NAME
                extension_dict["extension_config"] = extension_obj.default_guild_config
                guild_dict["extensions"]["enabled"].append(extension_dict)

        AppConfig.DB.add_new_guild(guild_dict)
