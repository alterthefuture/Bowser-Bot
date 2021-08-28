from discord.ext import commands
import discord
from discord import Webhook, AsyncWebhookAdapter
import aiohttp

class events(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.Cog.listener()
    async def on_command_error(self,ctx, error):
        if isinstance(error, commands.CommandNotFound):
            data = await self.client.config.get_by_id(ctx.guild.id)
            if not data or "prefix" not in data:
                prefix = ";"
            else:
                prefix = data["prefix"]

            await ctx.send(f"Command not found, use `{prefix}help` for a list of commands.")

        elif isinstance(error, commands.DisabledCommand):
            await ctx.send(f'The command **{ctx.command}** has been disabled.')
        elif isinstance(error,commands.CommandOnCooldown):
            await ctx.send(f"This command is on cooldown for **{error.retry_after:.2f}** seconds.")


def setup(client):
    client.add_cog(events(client))
