import tokens
import discord
import random
from monthlyVolume import mVolList
from discord.ext import commands

client = commands.Bot(command_prefix='$', intents=discord.Intents.all())


@client.event
async def on_ready():
    await client.tree.sync()
    print(f'We have logged in as {client.user}')
    await client.change_presence(activity=discord.Game("$play or /play for fun :)"))


class Buttons(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.user_higher = None

    @discord.ui.button(label="Higher", style=discord.ButtonStyle.green)
    async def higher(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.user_higher = True
        self.stop()

    @discord.ui.button(label="Lower", style=discord.ButtonStyle.red)
    async def lower(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.user_higher = False
        self.stop()


@client.tree.command(name="play", description='Play a game of "higher or lower"')
async def play(interaction: discord.Interaction):
    a = random.randint(0, 66)
    c = random.randint(0, 66)
    while a == c or mVolList[a][2] == mVolList[c][2]:
        c = random.randint(0, 66)
    score_counter = 0
    have_lost = True
    await interaction.channel.send(f"---")
    while have_lost:
        buttons = Buttons()
        await interaction.channel.send(
            f"`Which is more popular: \n {mVolList[a][0]} --- {mVolList[a][1]} searches a month --- or --- {mVolList[c][0]} --- ? searches a month`")
        await interaction.channel.send(content=f"Is *{mVolList[c][0]}* Higher or Lower?", view=buttons)
        await buttons.wait()
        if (mVolList[a][2] < mVolList[c][2]) == buttons.user_higher:
            await interaction.channel.send(content=f'`you are correct {mVolList[c][1]}`')

            score_counter += 1
        else:
            have_lost = False
        a = c
        c = random.randint(0, 66)
        while a == c or mVolList[a][2] == mVolList[c][2]:
            c = random.randint(0, 66)
    await interaction.channel.send(f"You got {str(score_counter)} Points")
    await interaction.channel.send(f"---")


@client.command()
async def play(ctx):
    a = random.randint(0, 66)
    c = random.randint(0, 66)
    while a == c or mVolList[a][2] == mVolList[c][2]:
        c = random.randint(0, 66)
    score_counter = 0
    have_lost = True
    await ctx.send(f"---")
    while have_lost:
        buttons = Buttons()
        await ctx.send(
            f"`Which is more popular: \n {mVolList[a][0]} --- {mVolList[a][1]} searches a month --- or --- {mVolList[c][0]} --- ? searches a month`")
        await ctx.send(content=f"Is *{mVolList[c][0]}* Higher or Lower?", view=buttons)
        await buttons.wait()
        if (mVolList[a][2] < mVolList[c][2]) == buttons.user_higher:
            await ctx.send(content=f'`you are correct {mVolList[c][1]}`')

            score_counter += 1
        else:
            have_lost = False
        a = c
        c = random.randint(0, 66)
        while a == c or mVolList[a][2] == mVolList[c][2]:
            c = random.randint(0, 66)
    await ctx.send(f"You got {str(score_counter)} Points")
    await ctx.send(f"---")


client.run(tokens.Discord_Token)
