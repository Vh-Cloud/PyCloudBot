from dotenv import dotenv_values
import discord
import time
from discord.ext import commands
import random
from modules import channels, embed


token = dotenv_values(".env")['TOKEN']
bot = commands.Bot(command_prefix='%', case_insensitive=True)
bot.remove_command('help')
client = discord.Client()

# Events
@bot.event
async def on_ready():
    print(f'{bot.user.name} running.')
    await bot.change_presence(activity=discord.Streaming(name="%info", url="https://www.twitch.tv/123"))

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
async def create(ctx, name):
    createChannel = channels.ChannelsFunction(ctx, name)
    createChannel.create()

@bot.command()
async def delete(ctx, name):
    delChannel = channels.ChannelsFunction(ctx, name)
    delChannel.delete(discord)

@bot.command()
async def info(ctx):
    embedDiscord = embed.EmbedFunction(ctx)
    embedDiscord.embedCreate(discord, 'info')

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


#Run bot
bot.run(token)
