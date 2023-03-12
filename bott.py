import tokens
import discord
from discord.ext import commands

client = commands.Bot(command_prefix='$', intents=discord.Intents.all())


@client.event
async def on_ready():
    await client.tree.sync()
    print(f'We have logged in as {client.user}')
    await client.change_presence(activity=discord.Game("$play for fun :)"))


@client.tree.command(name="play", description='Play a game of "higher or lower"')
async def play(interaction: discord.Interaction):
    a = str(interaction.guild.get_member(247320522814259200))
    await interaction.response.send_message(a[:-5:])


@client.command()
async def play(ctx, *args):
    await ctx.send(f'{ctx.guild.get_member(243320522814259200)}')


client.run(tokens.Discord_Token)
