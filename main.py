import discord
import random
import os
from discord.ext import commands

#Makes the bot command to start with dot(.)
client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online,activity=discord.Game('https://quicc.page.link/Dashy-3'))
    print("Bot Online")



#The ping commnad
#@client.command()
#sync def ping(ctx):
#await ctx.send(f'Pong! {round(client.latency*1000)}ms')


#Loads files from folder cogs
@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

#Unloads files from folder cogs
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

#Reload function for cogs
@client.command()
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

#loads all files from folder cogs as the bot starts
for filename in os.listdir('./cogs'):
    if filename.endswith('py'):
        client.load_extension(f'cogs.{filename[:-3]}')

#Bot IID Should be empty
client.run('')