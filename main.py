import discord
import random
import os
from discord.ext import commands, tasks
from itertools import cycle

#Makes the bot command to start with dot(.)
client = commands.Bot(command_prefix = '.')
status = cycle(['https://quicc.page.link/Dashy-3','mc.superfiremc.net'])

#Starting events
@client.event
async def on_ready():
    change_status.start()
    print("Bot Online")

#loop for the Playing status
@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

#General error finder
@client.event
async def on_command_error(ctx,error):
     if isinstance(error, commands.CommandNotFound):
        await ctx.send('Please do ``.help`` to See the commands avaible')

#stores user id
def is_it_me(ctx):
    return ctx.author.id == 00000000000000 #0000000000 = place holder




#Loads files from folder cogs
@client.command()
@commands.check(is_it_me)#checks for the user id stored  and then allowes the command
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

#Unloads files from folder cogs
@client.command()
@commands.check(is_it_me)
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

#Reload function for cogs
@client.command()
@commands.check(is_it_me)
async def reload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    client.load_extension(f'cogs.{extension}')

#loads all files from folder cogs as the bot starts
for filename in os.listdir('./cogs'):
    if filename.endswith('py'):
        client.load_extension(f'cogs.{filename[:-3]}')

#Bot IID Should be empty
client.run('')