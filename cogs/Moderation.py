import discord
from discord.ext import commands

class Moderation(commands.Cog):
    
    def __init__(self , client):
        self.client = client
 #The kick command 
    @commands.command(aliases=['k'])
    async def kick(self, ctx,member : discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f'Kicked {member.mentio}')

#The ban Command
    @commands.command(aliases=['b'])
    async def ban(self,ctx,member : discord.Member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}')

#The unban commnad
    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

        if(user.name, user.discriminator) == (member_name,member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return
#The clean command
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self,ctx,ammount : int):
        await ctx.channel.purge(limit=ammount)
    @clear.error#Error checker for clean command
    async def oclear_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please specifecy ammount of messages to delete')
        if isinstance(error,commands.MissingPermissions):
            await ctx.send('Sorry no permission to do that!')

    
def  setup(client):
    client.add_cog(Moderation(client))