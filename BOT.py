import os
import subprocess
import random
import discord
import sys

from dotenv import load_dotenv
from discord.ext import commands


#get environment info
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')



@client.event
async def on_ready():
        for guild in client.guilds:
            if guild.name == GUILD:
                break

        print(
            f'{client.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )

client.run(TOKEN)

