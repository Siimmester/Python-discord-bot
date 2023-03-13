import tokens
import discord
# import random
# from monthlyVolume import mVolList
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
        self.value = None

    @discord.ui.button(label="Higher", style=discord.ButtonStyle.green)
    async def higher(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.channel.send(content="Higher")

    @discord.ui.button(label="Lower", style=discord.ButtonStyle.red)
    async def lower(self, interaction: discord.Interaction, button: discord.ui.Button):
        await interaction.channel.send(content="Lower")


@client.tree.command(name="play", description='Play a game of "higher or lower"')
async def play(interaction: discord.Interaction):
    await interaction.response.send_message(content="Higher or Lower?", view=Buttons())


@client.command()
async def play(ctx, arg):
    await ctx.send(f'{ctx.guild.get_member(int(arg))}')


client.run(tokens.Discord_Token)
