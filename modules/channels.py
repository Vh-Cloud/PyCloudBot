class ChannelsFunction:
    
    def __init__(self, ctx, name):
        self.context = ctx
        self.name = name
    
    async def delete(self, discord):
        author = self.context.message.author
    
        if author.guild_permissions.administrator:
            guild = self.context.message.guild
            existChannel = discord.utils.get(guild.channels, name=self.name)
            
            if existChannel != None:
                await existChannel.delete()
                await self.context.send(f'{author.mention} Deletou o canal {self.name}')
            
            else:
                await self.context.send(f'{author.mention} O canal {self.name} não existe')
        
        else:
            await self.context.send(f'{author.mention} Você não tem permissão para deletar canais')
        
    async def create(self):
        author = self.context.message.author
        guild = self.context.message.guild
    
        if author.guild_permissions.administrator:
            await guild.create_text_channel(self.name)
            await self.context.send(f'Novo canal ({self.name}) criado por {author.mention}')
        
        else:
            await self.context.send(f'{author.mention} Você não tem permissão para criar canais')
