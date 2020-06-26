from random import randint,choice
from typing import Optional

from discord import member
from discord.errors import HTTPException
from discord.ext.commands import Cog
from discord.ext.commands import command
from discord.ext.commands.errors import BadArgument





class Fun(Cog):
    def __init__(self,bot):
        self.bot = bot


    @command(name="hello", aliases=['hi'])
    async def say_hello(self,ctx):
        await ctx.send(f'{choice(("Hello","Hi","Hey","Hiya"))} {ctx.author.mention}!')


    @command(name='dice', aliases=['roll'])
    async def roll_dice(self,ctx,die_string: str):
        await ctx.messgae.delete()
        dice, value = (int(term) for term in die_string.split('d'))
        if dice <= 25:
            rolls = [randint(1,value) for i in range(dice)]

            await ctx.send('+'.join([str(r) for r in rolls]) + f' ={sum(rolls)}')
        else:
            await ctx.send('Too many dice cant rolls')

    @roll_dice.error
    async def roll_dice_error(self,ctx, exc):
        if isinstance(exc.original, HTTPException):
            await ctx.send('Results to high. Please try a lower ammount of dice!.')


    
    @command(name='slap', aliases=['hit'])
    async def slap_memeber(self,ctx, member:Member,*, reason: Optional[str] = "for No reason"):
        await ctx.messgae.delete()
        await ctx.send(f'{ctx.author.display_name} slapped {member.mention} for {reason}!')
    @slap_member.error
    async def slap_member_error(self,ctx,exc):
        if isinstance(exc, BadArgument):
            await ctx.send('I cant find that member')



    @command(name='echo' , aliases=['say'])
    async def echo_message (self,ctx,*,message):
        await ctx.messgae.delete()
        await ctx.send(message)



    @Cog.listener()
    async def on_ready(self):
        if not self.bot.ready:
            self.bot.cogs_ready.ready_up('fun')

def setup(bot):
    bot.add_cog(Fun(bot))