import discord
from discord.ext import commands
import random
import Xgamaversion
from discord.ext.commands import CommandNotFound, has_permissions, MissingPermissions
import statcord 

Started = 'Bot is working!'

client = commands.Bot(command_prefix = 'X')
client.remove_command('help')

key = "-"
api = statcord.Client(client,key)
api.start_loop()
    
token = '-'

################################################################################################

    #commands
    
class NormalCommands:

    @client.command()
    async def ping(ctx):
        await ctx.send(f'Pong! :ping_pong: ```Latency: {client.latency} second.```')
        
    @client.command()
    async def xD(ctx):
        await ctx.send('XD')

    @client.command()
    async def issue(ctx):
        await ctx.send(':gear: Send Private Message to me! ```<<< BETA``` , ```Recommended >>>``` Or Open Issue In Github! :gear:')
    
    @client.command()
    async def rpshelp(ctx):
        await ctx.send(':gear: Xrps_(Your Choice) Example: Xrps_rock')
        await ctx.send(':warning: Find a Secret Command Of RPS game!')
    
    @client.command()
    async def invite(ctx):
        await ctx.send('You can also invite me! ( https://xgama.herokuapp.com/ ) , Github Code: https://github.com/ZeroThink-01/X-Gama')

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
        
    @client.command()
    async def puzzleadder(ctx):
        await ctx.send('Help to add puzzles to bot? Then come to our server! (Including Puzzle Admin Role) https://discord.gg/9nqSejU ')
        
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
        responses = ['White to play. Author = masterXpro7#2678 https://github.com/ZeroThink-01/X-Gamav1.7/blob/master/jpg/chesstactic2.JPG?raw=true',
                    'Black to play. Author = masterXpro7#2678 https://github.com/ZeroThink-01/X-Gamav1.7/blob/master/jpg/chesstactic3.JPG?raw=true',
                    'White to play. Author = masterXpro7#2678 https://github.com/ZeroThink-01/X-Gamav1.7/blob/master/jpg/chesstactic4.JPG?raw=true',
                    'Black to Play. Author = masterXpro7#2678 https://github.com/ZeroThink-01/X-Gamav1.7/blob/master/jpg/chesstactic5.JPG?raw=true',
                    'Black to play. Author = masterXpro7#2678 https://github.com/ZeroThink-01/X-Gamav1.7/blob/master/jpg/mate%20in%2017.JPG?raw=true',
                    'Black to play. Author = masterXpro7#2678 https://github.com/ZeroThink-01/X-Gamav1.7/blob/master/jpg/matein3.JPG?raw=true',
                    'White to play. Author = masterXpro7#2678 https://github.com/ZeroThink-01/X-Gamav1.7/blob/master/jpg/taktik1.JPG?raw=true',
                    'puzzle not founded. Puzzle command is not working for now.']

        await ctx.send(random.choice(responses))
        
    @client.command()
    async def puzzle_atomic(ctx):
        responses = ['White to play. Variant = Atomic , Author = masterXpro7#2678 https://github.com/ZeroThink-01/X-Gama/blob/master/jpg/atomicchess.JPG?raw=true',
                    'puzzle not founded. Puzzle command is not working for now.']

        await ctx.send(random.choice(responses))
        
    @client.command()
    async def puzzle_racingkings(ctx):
        responses = ['Black to play. Variant = Racingkings , Author = masterXpro7#2678 https://github.com/ZeroThink-01/X-Gama/blob/master/jpg/chessRK.JPG?raw=true',
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
        
    @client.command()
    async def emoji(ctx):
        responses = [':100:',
                    ':thumbsup:',
                    ':laughing:',
                    ':smiling_imp:']
    
        await ctx.send(random.choice(responses))
        
    @client.command()
    async def help(ctx):
        await ctx.send('''```Commands :
  Category Chess:
  Xpuzzle     {sending chess puzzles}
  Xpuzzle_atomic  {sending atomic chess puzzles}
  Xpuzzle_racingkings    {sending RacingKings chess puzzles}
  Xpuzzleadder             (Help to add puzzles to bot? then come to our server! (including puzzle admin role) )

  Category Talk:
  Xtalk (your message)       {sending random messages to your questions!}
  Xauthor            {sending author's id}
  Xhi                    { say "hello" to bot! }
  Xhowareyou     { say "how are you?" to bot! }
  Xinvite          { invite link , also some little websites to invite! }
  Xversion         {The version of bot}
  Xissue        (issues/feedbacks)
  Xping          {Ping-Pong : Latency}
  XxD             (XD)
  
  Category Moderation:
  Xwarn              ( You Can Only warn if you have these PERMISSIONS:)
                     - Manage nicknames!
                     - Ban Members!
                     ====================================================
                      
 Category Help:
  Xhelp                {..... ( For more info and commands type 'Xhelp' ) .....}

 Category Games:
  Xrps_(chosen power) (example : Xrps_rock ; can use: rock, scissors, paper) { Play RockScissorsPaper }
  Xrpsclue           ( Want to find secret Powers in RPS game? Then use it! )
  Xrpshelp       {Howto play RockScissorsPaper game?}
  Xemoji            { Sends Random Emojies from Server! }    


SEND DM (PRIVATE MESSAGES) MESSAGES TO BOT FOR SUBMITTING YOUR ISSUE/FEEDBACK!
```''')

    @client.command()
    async def D(ctx):
        return

############################################################################ SECRET!!!!
        
    @client.command()
    async def rpsclue(ctx):
        await ctx.send('''
Clue 1 :white_check_mark: = Light , Dark.
        
^^ Task 1
 =========================================
Clue 1  :white_check_mark: = Blue
Clue 2 :white_check_mark: = Raining
        
^^ Task 2
        
==========================================

Clue 1 :white_check_mark: = Red , Orange , Yellow

^^ Task 3

==========================================    
Other Tasks added in soon!

        
''')
############################################################################### WARN

    @client.command(pass_context = True)
    @has_permissions(manage_nicknames=True, ban_members=True)
    async def warn(ctx, member: discord.Member, *, reason=None):
        await ctx.send(f'User {member} Warned!')
        await ctx.send(f'{member} Please be more careful!')

###############################################################################

class eventandrun:

    # events
    @client.event
    async def on_command(ctx):
        api.command_run(ctx)
        
    @client.event
    async def on_command_error(ctx, error):
        if isinstance(error, CommandNotFound):
            print('Command Error')
            print(error)
        await ctx.send(f'```{error} / may be try "Xhelp" / ?```')
        return
        raise error

    @client.event
    async def on_ready():
        print(f'Discord.py version: {discord.__version__}')
        print('X-Gama discord-bot is ready!')
        print(Started)
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=" In 7 Servers! | Xhelp , Xissue |"))
    
    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return
       
    @client.event
    async def on_message(message):
        if isinstance(message.channel, discord.channel.DMChannel) and message.author != client.user: 
            responses = ['Marked as a issue!',
                        'Hello!',
                        'Can you repeat it again?',
                        'Thank You For your feedback!']
            await message.channel.send(random.choice(responses))
            print(message)
            
        await client.process_commands(message)
           
############################################################################### 
        
###############################################################################

        # run!

        # Finish :)  

    client.run(token)