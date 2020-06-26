from discord.ext.commands import Bot as BotBase
from discord import Embed, File
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.cron import CronTrigger
from datetime import datetime
from discord.ext.commands import CommandNotFound
from ..db import db


PREFIX = '+'
OWNER_IDS =[234472372491517952]

class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.scheduler = AsyncIOScheduler()

        db.autosave(self.scheduler)

        super().__init__(command_prefix=PREFIX, owner_ids=OWNER_IDS)

    def run(self, version):
        self.VERSION = version
        try:
            with open('./lib/bot/token.0','r',encoding='utf=8')as tf:
                self.TOKEN = tf.read()
        except:
            print("There was an error trying to load the token in ./lib/bot/token.0\nThe program will now exit")
            exit(1)
        print('Running bot ...')
        super().run(self.TOKEN, reconnect=True)

    async def rules_reminder(self):
        pass

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
            self.ready = True
            self.scheduler.add_job(self.rules_reminder, CronTrigger(day_of_week=0, hour=12, minute=0, second=0))
            self.scheduler.start()



            channel = self.get_channel(693244168725856308)
            await channel.send("Now Online")

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

            print('bot ready')
        else:
            print('Bot reconnected')

    async def on_message(self, message):
        pass


bot = Bot()
