from discord.ext.commands import Bot as BotBase
from glob import glob
from discord import Embed, File
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime
from discord.ext.commands import CommandNotFound
from ..db import db
from asyncio import sleep


PREFIX = '+'
OWNER_IDS =[234472372491517952]
COGS = [path.split('\\')[-1][:-3] for path in glob('./lib/cogs/*.py')]
class Ready(object):
    def __init__(self):
        for cog in COGS:
            setattr(self, cog, False)
    def ready_up(self,cog):
        setattr (self, cog,True)
        print(f'{cog} cog ready')
    def all_ready(self):
        return all([getattr(self, cog) for cog in COGS])
class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.cogs_ready = Ready()
        self.guild = None
        self.scheduler = AsyncIOScheduler()

        db.autosave(self.scheduler)

        super().__init__(command_prefix=PREFIX, owner_ids=OWNER_IDS)
    def setup(self):
        for cog in COGS:
            self.load_extension(f"lib.cogs.{cog}")
            print(f'{cog} cog loadded')
            print('Setup completed')

    def run(self, version):
        self.VERSION = version
        print('Running Setup ...')
        self.setup()
        try:
            with open('./lib/bot/token.0','r',encoding='utf=8')as tf:
                self.TOKEN = tf.read()
        except:
            print("There was an error trying to load the token in ./lib/bot/token.0\nThe program will now exit")
            exit(1)
        print('Running bot ...')
        super().run(self.TOKEN, reconnect=True)
    
    async def rules_reminder(self):
        await self.stdout.send('Remeber to add rules here')



    async def on_connect(self):
        print('Bot is connected')

    async def on_disconect(self):
        print('Bot Has Disconnected')

    async def on_error(self,err, *args, **kwargs):
        if err == "on_command_error":
            await args[0].send("Something is Wrong.")

        raise

    async def on_command_error(self,ctx, exc):
        if isinstance(exc, CommandNotFound):
            pass
        elif hasattr(exc, "original"):
            raise exc.original
        else:
            raise exc


    async def on_ready(self):
        if not self.ready:
            self.stdout = self.get_channel(693244168725856308)
            self.scheduler.add_job(self.rules_reminder, CronTrigger(day_of_week='0', hour='12',minute='0',second='0'))
            self.scheduler.start()
            
            

            #embed = Embed(title='Now Online!', description='Dashy-3 Is now online',
            #              colour=0xFF0000, timestamp=datetime.utcnow())
            #fields=[('Name','Value',True),
            #        ('Another Fireld','Another Value',True),
            #        ('A none inline filed','This fireld will apaer on new row same row',False),]
            #for name,value,inline in fields:
            #    embed.add_field(name=name, value=value,inline=inline)
            #    embed.set_author(name='Dashy-3')
            #    embed.set_footer(text='This is a footer!')
            #await channel.send(embed=embed)
            #await channel.send(file=File('./data/images/bot-icon-2883144_1280.png'))
            while not self.cogs_ready.all_ready():
                await sleep(0.5)

            await self.stdout.send("Now Online")
            self.ready = True
            print('bot ready')
        else:
            print('Bot reconnected')

    async def on_message(self, message):
        pass


bot = Bot()
