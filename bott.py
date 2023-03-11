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
    await interaction.response.send_message("{placeholder}")

@client.command()
async def play(ctx, *args):
    arguments = ', '.join(args)
    await ctx.send(f'{len(args)} arguments: {arguments}')


client.run(tokens.Discord_Token)
