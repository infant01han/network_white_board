# -*- coding: utf-8 -*-
# @Time    : 2020/1/6 8:52
# @Author  : Han lei
# @Email   : hanlei5012@163.com
# @File    : client.py
# @Software: PyCharm
import time
from threading import Thread

from connection import Connection
from whiteboard import WhiteBoard


class Client(Thread,WhiteBoard):
    def __init__(self):
        self.conn = Connection()
        Thread.__init__(self)
        WhiteBoard.__init__(self)
        self._init_mouse_event()
        self.setDaemon(True)
        self.isMouseDown = False
        self.x_pos = None
        self.y_pos = None
        self.last_time = None
    def _init_mouse_event(self):
        self.drawing_area.bind('<Motion>',self.motion)
        self.drawing_area.bind('<ButtonPress-1>',self.left_but_down)
        self.drawing_area.bind('<ButtonRelease-1>',self.left_but_up)
    def left_but_down(self,event=None):
        self.isMouseDown = True
        self.x_pos = event.x
        self.y_pos = event.y
        self.last_time = time.time()
    def left_but_up(self,event=None):
        self.isMouseDown = False
        print(event.x,event.y)
        self.last_time = None
    # (tpye，startx,starty,endx,endy,color)
    # ('D',startx,starty,endx,endy,'red')
    def motion(self,event=None):
        if self.isMouseDown == True:
            now = time.time()
            if now - self.last_time < 0.02:
                return
            self.last_time = now
            msg = ('D',self.x_pos,self.y_pos,event.x,event.y,'red')
            self.conn.send_message(msg)
            self.x_pos = event.x
            self.y_pos = event.y
    def run(self):
        while True:
            msg = self.conn.receive_msg()
            self.draw_from_msg(msg)
            if msg == 'xxx':
                pass
            # time.sleep(0.1)
if __name__ == '__main__':
    client = Client()
    client.start()
    client.show_window()