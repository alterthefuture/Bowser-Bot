from discord.ext import commands
import discord
from datetime import datetime
from datetime import timedelta 
import random
import asyncio

def convert(time):
  pos = ["S","M","D","s","m","d"]

  time_dict = {"S" : 1, "M" : 60, "D": 3600*24,"s" : 1, "m" : 60, "d": 3600*24}

  unit = time[-1]

  if unit not in pos:
    return -1
  try:
    val = int(time[:-1])
  except:
    return -2

  return val * time_dict[unit]

class server(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command(
        name="setprefix",
        description="Sets new prefix for guild.",
        usage='setprefix [prefix]',
        aliases=['prefix']
    )
    @commands.has_guild_permissions(manage_guild=True)
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def setprefix(self,ctx,new_prefix=None):
        if new_prefix == None:
            await ctx.send("Please specify a new prefix.")

        try:
            await self.client.config.upsert({"_id": ctx.guild.id, "prefix": new_prefix})
            await ctx.send(f"Successfully changed guild prefix to `{new_prefix}`")
        except:
            await ctx.send("Failed to change prefix, please try again later.")

    @commands.command(
        name="announce",
        description="Announces to mentioned channel.",
        usage='announce [message]',
        aliases=['anc']
    )
    @commands.bot_has_guild_permissions(manage_channels=True)
    @commands.has_guild_permissions(administrator=True)
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def announce(self,ctx,channel: discord.TextChannel, *, text: commands.clean_content()):
        try:
            await channel.send(text)
        except:
            await ctx.send("Couldn't send entered message.")

    @commands.command(
        name="giveaway",
        description="Creates a fully customizable giveaway.",
        usage="giveaway",
        aliases=['ga']
    )
    @commands.has_guild_permissions(manage_guild=True)
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def giveaway(self,ctx):
        questions = ["🎉 Alright! Let's setup your giveaway! First, what channel do you want the giveaway in?\n\n`Please mention the giveaway channel.`", "🎉 Sweet! Next, how long should the giveaway last?\n\n`Please enter the duration of the giveaway and include S at the end.`\n`Otherwise, enter a duration in minutes and include a M at the end, or days and include a D.`", "🎉 Neat! Finally, what do you want to give away?\n\n`Please enter the giveaway prize. NOTE: This will begin the giveaway.`"]

        answers = []

        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        for i in questions:
            await ctx.send(i)

            try:
                msg = await self.client.wait_for("message", check=check,timeout=15.0)
            except asyncio.TimeoutError:
                await ctx.send('💥 Uhhh... You took too long, Please try again later.')
                return
            else:
                answers.append(msg.content)

        try:
            c_id = int(answers[0][2:-1])
        except:
            await ctx.send(f"💥 Uhhh... You didn't mention a channel properly, Please mention the channel next time!")
            return

        channel = self.client.get_channel(c_id)

        time = convert(answers[1])
        if time == -1:
            await ctx.send(f"💥 Uhhh... That doesn't look like a valid unit, Please Use D, M, or S, next time!")
            return
        elif time == -2:
            await ctx.send(f"💥 Uhhh... That doesn't look like a number, Please enter a number next time!")
            return
        
        prize = answers[2]

        await ctx.send(f"🎉 Done! The giveaway for `{prize}` is starting in {channel.mention}!")

        if "d" in answers[1] or "D" in answers[1]:
            if "1" in answers[1]:
                new_date = datetime.now() + timedelta(days=1)
                layout = new_date.strftime("%B %d, %Y %I:%M %p")

                embed=discord.Embed(title=prize,description=f"React with 🎉 to enter!\nEnds: `in 1 Day ({layout})`\nHosted by: {ctx.author.mention}",color=0x86242a,timestamp=datetime.utcnow())
            else:
                if "d" in answers[1]:
                    times = answers[1].replace('d','')
                    prize_date = int(times)

                    new_date = datetime.now() + timedelta(days=prize_date)
                    layout = new_date.strftime("%B %d, %Y %I:%M %p")

                    embed=discord.Embed(title=prize,description=f"React with 🎉 to enter!\nEnds: `in {answers[1].replace('d','')} Days ({layout})`\nHosted by: {ctx.author.mention}",color=0x86242a,timestamp=datetime.utcnow())
                elif "D" in answers[1]:
                    times = answers[1].replace('D','')
                    prize_date = int(times)

                    new_date = datetime.now() + timedelta(days=prize_date)
                    layout = new_date.strftime("%B %d, %Y %I:%M %p")

                    embed=discord.Embed(title=prize,description=f"React with 🎉 to enter!\nEnds: `in {answers[1].replace('D','')} Days ({layout})`\nHosted by: {ctx.author.mention}",color=0x86242a,timestamp=datetime.utcnow())
        elif "s" in answers[1] or "S" in answers[1]:
            if "1" in answers[1]:
                new_date = datetime.now() + timedelta(seconds=1)
                layout = new_date.strftime("%B %d, %Y %I:%M %p")

                embed=discord.Embed(title=prize,description=f"React with 🎉 to enter!\nEnds: `in 1 second ({layout})`\nHosted by: {ctx.author.mention}",color=0x86242a,timestamp=datetime.utcnow())
            else:
                if "s" in answers[1]:
                    times = answers[1].replace('s','')
                    prize_date = int(times)

                    new_date = datetime.now() + timedelta(seconds=prize_date)
                    layout = new_date.strftime("%B %d, %Y %I:%M %p")

                    embed=discord.Embed(title=prize,description=f"React with 🎉 to enter!\nEnds: `in {answers[1].replace('s','')} Seconds ({layout})`\nHosted by: {ctx.author.mention}",color=0x86242a,timestamp=datetime.utcnow())
                elif "S" in answers[1]:
                    times = answers[1].replace('S','')
                    prize_date = int(times)

                    new_date = datetime.now() + timedelta(seconds=prize_date)
                    layout = new_date.strftime("%B %d, %Y %I:%M %p")

                    embed=discord.Embed(title=prize,description=f"React with 🎉 to enter!\nEnds: `in {answers[1].replace('S','')} Seconds ({layout})`\nHosted by: {ctx.author.mention}",color=0x86242a,timestamp=datetime.utcnow())
        elif "m" in answers[1] or "M" in answers[1]:
            if "1" in answers[1]:
                new_date = datetime.now() + timedelta(minutes=1)
                layout = new_date.strftime("%B %d, %Y %I:%M %p")

                embed=discord.Embed(title=prize,description=f"React with 🎉 to enter!\nEnds: `in 1 minute ({layout})`\nHosted by: {ctx.author.mention}",color=0x86242a,timestamp=datetime.utcnow())
            else:
                if "m" in answers[1]:
                    times = answers[1].replace('m','')
                    prize_date = int(times)

                    new_date = datetime.now() + timedelta(minutes=prize_date)
                    layout = new_date.strftime("%B %d, %Y %I:%M %p")

                    embed=discord.Embed(title=prize,description=f"React with 🎉 to enter!\nEnds: `in {answers[1].replace('m','')} Minutes ({layout})`\nHosted by: {ctx.author.mention}",color=0x86242a,timestamp=datetime.utcnow())
                elif "M" in answers[1]:
                    times = answers[1].replace('M','')
                    prize_date = int(times)

                    new_date = datetime.now() + timedelta(minutes=prize_date)
                    layout = new_date.strftime("%B %d, %Y %I:%M %p")

                    embed=discord.Embed(title=prize,description=f"React with 🎉 to enter!\nEnds: `in {answers[1].replace('M','')} Seconds ({layout})`\nHosted by: {ctx.author.mention}",color=0x86242a,timestamp=datetime.utcnow())
        embed.set_footer(text="Make sure to react!")

        my_msg = await channel.send("🎉 **GIVEAWAY** 🎉",embed = embed)

        await my_msg.add_reaction("🎉")

        await asyncio.sleep(time)

        new_msg = await channel.fetch_message(my_msg.id)

        users = await new_msg.reactions[0].users().flatten()
        users.pop(users.index(self.client.user))

        winner = random.choice(users)

        await channel.send(f"Congratulations {winner.mention}! You won the **{prize}**!")


    @commands.command(
        name="reroll",
        description="Rerolls giveaway winner.",
        usage="reroll [channel] [giveaway_messageID]",
        aliases=['rr']
    )
    @commands.has_guild_permissions(manage_guild=True)
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def reroll(self,ctx, channel : discord.TextChannel, id_ : int):
        try:
            new_msg = await channel.fetch_message(id_)
        except:
            await ctx.send("Giveaway message not found.")
        users = await new_msg.reactions[0].users().flatten()
        users.pop(users.index(self.client.user))

        winner = random.choice(users)

        await channel.send(f"🎉 The new winner is {winner.mention}! Congratulations!")
    
    @reroll.error
    async def reroll_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'You are missing the permission: **{"".join(error.missing_perms)}**')
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please **mention** a channel')

    @giveaway.error
    async def giveaway_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'You are missing the permission: **{"".join(error.missing_perms)}**')
        

    @announce.error
    async def announce_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'You are missing the permission: **{"".join(error.missing_perms)}**')
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please **mention** a channel')

    @setprefix.error
    async def setprefix_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
            await ctx.send(f'You are missing the permission: **{"".join(error.missing_perms)}**')


def setup(client):
    client.add_cog(server(client))
