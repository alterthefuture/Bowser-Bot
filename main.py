import os
import discord
from pathlib import Path
import motor.motor_asyncio
from discord.ext import commands
import json
import asyncio

import util.json
from util.mongo import Document

cwd = Path(__file__).parents[0]
cwd = str(cwd)

async def get_prefix(client,message):
    if not message.guild:
        return commands.when_mentioned_or(";")(client,message)

    try:
        data = await client.config.find(message.guild.id)

        if not data or "prefix" not in data:
            return commands.when_mentioned_or(";")(client,message)
        return commands.when_mentioned_or(data['prefix'])(client,message)
    except:
        return commands.when_mentioned_or(";")(client,message)

intents=discord.Intents.all()
secret_file = json.load(open(cwd+'/secrets.json'))
client = commands.Bot(command_prefix=get_prefix,intents=intents,case_insensitive=True,owner_id=798325945463078952)
client.remove_command(name="help")

client.config_token = secret_file['token']
client.connection_url = secret_file['mongo']

@client.event
async def on_ready():
    print("Bowser Bot is online.")

    client.mongo = motor.motor_asyncio.AsyncIOMotorClient(str(client.connection_url))
    client.db = client.mongo['ritz']

    client.config = Document(client.db,'config')

    while True:
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name=f"{len(client.guilds)} Servers {len(client.users)} Members!"))
        await asyncio.sleep(4)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name=f";help"))
        await asyncio.sleep(4)

@client.event
async def on_message(message):
    if message.author.bot:
        return

    data = await client.config.get_by_id(message.author.id)

    if not data:
        pass
    else:
        return

    if message.content.startswith(f"<@!{client.user.id}>") and len(message.content) == len(f"<@!{client.user.id}>"):
        data = await client.config.get_by_id(message.guild.id)
        if not data or "prefix" not in data:
            prefix = ";"
        else:
            prefix = data["prefix"]
        await message.channel.send(f"My prefix for this server is: `{prefix}`")

    await client.process_commands(message)

async def setup():
  await client.wait_until_ready()
  for filename in os.listdir('./cogs'):
      if filename.endswith('.py'):
          client.load_extension(f'cogs.{filename[:-3]}')

client.loop.create_task(setup())
client.run(client.config_token)
