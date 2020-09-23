class eventandrun:

    # events
    @client.event
    async def on_command_error(ctx, error):
        if isinstance(error, CommandNotFound):
            return
        raise error
        
    @client.event
    async def on_message(message):
        print(message.content)
        await client.process_commands(message)
    
    @client.event
    async def on_ready():
        print('X-Gama discord-bot is ready!')
        print(Started)

    async def on_message(self, message):
        if message.author == self.user:
            return
 
