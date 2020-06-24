import discord
from discord.ext import commands
import random

class Fun(commands.Cog):
    def __init__(self , client):
        self.client = client
#The 8ball command
    @commands.command(aliases=['8ball'])
    async def _8ball(self,ctx,*,question):
        responces = ["It is certain.",
                    "It is decidedly so.",
                    "Without a doubt.",
                    "Yes - definitely.",
                    "You may rely on it.",
                   "As I see it, yes.",
                    "Most likely.",
                    "Outlook good.",
                    "Yes.",
                    "Signs point to yes.",
                    "Reply hazy, try again.",
                    "Ask again later.",
                    "Better not tell you now.",
                    "Cannot predict now.",
                    "Concentrate and ask again.",
                    "Don't count on it.",
                    "My reply is no.",
                    "My sources say no.",
                    "Outlook not so good.",
                    "Very doubtful."]
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responces)}')
    @_8ball.error
    async def oclear_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please specifecy the question')
    #The ping commnad
    @commands.command()
    async def ping(self,ctx):
        await ctx.send('Pong!')














def  setup(client):
     client.add_cog(Fun(client))