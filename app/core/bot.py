from config import (
    DiscordPyConfig,
    AppConfig
)


class BotUtils:

    @staticmethod
    def get_prefix(client, message):
        guild_ctx_req = AppConfig.DB.get_guild_prefix(message.guild.id)
        guild_ctx_resp = guild_ctx_req.check_for_result()
        if guild_ctx_resp.command_state:
            prefix = guild_ctx_resp.command_result[0]["prefix"]
            if prefix is not None:
                return prefix
        return DiscordPyConfig.BASE_COMMANDS_PREFIX
