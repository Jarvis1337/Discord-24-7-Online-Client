import discord
import os
import keep_alive

from discord.ext import commands

client = commands.Bot(command_prefix='..', self_bot=True)

# <!-- Import Your Self Bot Commands <3 --> 

@client.event
async def on_ready():
    activity = discord.Activity(type=discord.ActivityType.listening, name="Yours-Jarvis on Github") # Activity Types :- listening, watching, streaming
    await client.change_presence(status=discord.Status.dnd, activity=activity)

keep_alive.keep_alive()
client.run(os.getenv("TOKEN"), bot=False)

## <!-- 🚀 Please follow on GitHub to stay tuned with us for more Exciting future Updates like this. | © 2022 — Made By Your's Jarvis #2431 with ♥ -->
