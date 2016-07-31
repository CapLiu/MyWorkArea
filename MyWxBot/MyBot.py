# coding=utf-8


import time
from wxbot import *


class MyWXBot(WXBot):
    def handle_msg_all(self, msg):
        pass
        #if msg['msg_type_id'] == 9:
            #self.send_msg(msg['username'], '表情收到')


    def schedule(self):
        #pass
        self.send_msg('文件传输助手', 'wxbot测试')
         #time.sleep(1)


def main():
    bot = MyWXBot()
    bot.DEBUG = True
    bot.run()
    exit()


if __name__ == '__main__':
    bot=MyWXBot()
    bot.preparetosendmsg()