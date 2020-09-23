import discord
from discord.ext import commands
import random
import Xgamaversion
import commandsxgama

Started = 'Bot is working!'

client = commands.Bot(command_prefix = 'X')
    
token = '--------------------------'

class eventandrun:

    # events
          
    @client.event
    async def on_ready():
        print('X-Gama discord-bot is ready!')
        print(Started)

    async def on_message(self, message):
        if message.author == self.user:
            return

    # run!

    # Finish :)  

    client.run(token)
