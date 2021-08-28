from discord.ext import commands
import random
import asyncio

class games(commands.Cog):
    def __init__(self,client):
        self.client = client

    @commands.command(
        name="rockpaperscissors",
        description="Play a game of rock paper sciscors with the bot.",
        usage='rockpaperscissors',
        aliases=['rps']
    )
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def rockpaperscissors(self,ctx):
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        options = ['rock','paper','scissors']
        choice = random.choice(options)

        try:
            await ctx.send("**RPS** Game! Your options are: **Rock**, **Paper**, or **Scissors**, Please type your choice.")

            message = await self.client.wait_for('message',check=check,timeout=15)

            if message.content.lower() == "rock" or message.content.lower() == "rock":
                if choice == "paper":
                    await ctx.send("I chose **paper**, you chose **rock**. You lose, Better luck next time!")
                elif choice == "rock":
                    await ctx.send("I chose **rock**, you chose **rock**. Tie game, Nice try")
                elif choice == "scissors":
                    await ctx.send("I chose **scissors**, you chose **rock**. You win, Congrats!")
            elif message.content.lower() == "paper" or message.content.lower() == "Paper":
                if choice == "paper":
                    await ctx.send("I chose **paper**, you chose **paper**. Tie game, Nice try")
                elif choice == "rock":
                    await ctx.send("I chose **rock**, you chose **paper**. You win, Congrats!")
                elif choice == "scissors":
                    await ctx.send("I chose **scissors**, you chose **paper**. You lose, Better luck next time!")
            elif message.content.lower() == "scissors" or message.content.lower() ==  "Scissors":
                if choice == "paper":
                    await ctx.send("I chose **paper**, you chose **scissors**. You win, Congrats!")
                elif choice == "rock":
                    await ctx.send("I chose **rock**, you chose **scissors**. You lose, Better luck next time!")
                elif choice == "scissors":
                    await ctx.send("I chose **scissors**, you chose **scissors**. Tie game, Well played!")
            else:
                await ctx.send("**RPS** Game! Please type a **valid** choice.")

        except asyncio.TimeoutError:
            await ctx.send(f"**RPS** Game! You took too long, Please try again later.")

    @commands.command(
        name="coinflip",
        description="Play a game of heads or tails with the bot.",
        usage='coinflip',
        aliases=['cf']
    )
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def coinflip(self,ctx):
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        options = ['heads','tails']
        choice = random.choice(options)

        try:
            await ctx.send("**CF** Game! Your options are: **Heads** or **Tails**, Please type your choice.")

            message = await self.client.wait_for('message',check=check,timeout=15)

            if message.content.lower() == "heads" or message.content.lower() == "Heads":
                if choice == "heads":
                    await ctx.send(f"You chose **heads**, I get **tails**. The coin landed on **{choice}**. You won, Congrats! 🎉")
                elif choice == "tails":
                    await ctx.send(f"You chose **heads**, I get **tails**. The coin landed on **{choice}**. You lose, Better luck next time!")
            elif message.content.lower() == "tails" or message.content.lower() == "Tails":
                if choice == "tails":
                    await ctx.send(f"You chose **tails**, I get **heads**. The coin landed on **{choice}**. You won, Congrats! 🎉")
                elif choice == "heads":
                    await ctx.send(f"You chose **tails**, I get **heads**. The coin landed on **{choice}**. You lose, Better luck next time!")
            else:
                await ctx.send("**CF** Game! Please type a **valid** choice.")

        except asyncio.TimeoutError:
            await ctx.send("**CF** Game! You took too long, please try again later.")

    @commands.command(
        name="blackjack",
        description="Play a game of blackjack with the bot.",
        usage='blackjack',
        aliases=['bj']
    )
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def blackjack(self,ctx):
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel

        player_card1 = random.randint(1,11)
        player_card2 = random.randint(1,11)

        dealer_card1 = random.randint(1,11)
        dealer_card2 = random.randint(1,11)
        dealer_card3 = random.randint(1,11)

        player_total = player_card1 + player_card2
        dealer_total = dealer_card1 + dealer_card2 + dealer_card3

        if player_total < 21:
            try:
                await ctx.send(f"**BJ** Game! Your cards are **{player_card1}** and **{player_card2}**, Your total is **{player_total}**. Would you like to **Hit**, **Stand**, or **Fold**?")

                message = await self.client.wait_for('message',check=check,timeout=15)

                if message.content.lower() == "fold" or message.content.lower() == "Fold":
                    await ctx.send("**BJ** Game! You folded, Better luck next time!")
                elif message.content.lower() == "stand" or message.content.lower() == "Stand":
                    if dealer_total < 21:
                        if dealer_total > player_total:
                            await ctx.send(f"**BJ** Game! Dealers cards are **{dealer_card1}**, **{dealer_card2}**, and **{dealer_card3}**, Total is **{dealer_total}**. Your total is **{player_total}**. You lose, Better luck next time.")
                        elif dealer_total < player_total:
                            await ctx.send(f"**BJ** Game! Dealers cards are **{dealer_card1}**, **{dealer_card2}**, and **{dealer_card3}**, Total is **{dealer_total}**. Your total is **{player_total}**. You won, Congrats! 🎉")
                        elif dealer_total == player_total:
                            await ctx.send(f"**BJ** Game! Dealers cards are **{dealer_card1}**, **{dealer_card2}**, and **{dealer_card3}**, Total is **{dealer_total}**. Your total is **{player_total}**. Tie game, Well played!")
                    elif dealer_total == 21:
                        await ctx.send(f"**BJ** Game! Dealers cards are **{dealer_card1}**, **{dealer_card2}**, and **{dealer_card3}**, Total is **{dealer_total}**. Your total is **{player_total}**. You lose, Better luck next time.")
                    elif dealer_total > 21:
                        await ctx.send(f"**BJ** Game! Dealers cards are **{dealer_card1}**, **{dealer_card2}**, and **{dealer_card3}**, Total is **{dealer_total}**. Your total is **{player_total}**. You won, Congrats! 🎉")
                elif message.content.lower() == "hit" or message.content.lower() == "Hit":
                    player_card3 = random.randint(1,11)

                    player_total = player_total + player_card3

                    if player_total < 21:
                        if player_total > dealer_total:
                            await ctx.send(f"**BJ** Game! Your cards are **{player_card1}**, **{player_card2}**, and **{player_card3}**, Your total is **{player_total}**. Dealers total is **{dealer_total}**. You won, Congrats! 🎉")
                        elif player_total < dealer_total:
                            await ctx.send(f"**BJ** Game! Your cards are **{player_card1}**, **{player_card2}**, and **{player_card3}**, Your total is **{player_total}**. Dealers total is **{dealer_total}**. You lose, Better luck next time!")
                    elif player_total == 21:
                        await ctx.send(f"**BJ** Game! Your cards are **{player_card1}**, **{player_card2}**, and **{player_card3}**, Your total is **{player_total}**. Dealers total is **{dealer_total}**. You won, Congrats! 🎉")
                    elif player_total > 21:
                        await ctx.send(f"**BJ** Game! Your cards are **{player_card1}**, **{player_card2}**, and **{player_card3}**, Your total is **{player_total}**. Dealers total is **{dealer_total}**. You lose, Better luck next time!")

            except asyncio.TimeoutError:
                await ctx.send("**BJ** Game! You took too long, please try again later.")

        elif player_total == 21:
            await ctx.send(f"**BJ** Game! Your cards are **{player_card1}** and **{player_card2}**, Your total is **{player_total}**. Dealers total is **{dealer_total}**. You won, Congrats! 🎉")
        elif player_total > 21:
            await ctx.send(f"**BJ** Game! Your cards are **{player_card1}** and **{player_card2}**, Your total is **{player_total}**. Dealers total is **{dealer_total}**. You lose, Better luck next time!")

    @commands.command(
        name="slotmachine",
        description="Test your luck and play a game of 1x3 slots.",
        usage='slotmachine',
        aliases=['sm']
    )
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def slotmachine(self,ctx):
        slots = ['🍌','🍎','🌠','💕','⭐','🌙']

        slot1 = slots[random.randint(0, 5)]
        slot2 = slots[random.randint(0, 5)]
        slot3 = slots[random.randint(0, 5)]

        slotOutput = f'{slot1} {slot2} {slot3}'

        if slot1 == slot2 and slot1 == slot3:
            await ctx.send(f"You got {slotOutput}, 3 in a row! You won, Congrats! 🎉")
        elif slot1 == slot2 or slot2 == slot3:
            await ctx.send(f"You got {slotOutput}, Nothing. You lose, Better luck next time!")
        else:
            await ctx.send(f"You got {slotOutput}, Nothing. You lose, Better luck next time!")

    @commands.command(
        name="bigslotmachine",
        description="Test your luck and play a game of 3x3 slots.",
        usage='bigslotmachine',
        aliases=['bsm']
    )
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def bigslotmachine(self,ctx):
        slots = ['🍌','🍎','🌠','💕','⭐','🌙','🍏','✨']

        slot1 = slots[random.randint(0, 7)]
        slot2 = slots[random.randint(0, 7)]
        slot3 = slots[random.randint(0, 7)]
        slot4 = slots[random.randint(0, 7)]
        slot5 = slots[random.randint(0, 7)]
        slot6 = slots[random.randint(0, 7)]
        slot7 = slots[random.randint(0, 7)]
        slot8 = slots[random.randint(0, 7)]
        slot9 = slots[random.randint(0, 7)]

        slotOutput = f'''
{slot1} {slot2} {slot3}
{slot4} {slot5} {slot6}
{slot7} {slot8} {slot9}'''

        if slot1 == slot2 and slot1 == slot3:
            await ctx.send(f"{slotOutput}\n\nYou got 3 in a row! You won, Congrats! 🎉")
        elif slot4 == slot5 and slot4 == slot6:
            await ctx.send(f"{slotOutput}\n\nYou got 3 in a row! You won, Congrats! 🎉")
        elif slot7 == slot8 and slot7 == slot9:
            await ctx.send(f"{slotOutput}\n\nYou got 3 in a row! You won, Congrats! 🎉")

        elif slot1 == slot2 or slot2 == slot3:
            await ctx.send(f"{slotOutput}\n\nYou got nothing. You lose, Better luck next time!")
        elif slot4 == slot5 or slot5 == slot6:
            await ctx.send(f"{slotOutput}\n\nYou got nothing. You lose, Better luck next time!")
        elif slot7 == slot8 or slot8 == slot9:
            await ctx.send(f"{slotOutput}\n\nYou got nothing. You lose, Better luck next time!")

        else:
            await ctx.send(f"{slotOutput}\n\nYou got nothing. You lose, Better luck next time!")

    @commands.command(
        name="8ball",
        description="Ask 8ball a question.",
        usage='8ball [question]'
    )
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def eightball(self,ctx, *, question):
        responses = [
            'As I see it, yes.',
            'Ask again later.',
            'Better not tell you now.',
            'Cannot predict now.',
            'Concentrate and ask again.',
            'Don’t count on it.',
            'It is certain.',
            'It is decidedly so.',
            'Most likely.',
            'My reply is no.',
            'My sources say no.',
            'Outlook not so good.',
            'Outlook good.',
            'Reply hazy, try again.',
            'Signs point to yes.',
            'Very doubtful.',
            'Without a doubt.',
            'Yes.',
            'Yes – definitely.',
            'You may rely on it.'
        ]
        answer = random.choice(responses)
        await ctx.send(f"**{answer}** {ctx.author.mention}")

def setup(client):
    client.add_cog(games(client))
