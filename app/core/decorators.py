import functools
import asyncio

from config import (
    DiscordPyConfig,
    AppConfig
)

class Decorators:

    @staticmethod
    def pass_guild_ctx(coro):

        @functools.wraps(coro)
        async def wrapped_coro(*args, **kwargs):


            loop = asyncio.get_event_loop()

            for arg in args:
                try:
                    guild_id = arg.guild.id
                except AttributeError:
                    pass

            guild_ctx_req = AppConfig.DB.get_guild_ctx_raw(guild_id)
            guild_ctx_resp = await loop.run_in_executor(None, guild_ctx_req.check_for_result)

            if guild_ctx_resp.command_state:
                guild_ctx = guild_ctx_resp.command_result[0]

                #args += (guild_ctx,)
                kwargs["guild_ctx"] = guild_ctx

                return await coro(*args, **kwargs)

            return await coro(*args, **kwargs)
        return wrapped_coro
