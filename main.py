from dotenv import dotenv_values
import discord
from discord.ext import commands
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

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('Por favor, passe todos os requerimentos :rolling_eyes:.')

# Bot commands
@bot.command()
async def ping(ctx):
    await ctx.send(f':ping_pong: **pong** | **{round(bot.latency, 1):0.3f}s**')

@bot.command()
async def say(ctx, msg):
    userMsg = ctx.message
    await userMsg.delete()
    await ctx.send(msg)

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
    if reason == None:
        await ctx.send('Diga a razão do banimento')
    
    else:
        await member.ban(reason= reason)

@bot.command()
async def random(ctx, init=0, end=1):
    value = int(random.randrange(init, end))
    await ctx.send(value)
    
    

#Run bot
bot.run(token)
