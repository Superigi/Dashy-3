from discord.ext.commands import Bot as BotBase

from apscheduler.schedulers.asyncio import AsyncIOScheduler

PREFIX = '+'
OWNER_IDS =[234472372491517952]

class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.scheduler = AsyncIOScheduler
        super().__init__(command_prefix=PREFIX, owner_ids=OWNER_IDS)

    def run(self, version):
        self.VERSION = version
        with open('./lib/bot/token.0','r',encoding='utf=8')as tf:
            self.TOKEN = tf.read()
        print('Running bot ...')
        super().run(self.TOKEN, reconnect=True)

    async def on_connect(self):
        print('Bot is connected')

    async def on_disconect(self):
        print('Bot Has Disconnected')

    async def on_ready(self):
        if not self.ready:
            self.ready = True
            print('bot ready')
        else:
            print('Bot reconnected')

    async def on_message(self, message):
        pass


bot = Bot()
