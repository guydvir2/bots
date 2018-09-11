import telepot
from telepot.loop import MessageLoop
from threading import Thread
import time


class TelegramBot(Thread):
    def __init__(self, id=None, token=None):
        Thread.__init__(self)
        if id is None:
            self.chat_id = 596123373
        else:
            self.chat_id = id
        if token is None:
            self.bot = telepot.Bot('497268459:AAFrPh-toL6DPPArWknqJzIAby8jMi21S4c')
        else:
            self.bot = telepot.Bot(token)

        self.me = self.bot.getMe()
        self.send_msg("HomePi Telegram - Start")
        self.telbot_arrived_msg = None
        self.msg_chtid = None

    def send_msg(self, msg):
        self.bot.sendMessage(self.chat_id, msg)

    def handle(self, msg):
        self.msg_chtid = msg['chat']['id']
        self.telbot_arrived_msg = msg['text']
        self.telbot_commands()

    def telbot_commands(self):
        pass

    def run(self):
        MessageLoop(self.bot, self.handle).run_as_thread()
        while True:
            time.sleep(1)


if __name__ == "__main__":

    def coms(msg):
        if msg == '1':
            print("ONR")
        else:
            print("OTHER")


    a = MyTBot()
    # a.commands(command)= lambda :com
    a.start()
