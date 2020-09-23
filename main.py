import discord
from discord.ext import commands
import random
import Xgamaversion
from discord.ext.commands import CommandNotFound

Started = 'Bot is working!'

client = commands.Bot(command_prefix = 'X')
    
token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'

################################################################################################

    #commands
    
class NormalCommands:
  
    @client.command()
    async def rpshelp(ctx):
        await ctx.send(':gear: Xrps_(Your Choice) Example: Xrps_rock')
    
    @client.command()
    async def invite(ctx):
        await ctx.send('You can also invite me! ( https://sites.google.com/view/x-gama/main-page ) , Github Code: https://github.com/ZeroThink-01/X-Gama')

    @client.command()
    async def version(ctx):
        await ctx.send(':gear: BetaV1')

    @client.command()
    async def hi(ctx):
        await ctx.send(':100: hi!')
    
    @client.command()
    async def author(ctx):
        await ctx.send('masterXpro7#2678') 

    @client.command()
    async def howareyou(ctx):
        await ctx.send('im fine thanks, you?')
        
class RandomCommands:
    
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
        responses = ['White to play. https://github.com/ZeroThink-01/X-Gamav1.7/blob/master/jpg/chesstactic2.JPG?raw=true',
                    'Black to play. https://github.com/ZeroThink-01/X-Gamav1.7/blob/master/jpg/chesstactic3.JPG?raw=true',
                    'White to play. https://github.com/ZeroThink-01/X-Gamav1.7/blob/master/jpg/chesstactic4.JPG?raw=true',
                    'Black to Play. https://github.com/ZeroThink-01/X-Gamav1.7/blob/master/jpg/chesstactic5.JPG?raw=true',
                    'Black to play. https://github.com/ZeroThink-01/X-Gamav1.7/blob/master/jpg/mate%20in%2017.JPG?raw=true',
                    'Black to play. https://github.com/ZeroThink-01/X-Gamav1.7/blob/master/jpg/matein3.JPG?raw=true',
                    'White to play. https://github.com/ZeroThink-01/X-Gamav1.7/blob/master/jpg/taktik1.JPG?raw=true',
                    'puzzle not founded. Puzzle command is not working for now.']

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

###############################################################################

class eventandrun:

    # events
    @client.event
    async def on_command_error(ctx, error):
        if isinstance(error, CommandNotFound):
            return
        raise error
    
    @client.event
    async def on_ready():
        print('X-Gama discord-bot is ready!')
        print(Started)

    async def on_message(self, message):
        if message.author == self.user:
            return
 
####################################################

    # run!

    # Finish :)  

    client.run(token)
