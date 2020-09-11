import discord
from discord.ext import commands
import random

Started = 'Bot is working!'

token = 'XXXXXXXXXXXXXXXXXXXXXXXXX'

client = commands.Bot(command_prefix = 'X')

@client.event
async def on_ready():
    print('Hello!')
    print(Started)

async def on_message(self, message):
   # don't respond to ourselves
    if message.author == self.user:
        return

    if message.content == 'version':
        await message.channel.send('BetaV1')

    if message.content == 'hi':
        await message.channel.send('hi!')    
        
    if message.content == 'author':
        await message.channel.send('masterXpro7#2678')  

    if message.content == 'howareyou':
        await message.channel.send('im fine thanks, you?')

    if message.content == 'rpshelp':
        await message.channel.send('Xrps_(Your Choice) Example: Xrps_rock')

    if message.content == 'invite':
        await message.channel.send('You can also invite me! ( https://sites.google.com/view/x-gama/main-page ) , Github Code: https://github.com/ZeroThink-01/X-Gama')  

@client.command()
async def rpshelp(ctx):
    await ctx.send('Xrps_(Your Choice) Example: Xrps_rock')
    
@client.command()
async def invite(ctx):
    await ctx.send('You can also invite me! ( https://sites.google.com/view/x-gama/main-page ) , Github Code: https://github.com/ZeroThink-01/X-Gama')

@client.command()
async def version(ctx):
    await ctx.send('BetaV1')

@client.command()
async def hi(ctx):
    await ctx.send('hi!')
    
@client.command()
async def author(ctx):
    await ctx.send('masterXpro7#2678') 

@client.command()
async def howareyou(ctx):
    await ctx.send('im fine thanks, you?')
        
@client.command()
async def bird(ctx):
    responses = ['https://st3.depositphotos.com/23057334/34866/v/450/depositphotos_348664714-stock-illustration-swallow-flight-isolated-white-background.jpg',
                'https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcQzxaixGcue_nINriYyf-ln53iTcioe3cV19Q&usqp=CAU',
                'https://st.depositphotos.com/1052928/4396/i/450/depositphotos_43963763-stock-photo-blue-budgie.jpg']
    
    await ctx.send(random.choice(responses))
    
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
                'Okay , im understanding',
                'Hey!',
                'Bye!',
                'hmm',
                'How are you?',
                'thanks',
                'can you repeat again?']

    await ctx.send(random.choice(responses))
    
@client.command(aliases=['tacticchess','puzzle'])
async def _puzzle(ctx):
    responses = ['https://github.com/ZeroThink-01/X-Gamav1.7/blob/master/jpg/chesstactic2.JPG?raw=true',
                'https://github.com/ZeroThink-01/X-Gamav1.7/blob/master/jpg/chesstactic3.JPG?raw=true',
                'https://github.com/ZeroThink-01/X-Gamav1.7/blob/master/jpg/chesstactic4.JPG?raw=true',
                'https://github.com/ZeroThink-01/X-Gamav1.7/blob/master/jpg/chesstactic5.JPG?raw=true',
                'https://github.com/ZeroThink-01/X-Gamav1.7/blob/master/jpg/mate%20in%2017.JPG?raw=true',
                'https://github.com/ZeroThink-01/X-Gamav1.7/blob/master/jpg/matein3.JPG?raw=true',
                'https://github.com/ZeroThink-01/X-Gamav1.7/blob/master/jpg/taktik1.JPG?raw=true',
                'puzzle not founded.']

    await ctx.send(random.choice(responses))
    
@client.command()
async def rps_scissors(ctx):
    responses = ['Your Choice: Scissors , My Choice: Rock , I won!',
                'Your Choice: Scissors , My Choice: Paper , You won!',
                'Your Choice: Scissors , My Choice: Scissors , Draw!']
    
    await ctx.send(random.choice(responses))
    
@client.command()
async def rps_rock(ctx):
    responses = ['Your Choice: Rock , My Choice: Paper , I won!',
                'Your Choice: Rock , My Choice: Scissors , You won!',
                'Your Choice: Rock , My Choice: Rock , Draw!']
    
    await ctx.send(random.choice(responses))
    
@client.command()
async def rps_paper(ctx):
    responses = ['Your Choice: Paper , My Choice: Scissors , I won!',
                'Your Choice: Paper , My Choice: Rock , You won!',
                'Your Choice: Paper , My Choice: Paper , Draw!']
    
    await ctx.send(random.choice(responses))
    
# Finish :)  
    
client.run(token)
