from discord import embeds
from discord.ext import commands
import discord
import datetime
import platform

class information(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command(
        name="botinfo",
        description="Displays information about the bot.",
        usage="botinfo",
        aliases=['bi']
    )
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def botinfo(self,ctx):
        dpyVersion = discord.__version__
        pythonVersion = platform.python_version() 

        embed=discord.Embed(title="Bowser Information",description=f"Bowser is a **multipurpose** bot that is meant to make your server even more fun. Ranging from **game** commands, **fun** commands, and **more**!\n\n[Server](https://discord.gg/rftvVFjUWW) • [Invite](https://discord.com/api/oauth2/authorize?client_id=870501241980067861&permissions=8&scope=bot) • [Upvote](https://discordbotlist.com/bots/bowser/upvote)\n\n**Discord**\nServers: **{len(self.client.guilds)}**\nMembers: **{len(self.client.users)}**\nPing: **{round(self.client.latency * 1000)}**\n\n**Information**\nCreation Date: **8/1/21**\nDeveloper: **ritz#88888**\nLanguage: **Python {pythonVersion}**\nDiscord.py Version: **{dpyVersion}**\n\n**Cooldowns**\nInformation Commands: **5** seconds\nModeration Commands: **25** seconds\nGame Commands: **10** seconds\nServer Commands **15** seconds\nFun Commands: **10** seconds\n\nWhy is there **cooldowns**? Cooldowns are used so the bot doesn't get **ratelimited**. If the bot gets ratelimited, it will be prevented from running.",timestamp=datetime.datetime.utcnow(),color=0x86242a)
        embed.set_footer(text=f"Requested by {ctx.author}",icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=self.client.user.avatar_url)

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(information(client))
