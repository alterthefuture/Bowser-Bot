from discord.ext import commands
import discord
import random
import requests
import datetime

class fun(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command(
        name="gayrate",
        description="Gayrates mentioned user.",
        usage='gayrate (@user)',
        aliases=['gr']
    )
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def gayrate(self, ctx,member: discord.Member):
        percentage = random.randint(1,100)
        await ctx.send(f"{member.mention} is **{percentage}%** gay.")

    @commands.command(
        name="simprate",
        description="Simprates mentioned user.",
        usage='simprate (@user)',
        aliases=['sr']
    )
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def simprate(self, ctx,member: discord.Member):
        percentage = random.randint(1,100)
        await ctx.send(f"{member.mention} is **{percentage}%** simp.")

    @commands.command(
        name="hotrate",
        description="Hotrate mentioned user.",
        usage='hotrate (@user)',
        aliases=['hr']
    )
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def hotrate(self, ctx,member: discord.Member):
        percentage = random.randint(1,100)
        await ctx.send(f"{member.mention} is **{percentage}%** hot.")

    @commands.command(
        name="compatible",
        description="Checks compatibilty between you and a user.",
        usage='compatible [@user]',
        aliases=['cmp']
    )
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def compatible(self,ctx,member: discord.Member):
        percentage = random.randint(1,100)
        await ctx.send(f"*You and {member.mention} are {percentage}% compatible.*")

    @commands.command(
        name="cat",
        description="Gets a random picture of a cat.",
        usage="cat"
    )
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def cat(self,ctx):
        r = requests.get("https://some-random-api.ml/img/cat").json()
        embed = discord.Embed(color=0x86242a,timestamp=datetime.datetime.utcnow()) 
        embed.set_image(url=str(r["link"]))
        embed.set_footer(text=f"requested by {ctx.author}",icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(
        name="dog",
        description="Gets a random picture of a dog.",
        usage="dog"
    )
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def dog(self,ctx):
        r = requests.get("https://some-random-api.ml/img/dog").json()
        embed = discord.Embed(color=0x86242a,timestamp=datetime.datetime.utcnow()) 
        embed.set_image(url=str(r["link"]))
        embed.set_footer(text=f"requested by {ctx.author}",icon_url=ctx.author.avatar_url)
        await ctx.send(embed=embed)

    @commands.command(
        name="quote",
        description="Quotes a users message.",
        usage='quote [message_ID]',
        aliases=['qt']
    )
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def quote(self,ctx,id: int):
        try:
            message = await ctx.channel.fetch_message(id)
        except discord.errors.NotFound:
            await ctx.send("Message not found.")
            return

        await ctx.send(f'"{message.content}" - **{message.author}**')

    @commands.command(
        name="clapify",
        description="Clapifys entered message.",
        usage='clapify ["message"]',
        aliases=['clap']
    )
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def clapify(self,ctx, text: commands.clean_content()):
        await ctx.send(text.replace(" ", ":clap:")[:2000])

    @commands.command(
        name="say",
        description="Repeats entered message.",
        usage='say ["message"]'
    )
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def say(self, ctx, text: commands.clean_content()):
        await ctx.send(text[:2000])

    @say.error
    async def say_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Please enter a **message ID** for me to quote.")

    @say.error
    async def say_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Please enter a **message** for me to clapify.")

    @say.error
    async def say_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Please enter a **message** for me to repeat.")

    @compatible.error
    async def compatible_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"Please **mention** a user.")

    @hotrate.error
    async def hotrate_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            percentage = random.randint(1,100)
            await ctx.send(f"You are **{percentage}%** hot.")

    @gayrate.error
    async def gayrate_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            percentage = random.randint(1,100)
            await ctx.send(f"You are **{percentage}%** gay.")

    @simprate.error
    async def simprate_error(self, ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            percentage = random.randint(1,100)
            await ctx.send(f"You are **{percentage}%** simp.")

def setup(client):
    client.add_cog(fun(client))
