import discord
from discord.ext import commands
import random

token = ''

client = commands.Bot(command_prefix = 'X')

@client.event
async def on_ready():
    print('Hello!')

async def on_message(self, message):
   # don't respond to ourselves
    if message.author == self.user:
        return

    if message.content == 'version':
        await message.channel.send('BetaV1')

    if message.content == 'hi':
        await message.channel.send('hi!')    

    if message.content == 'thisserverinvitelink':
        await message.channel.send('https://discord.gg/DBwQrvR')
        
    if message.content == 'author':
        await message.channel.send('masterXpro7#2678')  

    if message.content == 'howareyou':
        await message.channel.send('im fine thanks, you?')        

@client.command()
async def version(ctx):
    await ctx.send('BetaV1')
    
@client.command()
async def hi(ctx):
    await ctx.send('hi!')
    
@client.command()
async def thisserverinvitelink(ctx):
    await ctx.send('https://discord.gg/DBwQrvR')
    
@client.command()
async def author(ctx):
    await ctx.send('masterXpro7#2678') 

@client.command()
async def howareyou(ctx):
    await ctx.send('im fine thanks, you?')  
    
@client.command(aliases=['talk','tell'])
async def _talk(ctx, * , question):
    responses = ['Hi!',
                'Oh.',
                'Hmmm.',
                'Okay',
                'How can i solve that?',
                'yes?',
                'Oh No',
                'Yeah?',
                'Oh ok im understanding',
                'Hey!',
                'Bye!',
                'hmm',
                'How are you?',
                'thanks',
                'can you repeat again?']

    await ctx.send(random.choice(responses))
    
@client.command(aliases=['tacticchess','puzzle'])
async def _talk(ctx, * , question):
    responses = ['https://github.com/ZeroThink-01/X-Gama/blob/master/jpg/chesstactic2.JPG?raw=true',
                'https://github.com/ZeroThink-01/X-Gama/blob/master/jpg/chesstactic3.JPG?raw=true',
                'https://github.com/ZeroThink-01/X-Gama/blob/master/jpg/chesstactic4.JPG?raw=true',
                'https://github.com/ZeroThink-01/X-Gama/blob/master/jpg/chesstactic5.JPG?raw=true',
                'https://github.com/ZeroThink-01/X-Gama/blob/master/jpg/mate%20in%2017.JPG?raw=true',
                'https://github.com/ZeroThink-01/X-Gama/blob/master/jpg/matein3.JPG?raw=true',
                'https://github.com/ZeroThink-01/X-Gama/blob/master/jpg/taktik1.JPG?raw=true',
                'puzzle not founded.']

    await ctx.send(random.choice(responses))
    
client.run(token)
