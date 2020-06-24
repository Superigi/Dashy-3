import discord
from discord.ext import commands

class Moderation(commands.Cog):
    
    def __init__(self , client):
        self.client = client
 #The kick command 
    @commands.command(aliases=['k'])
    async def kick(self, ctx,member : discord.Member, *, reason : str):
        await member.kick(reason=reason)
        await ctx.send(f'Kicked {member.mentio}')
    @kick.error#Error checker for clean command
    async def oclear_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please specifecy the reason')
            print('Missing reason error 404')
        if isinstance(error,commands.MissingPermissions):
            await ctx.send('Sorry no permission to do that!')
            print('Missing permission error 408')

#The ban Command
    @commands.command(aliases=['b'])
    async def ban(self,ctx,member : discord.Member, *, reason : str):
        await member.ban(reason=reason)
        await ctx.send(f'Banned {member.mention}')
    @ban.error#Error checker for clean command
    async def oclear_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please specifecy reason')
            print('Missing reason error 404')
        if isinstance(error,commands.MissingPermissions):
            await ctx.send('Sorry no permission to do that!')
            print('Missing permission error 408')

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
    @unban.error#Error checker for clean command
    async def oclear_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please @user')
            print('Missing user error 404')
        if isinstance(error,commands.MissingPermissions):
            await ctx.send('Sorry no permission to do that!')
            print('Missing permission error 408')
#The clean command
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self,ctx,ammount : int):
        await ctx.channel.purge(limit=ammount)
    @clear.error#Error checker for clean command
    async def oclear_error(self,ctx, error):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send('Please specifecy ammount of messages to delete')
            print('Missing Argumnet Error')
        if isinstance(error,commands.MissingPermissions):
            await ctx.send('Sorry no permission to do that!')
            print('Missing permission error 408')

    
def  setup(client):
    client.add_cog(Moderation(client))