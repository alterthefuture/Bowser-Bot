from discord.ext import commands
import datetime
import discord

class owner(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command(
        name="blacklist",
        description="Blacklist user from bot.",
        usage='blacklist [id]'
    )
    @commands.is_owner()
    async def blacklist(self,ctx,id: int):
        if id == None:
            await ctx.send("Please specify a ID to blacklist.")

        try:
            await self.client.config.upsert({"_id": id})
            await ctx.send(f"Successfully blacklisted the ID **{id}**")
        except:
            await ctx.send("Failed to blacklist ID, please try again later.")

    @commands.command(
        name="unblacklist",
        description="Unblacklist user from bot.",
        usage='unblacklist [id]'
    )
    @commands.is_owner()
    async def unblacklist(self,ctx,id: int):
        if id == None:
            await ctx.send("Please specify a ID to blacklist.")

        try:
            await self.client.config.unset({"_id": id})
            await ctx.send(f"Successfully unblacklisted the ID **{id}**")
        except:
            await ctx.send("Failed to unblacklist ID, please try again later.")

    @commands.command(
        name="toggle",
        description="Enable or disables a command.",
        usage='toggle [command]'
    )
    @commands.is_owner()
    async def toggle(self,ctx,*,command):
        command = self.client.get_command(command)

        if command is None:
            await  ctx.send("This command is not found but you created the bot smh.")
        
        elif ctx.command == command:
            await ctx.send("Stupid owner you can't disable this command.")
        
        else:
            command.enabled = not command.enabled
            ternary = "enabled" if command.enabled else "disabled"
            await ctx.send(f"**{command.qualified_name}** has been {ternary}.")

    @commands.command(
        name="load",
        description="Loads a specific cog.",
        usage='load [cog]'
    )
    @commands.is_owner()
    async def load(self,ctx,extension):
        try:
            self.client.load_extension(f'cogs.{extension}')
            await ctx.send(f"Successfully loaded the cog **{extension}**")
        except:
            await ctx.send(f"Failed to load cog **{extension}**")

    @commands.command(
        name="unload",
        description="Unloads a specific cog.",
        usage='unload [cog]'
    )
    @commands.is_owner()
    async def unload(self,ctx,extension):
        try:
            self.client.unload_extension(f'cogs.{extension}')
            await ctx.send(f"Successfully unloaded the cog **{extension}**")
        except:
            await ctx.send(f"Failed to unload cog **{extension}**")

    @commands.command(
        name="reload",
        description="Reloads a specific cog.",
        usage='reload [cog]'
    )
    @commands.is_owner()
    async def reload(self,ctx,extension):
        try:
            self.client.reload_extension(f'cogs.{extension}')
            await ctx.send(f"Successfully reloaded the cog **{extension}**")
        except:
            await ctx.send(f"Failed to reload cog **{extension}**")

    @commands.command(
      name="servers",
      description="Displays all the servers the bots in.",
      usage='servers'
    )
    @commands.is_owner()
    async def servers(self,ctx):
        embed=discord.Embed(title="Bowser Servers",descripion="Below is a list of servers Bowser is in.",color=0x86242a,timestamp=datetime.datetime.utcnow())
        embed.set_footer(text=f"Requested by {ctx.author}",icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=self.client.user.avatar_url)
        activeservers = self.client.guilds
        for guild in activeservers:
          members = len(guild.members)
          embed.add_field(name=f"{guild.name}",value=f"{members} Members.")
        await ctx.send(embed=embed)

    @reload.error    
    async def reload_error(self,ctx, error):
        if isinstance(error, commands.NotOwner):
            await ctx.send("You must be the **owner** of the bot to run this command.")

    @load.error    
    async def load_error(self,ctx, error):
        if isinstance(error, commands.NotOwner):
            await ctx.send("You must be the **owner** of the bot to run this command.")

    @unload.error    
    async def unload_error(self,ctx, error):
        if isinstance(error, commands.NotOwner):
            await ctx.send("You must be the **owner** of the bot to run this command.")

    @toggle.error    
    async def toggle_error(self,ctx, error):
        if isinstance(error, commands.NotOwner):
            await ctx.send("You must be the **owner** of the bot to run this command.")

    @blacklist.error    
    async def blacklist_error(self,ctx, error):
        if isinstance(error, commands.NotOwner):
            await ctx.send("You must be the **owner** of the bot to run this command.")

def setup(client):
    client.add_cog(owner(client))