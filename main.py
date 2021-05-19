from dotenv import dotenv_values
import discord
import time
import asyncio
from discord.ext import commands
import random
from modules import channels, embed, blacklist, anticaps

token = "ODQyOTI2Nzg4NDQ3NDM2ODAx.YJ8avw.13X8k4Pk8Ua5YH7c8Y3NlZkTLN4"
bot = commands.Bot(command_prefix='%', case_insensitive=True)
bot.remove_command('help')
client = discord.Client()
    
# Bot events
@bot.event
async def on_ready():
    print(f'{bot.user.name} running.')
    await bot.change_presence(activity=discord.Streaming(name="%info", url="https://www.twitch.tv/123"))
    
@bot.event
async def on_message(message):
    #Verify if contain some swear word
    wordVerify = blacklist.Blacklist(message)
    swearWords = wordVerify.verify()
    
    #Verify capslock
    capsVerify = anticaps.AntiCaps(message.content)
    caps = capsVerify.analyse()
        
    if caps:
        await message.channel.purge(limit=1)
        await message.channel.send(f'{message.author.mention}, olha o caps amigo 🙄.')
    
    elif swearWords >= 1:
        await message.channel.purge(limit=1)
        await message.channel.send(f'{message.author.mention}, Não permitimos esse tipo de linguajar 😠.')
    
    elif swearWords <= 0:
        await bot.process_commands(message)

    
# Bot commands
@bot.command(aliases=['p', 'q'])
async def ping(ctx):
    before = time.monotonic()
    message = await ctx.send("Pong?")
    ping = (time.monotonic() - before) * 1000
    await message.edit(content=f":ping_pong: Pong! | **{int(ping)}ms**")

@bot.command()
async def pong(ctx):
    await ctx.send("ping? kkk")

@bot.command()
async def say(ctx, *, content: str):
    await ctx.message.delete()
    await ctx.send(content)

@bot.command()
async def poll(ctx, *, message=None):
    await ctx.message.delete()
    if message == None:
        await ctx.send(f'{ctx.message.author.mention}, Não é possivel criar votações sem descrição')
    
    else:
        embedPoll = discord.Embed(color=0x005EFF, title="Votação", description=f"{message}").set_footer(text='30 segundos')
        msg = await ctx.send(embed=embedPoll)
        await msg.add_reaction('👍')
        await msg.add_reaction('👎')     

@bot.command()
async def create(ctx, name):
    createChannel = channels.ChannelsFunction(ctx, name)
    await createChannel.create()

@bot.command()
async def delete(ctx, name):
    delChannel = channels.ChannelsFunction(ctx, name)
    await delChannel.delete(discord)

@bot.command()
async def info(ctx):
    embedDiscord = embed.EmbedFunction(ctx)
    await embedDiscord.embedCreate(discord, 'info')

@bot.command()
async def help(ctx):
    embedDiscord = embed.EmbedFunction(ctx)
    await embedDiscord.embedCreate(discord, 'help')

@bot.command()
async def ban(ctx, member: discord.Member, reason=None):
    author = ctx.message.author    
    
    if author.guild_permissions.administrator:
        if reason == None:
            await ctx.send('Diga a razão do banimento')
        
        else:
            await member.ban(reason= reason)
    
    else:
        await ctx.send(f'{author.mention} Você não tem permissão para banir membros')

@bot.command()
async def unban(ctx, id: int):
    author = ctx.message.author    
    
    if author.guild_permissions.administrator:
        user = await bot.fetch_user(id)
        await ctx.guild.unban(user)
    
    else:
        await ctx.send(f'{author.mention} Você não tem permissão para desbanir membros')

@bot.command()
async def dice(ctx, init: int, end: int):
    value = int(random.randrange(init, end))
    await ctx.send(value)

@bot.command()
async def clear(ctx, amount = 6):
    author = ctx.message.author    
    
    if author.guild_permissions.administrator:
        await ctx.channel.purge(limit=amount)
    
    else:
        await ctx.send(f'{author.mention} Você não tem permissão para apagar conversas no canal')

@bot.command()
async def invite(ctx):
    author = ctx.message.author.mention
    await ctx.send(f'{author}, Meu convite https://discord.com/api/oauth2/authorize?client_id=842926788447436801&permissions=8&scope=bot')


#Run bot
bot.run("Token here")
