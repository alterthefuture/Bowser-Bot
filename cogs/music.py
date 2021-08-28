from discord.embeds import Embed
from discord.ext import commands
import youtube_dl
import asyncio
import pafy
import discord
import datetime

class music(commands.Cog):
    def __init__(self,client):
        self.client = client
        self.song_queue = {}

        self.setup()

    def setup(self):
        for guild in self.client.guilds:
            self.song_queue[guild.id] = []

    async def check_queue(self, ctx):
        if len(self.song_queue[ctx.guild.id]) > 0:
            ctx.voice_client.stop()
            await self.play_song(ctx,self.song_queue[ctx.guild.id][0])
            self.song_queue[ctx.guild.id].pop(0)

    async def search_song(self, amount, song, get_url=False):
        info = await self.client.loop.run_in_executor(None, lambda: youtube_dl.YoutubeDL({"format" : "bestaudio", "quiet": True}).extract_info(f'ytsearch{amount}:{song}', download=False, ie_key="YoutubeSearch"))
        if len(info["entries"]) == 0: return None

        return [entry["webpage_url"] for entry in info ["entries"]] if get_url else info

    async def play_song(self, ctx, song):
        url = pafy.new(song).getbestaudio().url
        ctx.voice_client.play(discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(url)), after=lambda error: self.client.loop.create_task(self.check_queue(ctx)))
        ctx.voice_client.source.volume = 0.5

    @commands.command(
        name="join",
        description='Joins voice channel.',
        usage="join",
        aliases=['j']
    )
    async def join(self,ctx):
        if ctx.author.voice is None:
            await ctx.send("You must be connected to a voice channel to use this command.")

        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
            await ctx.send(f"Successfully Connected to **{voice_channel}**.")
        else:
            if len(ctx.voice_client.channel.members) == 1:
                ctx.voice_client.stop()
                await ctx.voice_client.move_to(voice_channel)
                await ctx.send(f"Successfully Connected to **{voice_channel}**.")
            else:
                await ctx.send("Someone else is already listening to music in different channel.")

    @commands.command(
        name="disconnect",
        description='Leaves voice channel.',
        usage="disconnect",
        aliases=['dc']
        )
    async def disconnect(self,ctx):
        voice = ctx.voice_client

        if ctx.author.voice is None:
            await ctx.send("You must be connected to a voice channel to use this command.")
        elif ctx.voice_client is None:
            await ctx.send("I'm not in a voice channel.")
        else:
            if ctx.author.voice.channel == voice.channel:
                ctx.voice_client.stop()
                await ctx.voice_client.disconnect()
                await ctx.send(f"Successfully Disconnected from **{voice.channel}**.")
            else:
                if len(ctx.voice_client.channel.members) == 1:
                    ctx.voice_client.stop()
                    await ctx.voice_client.disconnect()
                    await ctx.send(f"Successfully Disconnected from **{voice.channel}**.")
                else:
                    await ctx.send("Someone else is already listening to music in different channel.")

    @commands.command(
        name="play",
        description='Plays song from url into voice channel.',
        usage='play [url/song_name]',
        aliases=['p']
        )
    async def play(self,ctx,*,song=None):
        voice = ctx.voice_client

        if song is None:
            await ctx.send("Please include a song to play.")

        if ctx.author.voice is None:
            await ctx.send("You must be connected to a voice channel to use this command.")

        if not ("youtube.com/watch?" in song or "https://youtu.be/" in song):
            result = await self.search_song(1, song, get_url=True)

            if result is None:
                return await ctx.send("Couldn't find entered song.")

            song = result[0]

        voice_channel = ctx.author.voice.channel
        if ctx.voice_client is None:
            await voice_channel.connect()
            await self.play_song(ctx, song)
            await ctx.send(f"Now playing {song}")
        else:
            if ctx.voice_client.source is not None:
                if ctx.author.voice.channel == voice.channel:
                    queue_len = len(self.song_queue[ctx.guild.id])

                    if queue_len < 10:
                        self.song_queue[ctx.guild.id].append(song)
                        return await ctx.send("Song has been added to queue.")
                    else:
                        return await ctx.send("I can only queue up to 10 songs, please wait for the current song to finish.")
                else:
                    if len(ctx.voice_client.channel.members) == 1:
                        ctx.voice_client.stop()
                        await ctx.voice_client.move_to(voice_channel)
                        await self.play_song(ctx, song)
                        await ctx.send(f"Now playing {song}")
                    else:
                        return await ctx.send("Someone else is already listening to music in different channel.")

            if ctx.author.voice.channel == voice.channel:
                await self.play_song(ctx, song)
                await ctx.send(f"Now playing {song}")
            else:
                if len(ctx.voice_client.channel.members) == 1:
                    ctx.voice_client.stop()
                    await ctx.voice_client.move_to(voice_channel)
                    await self.play_song(ctx, song)
                    await ctx.send(f"Now playing {song}")
                else:
                    await ctx.send("Someone else is already listening to music in different channel.")

    @commands.command(
        name="queue",
        description="Shows all songs in queue.",
        usage='queue',
        aliases=['q']
    )
    async def queue(self,ctx):
        if len(self.song_queue[ctx.guild.id]) == 0:
            return await ctx.send("There is currently so songs in queue.")

        embed=discord.Embed(title="Song Queue",description="",timestamp=datetime.datetime.utcnow(),color=0x86242a)
        embed.set_footer(text=f"Requested by {ctx.author}",icon_url=ctx.author.avatar_url)
        embed.set_thumbnail(url=self.client.user.avatar_url)
        i = 1
        for url in self.song_queue[ctx.guild.id]:
            embed.description += f"{i}) {url}\n"

            i += 1

        await ctx.send(embed=embed)

    @commands.command(
        name="skip",
        description="Skips current song.",
        usage='skip'
    )
    async def skip(self,ctx):
        voice = ctx.voice_client

        if ctx.author.voice is None:
            await ctx.send("You must be connected to a voice channel to use this command.")
        elif ctx.voice_client is None:
            await ctx.send("I'm not in a voice channel.")
        else:
            if ctx.author.voice.channel == voice.channel:
                poll_message = await ctx.send("Skip current song? 80% of the voice channel must vote to skip. Voting ends in 15 seconds.")

                poll_id = poll_message.id

                await poll_message.add_reaction(u"\u2705")
                await poll_message.add_reaction(u"\U0001F6AB")

                await asyncio.sleep(15)

                poll_msg = await ctx.channel.fetch_message(poll_id)

                votes = {u"\u2705": 0, u"\U0001F6AB": 0}
                reacted = []

                for reaction in poll_msg.reactions:
                    if reaction.emoji in [u"\u2705", u"\U0001F6AB"]:
                        async for user in reaction.users():
                            if user.voice.channel.id == ctx.voice_client.channel.id and user.id not in reacted and not user.bot:
                                votes[reaction.emoji] += 1

                                reacted.append(user.id)

                skip = False

                if votes[u"\u2705"] > 0:
                    if votes[u"\U0001F6AB"] == 0 or votes [u"\u2705"] / (votes[u"\u2705"]) > 0.79:
                        skip = True
                        await ctx.send("Voted song has been skipped.")

                if not skip:
                    await ctx.send("Voted song has not been skipped.")

                await poll_message.clear_reactions()

                if skip:
                    ctx.voice_client.stop()
                    await self.check_queue(ctx)
            else:
                await ctx.send("Someone else is already listening to music in different channel.")

    @commands.command(
        name="pause",
        description='Pauses current song.',
        usage="pause"
    )
    async def pause(self,ctx):
        voice = ctx.voice_client

        if ctx.author.voice is None:
            await ctx.send("You must be connected to a voice channel to use this command.")
        elif ctx.voice_client is None:
            await ctx.send("I'm not in a voice channel.")
        else:
            if ctx.author.voice.channel == voice.channel:
                if ctx.voice_client.is_playing():
                    ctx.voice_client.pause()
                    await ctx.send("Successfully Paused the song.")
                elif ctx.voice_client.is_paused():
                    await ctx.send("I'm already paused.")
                else:
                    await ctx.send("Nothing is playing.")
            else:
                await ctx.send("Someone else is already listening to music in different channel.")

    @commands.command(
        name="resume",
        description='Resumes current song.',
        usage="resume"
    )
    async def resume(self,ctx):
        voice = ctx.voice_client

        if ctx.author.voice is None:
            await ctx.send("You must be connected to a voice channel to use this command.")
        elif ctx.voice_client is None:
            await ctx.send("I'm not in a voice channel.")
        else:
            if ctx.author.voice.channel == voice.channel:
                if ctx.voice_client.is_paused():
                    ctx.voice_client.resume()
                    await ctx.send("Successfully Resumed the song.")
                elif ctx.voice_client.is_playing():
                    await ctx.send("Music is already playing.")
                else:
                    await ctx.send("Nothing is playing.")
            else:
                await ctx.send("Someone else is already listening to music in different channel.")

    @commands.command(
        name="stop",
        description='Stops current song.',
        usage="stop"
    )
    async def stop(self,ctx):
        voice = ctx.voice_client

        if ctx.author.voice is None:
            await ctx.send("You must be connected to a voice channel to use this command.")
        elif ctx.voice_client is None:
            await ctx.send("I'm not in a voice channel.")
        else:
            if ctx.author.voice.channel == voice.channel:
                if ctx.voice_client.is_playing() or ctx.voice_client.is_paused():
                    ctx.voice_client.stop()
                    await ctx.send("Successfully Stopped the song.")
                else:
                    await ctx.send("Nothing is playing.")
            else:
                await ctx.send("Someone else is already listening to music in different channel.")
        
def setup(client):
    client.add_cog(music(client))
