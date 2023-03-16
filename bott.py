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
        self.user_higher = True

    @discord.ui.button(label="Higher", style=discord.ButtonStyle.green)
    async def higher(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.user_higher = True


    @discord.ui.button(label="Lower", style=discord.ButtonStyle.red)
    async def lower(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.user_higher = False


@client.tree.command(name="play", description='Play a game of "higher or lower"')
async def play(interaction: discord.Interaction):

    score_counter = 0
    have_lost = True
    while have_lost:
        interaction.defer()
        a = random.randint(0, 66)
        c = random.randint(0, 66)
        while a == c or mVolList[a][2] == mVolList[c][2]:
            c = random.randint(0, 66)
        await interaction.channel.send(
            f"Which is more popular: \n {mVolList[a][0]} --- {mVolList[a][1]} searches a month --- or --- {mVolList[c][0]} --- ? searches a month")
        await interaction.response.send_message(content="Higher or Lower?", view=Buttons())
        if (mVolList[a][2] < mVolList[c][2]) == Buttons().user_higher:
            await interaction.channel.send(content=f'you are correct {mVolList[c][1]}')

            score_counter += 1
        else:
            have_lost = False
        a = random.randint(0, 66)
        c = random.randint(0, 66)
        while a == c or mVolList[a][2] == mVolList[c][2]:
            c = random.randint(0, 66)
    await interaction.channel.send(f"You got {str(score_counter)} Points")


@client.command()
async def play(ctx, arg):
    await ctx.send(f'{ctx.guild.get_member(int(arg))}')


client.run(tokens.Discord_Token)
