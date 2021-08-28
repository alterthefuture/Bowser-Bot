from discord.ext import commands
import discord
import datetime

class help(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command()
    async def help(self,ctx,category=None):
        data = await self.client.config.get_by_id(ctx.guild.id)
        if not data or "prefix" not in data:
            prefix = ";"
        else:
            prefix = data["prefix"]

        if category == None:
            embed=discord.Embed(title="Bowser Help Menu",description=f"Below are all the commands type `{prefix}help [catagory]` to get started.\n\n[Server](https://discord.gg/rftvVFjUWW) • [Invite](https://discord.com/api/oauth2/authorize?client_id=870501241980067861&permissions=8&scope=bot) • [Upvote](https://discordbotlist.com/bots/bowser/upvote)",color=0x86242a,timestamp=datetime.datetime.utcnow())
            embed.add_field(name="Games",value="Displays game related commands.",inline=False)
            embed.add_field(name="Music",value="Displays music related commands.",inline=False)
            embed.add_field(name="Server",value="Displays server related commands.",inline=False)
            embed.add_field(name="Fun",value="Displays fun related commands.",inline=False)
            embed.add_field(name="botinfo",value="Displays information about the bot.",inline=False)
            embed.set_footer(text=f"Requested by {ctx.author}",icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url=self.client.user.avatar_url)

            await ctx.send(embed=embed)

        elif category == "server" or category == "Server":
            cog = self.client.get_cog('server')
            commands = cog.get_commands()
            embed = discord.Embed(title="Bowser Server Commands",color=0x86242a,description='Commands with () are optional || Commands with [] are required.',timestamp=datetime.datetime.utcnow())
            embed.set_footer(text=f"Requested by {ctx.author}",icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url=self.client.user.avatar_url)
            for command in commands:
                if command.aliases != []:
                    alias_list = command.aliases
                    temp_alias_list = []
                    for i in range(len(alias_list)):
                        temp_alias_list.append(f'{prefix}'+alias_list[i])
                    embed.add_field(
                        name=command.qualified_name,
                        value=f'Description: {command.description}\nUsage: `{prefix}{command.usage}`\nAliases: `{", ".join(temp_alias_list)}`',
                        inline=False
                    )
                else:
                    embed.add_field(name=command.qualified_name,value=f'Description: {command.description}\nUsage: `{prefix}{command.usage}`',inline=False)

            await ctx.send(embed=embed)
          
        elif category == "music" or category == "Music":
            cog = self.client.get_cog('music')
            commands = cog.get_commands()
            embed = discord.Embed(title="Bowser Music Commands",color=0x86242a,description='Commands with () are optional || Commands with [] are required.',timestamp=datetime.datetime.utcnow())
            embed.set_footer(text=f"Requested by {ctx.author}",icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url=self.client.user.avatar_url)
            for command in commands:
                if command.aliases != []:
                    alias_list = command.aliases
                    temp_alias_list = []
                    for i in range(len(alias_list)):
                        temp_alias_list.append(f'{prefix}'+alias_list[i])
                    embed.add_field(
                        name=command.qualified_name,
                        value=f'Description: {command.description}\nUsage: `{prefix}{command.usage}`\nAliases: `{", ".join(temp_alias_list)}`',
                        inline=False
                    )
                else:
                    embed.add_field(name=command.qualified_name,value=f'Description: {command.description}\nUsage: `{prefix}{command.usage}`',inline=False)

            await ctx.send(embed=embed)

        elif category == "fun" or category == "Fun":
            cog = self.client.get_cog('fun')
            commands = cog.get_commands()
            embed = discord.Embed(title="Bowser Fun Commands",color=0x86242a,description='Commands with () are optional || Commands with [] are required.',timestamp=datetime.datetime.utcnow())
            embed.set_footer(text=f"Requested by {ctx.author}",icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url=self.client.user.avatar_url)
            for command in commands:
                if command.aliases != []:
                    alias_list = command.aliases
                    temp_alias_list = []
                    for i in range(len(alias_list)):
                        temp_alias_list.append(f'{prefix}'+alias_list[i])
                    embed.add_field(
                        name=command.qualified_name,
                        value=f'Description: {command.description}\nUsage: `{prefix}{command.usage}`\nAliases: `{", ".join(temp_alias_list)}`',
                        inline=False
                    )
                else:
                    embed.add_field(name=command.qualified_name,value=f'Description: {command.description}\nUsage: `{prefix}{command.usage}`',inline=False)

            await ctx.send(embed=embed)

        elif category == "games" or category == "Games":
            cog = self.client.get_cog('games')
            commands = cog.get_commands()
            embed = discord.Embed(title="Bowser Game Commands",color=0x86242a,description='Commands with () are optional || Commands with [] are required.',timestamp=datetime.datetime.utcnow())
            embed.set_footer(text=f"Requested by {ctx.author}",icon_url=ctx.author.avatar_url)
            embed.set_thumbnail(url=self.client.user.avatar_url)
            for command in commands:
                if command.aliases != []:
                    alias_list = command.aliases
                    temp_alias_list = []
                    for i in range(len(alias_list)):
                        temp_alias_list.append(f'{prefix}'+alias_list[i])
                    embed.add_field(
                        name=command.qualified_name,
                        value=f'Description: {command.description}\nUsage: `{prefix}{command.usage}`\nAliases: `{", ".join(temp_alias_list)}`',
                        inline=False
                    )
                else:
                    embed.add_field(name=command.qualified_name,value=f'Description: {command.description}\nUsage: `{prefix}{command.usage}`',inline=False)

            await ctx.send(embed=embed)

        elif category == "owner" or category == "Owner":
            if ctx.author.id == 798325945463078952:
                cog = self.client.get_cog('owner')
                commands = cog.get_commands()
                embed = discord.Embed(title="Bowser Owner Commands",color=0x86242a,description='Commands with () are optional || Commands with [] are required.',timestamp=datetime.datetime.utcnow())
                
                embed.set_footer(text=f"Requested by {ctx.author}",icon_url=ctx.author.avatar_url)
                embed.set_thumbnail(url=self.client.user.avatar_url)
                for command in commands:
                    if command.aliases != []:
                        alias_list = command.aliases
                        temp_alias_list = []
                        for i in range(len(alias_list)):
                            temp_alias_list.append(f'{prefix}'+alias_list[i])
                        embed.add_field(
                            name=command.qualified_name,
                            value=f'Description: {command.description}\nUsage: `{prefix}{command.usage}`\nAliases: `{", ".join(temp_alias_list)}`',
                            inline=False
                        )
                    else:
                        embed.add_field(name=command.qualified_name,value=f'Description: {command.description}\nUsage: `{prefix}{command.usage}`',inline=False)

                await ctx.send(embed=embed)
            else:
                pass

def setup(client):
    client.add_cog(help(client))
