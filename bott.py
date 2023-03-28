import tokens
import discord
import random
from monthlyVolume import mVolList
from discord.ext import commands

client = commands.Bot(command_prefix='$', intents=discord.Intents.all())


# once the bot boots up, it will print in to the console and the bot will start playing the game "$play or /play for
# fun :)"
@client.event
async def on_ready():
    await client.tree.sync()
    print(f'We have logged in as {client.user}')
    await client.change_presence(activity=discord.Game("$play or /play for fun :)"))


# Basic view
class Buttons(discord.ui.View):
    def __init__(self):
        super().__init__(timeout=None)
        self.user_higher = None

    # Will make the variable user_higher True and should stop the view
    @discord.ui.button(label="Higher", style=discord.ButtonStyle.green)
    async def higher(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.user_higher = True
        self.stop()

    # Will make the variable user_higher False and should stop the view
    @discord.ui.button(label="Lower", style=discord.ButtonStyle.red)
    async def lower(self, interaction: discord.Interaction, button: discord.ui.Button):
        self.user_higher = False
        self.stop()


# Slash command
@client.tree.command(name="play", description='Play a game of "higher or lower"')
async def play(interaction: discord.Interaction):
    # Generates 2 random ints
    random_list_item_1 = random.randint(0, 66)
    random_list_item_2 = random.randint(0, 66)
    # Checks if the two random ints are the same and if so replaces it.
    while random_list_item_1 == random_list_item_2 or mVolList[random_list_item_1][2] == mVolList[random_list_item_2][
        2]:
        random_list_item_2 = random.randint(0, 66)
    # Int to add to if user gets answer right
    score_counter = 0
    # Boolean to modify if user gets answer wrong
    have_not_lost = True
    # Using interaction.channel.send so slash command doesn't give error
    await interaction.response.send_message(f"---")

    while have_not_lost:
        buttons = Buttons()
        # Send message to channel that user commanded
        await interaction.channel.send(
            f"`Which is more popular: \n {mVolList[random_list_item_1][0]} --- {mVolList[random_list_item_1][1]} searches a month --- or --- {mVolList[random_list_item_2][0]} --- ? searches a month`")
        await interaction.channel.send(content=f"Is *{mVolList[random_list_item_2][0]}* Higher or Lower?", view=buttons)
        await buttons.wait()
        # if the button pressed gives the right variable give score counter + 1 and print out that the user was right
        if (mVolList[random_list_item_1][2] < mVolList[random_list_item_2][2]) == buttons.user_higher:
            await interaction.channel.send(content=f'`you are correct {mVolList[random_list_item_2][1]}`')
            score_counter += 1
        # Else end the game
        else:
            have_not_lost = False

        random_list_item_1 = random_list_item_2
        random_list_item_2 = random.randint(0, 66)
        # Checks if the two random ints are the same and if so replaces it.
        while random_list_item_1 == random_list_item_2 or mVolList[random_list_item_1][2] == \
                mVolList[random_list_item_2][2]:
            random_list_item_2 = random.randint(0, 66)
    # after leaving the loop print out
    await interaction.channel.send(f"You got {str(score_counter)} Points")
    await interaction.channel.send(f"---")


# text box command started by $
@client.command()
async def play(ctx):
    # Generates 2 random ints
    random_list_item_1 = random.randint(0, 66)
    random_list_item_2 = random.randint(0, 66)
    # Checks if the two random ints are the same and if so replaces it.
    while random_list_item_1 == random_list_item_2 or mVolList[random_list_item_1][2] == mVolList[random_list_item_2][
        2]:
        random_list_item_2 = random.randint(0, 66)
    # Int to add to if user gets answer right
    score_counter = 0
    # Boolean to modify if user gets answer wrong
    have_not_lost = True
    # not needed, just to stay consistent
    await ctx.send(f"---")

    while have_not_lost:
        buttons = Buttons()
        # Send message to channel that user commanded
        await ctx.send(
            f"`Which is more popular: \n {mVolList[random_list_item_1][0]} --- {mVolList[random_list_item_1][1]} searches a month --- or --- {mVolList[random_list_item_2][0]} --- ? searches a month`")
        await ctx.send(content=f"Is *{mVolList[random_list_item_2][0]}* Higher or Lower?", view=buttons)
        await buttons.wait()
        # if the button pressed gives the right variable give score counter + 1 and print out that the user was right
        if (mVolList[random_list_item_1][2] < mVolList[random_list_item_2][2]) == buttons.user_higher:
            await ctx.send(content=f'`you are correct {mVolList[random_list_item_2][1]}')
            score_counter += 1
        # Else end the game
        else:
            have_not_lost = False

        random_list_item_1 = random_list_item_2
        random_list_item_2 = random.randint(0, 66)
        while random_list_item_1 == random_list_item_2 or mVolList[random_list_item_1][2] == \
                mVolList[random_list_item_2][2]:
            random_list_item_2 = random.randint(0, 66)

    await ctx.send(f"You got {str(score_counter)} Points")
    await ctx.send(f"---")


client.run(tokens.Discord_Token)
