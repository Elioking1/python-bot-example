# Let's create some usefuls variables
PREFIX="YOUR PREFIX HERE"
TOKEN="YOUR TOKEN HERE"
# Let's import Discord.py
import discord
# Let's import the modules from it
from discord.ext import commands
# Let's create the bot
client = commands.Bot(command_prefix=PREFIX)
# When the bot is ready
@client.event
async def on_ready():
    # Let's log it in the console
    print("The bot is ready and connected!")

# Let's create the commands
@client.command()
# If the command is boop
async def boop(ctx):
    # Let's return Beep
    await ctx.send("Beep")
# Let's connect the bot to Discord
client.run(TOKEN)