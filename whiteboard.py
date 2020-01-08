# -*- coding: utf-8 -*-
# @Time    : 2020/1/6 14:15
# @Author  : Han lei
# @Email   : hanlei5012@163.com
# @File    : whiteboard.py
# @Software: PyCharm
import math
from tkinter import *
from tkinter import font

from UserDialog import UserDialog


class WhiteBoard:
    drawing_tool = 'pencil'
    Colors = {'b': 'blue', 'r': 'red', 'g': 'green', 'o': 'orange', 'y': 'yellow', 'c': 'cyan', 'p': 'purple1',
              'd': 'black', 's': 'snow'}
    line_width = 2
    def __init__(self):
        self.color = 'b'
        self.init_whiteboard()
        self._init_item_button()
        self._init_color_button()
        self.init_drawing_area()
    def draw_pencil(self,msgLst):
        startX,startY,endX,endY = int(msgLst[1]),int(msgLst[2]),int(msgLst[3]),int(msgLst[4])
        color = msgLst[5]
        msgid = msgLst[6]
        self.drawing_area.create_line(startX,startY,endX,endY,fill=color,width=self.line_width,tags=(msgid,))
    def draw_Rectangle(self,msgLst):
        startX,startY,endX,endY = int(msgLst[1]),int(msgLst[2]),int(msgLst[3]),int(msgLst[4])
        color = msgLst[5]
        msgid = msgLst[6]
        self.drawing_area.create_rectangle(startX,startY,endX,endY,fill=color,width=0,tags=(msgid,))
    def draw_oval(self,msgLst):
        startX,startY,endX,endY = int(msgLst[1]),int(msgLst[2]),int(msgLst[3]),int(msgLst[4])
        color = msgLst[5]
        msgid = msgLst[6]
        self.drawing_area.create_oval(startX,startY,endX,endY,fill=color,width=0,tags=(msgid,))
    def draw_line(self,msgLst):
        startX,startY,endX,endY = int(msgLst[1]),int(msgLst[2]),int(msgLst[3]),int(msgLst[4])
        color = msgLst[5]
        msgid = msgLst[6]
        self.drawing_area.create_line(startX,startY,endX,endY,fill=color,width=0,tags=(msgid,))
    def draw_circle(self,msgLst):
        startX,startY,endX,endY = int(msgLst[1]),int(msgLst[2]),int(msgLst[3]),int(msgLst[4])
        x_center = (startX+endX)//2
        y_center = (startY+endY)//2
        radius = math.sqrt((endX-startX)**2+(endY-startY)**2)//2
        color = msgLst[5]
        msgid = msgLst[6]
        self.drawing_area.create_oval(x_center-radius,y_center-radius,x_center+radius,y_center+radius,fill=color,width=0,tags=(msgid,))
    def draw_square(self,msgLst):
        startX,startY,endX,endY = int(msgLst[1]),int(msgLst[2]),int(msgLst[3]),int(msgLst[4])
        edge_size = ((endX-startX) + (endY-startY)) //2
        color = msgLst[5]
        msgid = msgLst[6]
        self.drawing_area.create_rectangle(startX,startY,startX+edge_size,startY+edge_size,fill=color,width=0,tags=(msgid,))
    def draw_Text(self,msgLst):
        textLst = msgLst[4:-1]
        text = ' '.join(textLst)
        x,y = msgLst[1],msgLst[2]
        color = msgLst[3]
        msgid = msgLst[-1]
        text_font = font.Font(family='Helvetica', size=50, weight='bold', slant='italic')
        self.drawing_area.create_text(x,y,fill=color,font=text_font,text=text,tags=(msgid,))
    def delete_obj(self,msgLst):
        item = self.drawing_area.find_withtag(msgLst[1])
        self.drawing_area.delete(item)
    def draw_from_msg(self,msg):
        msgLst = msg[:-1].split(' ')
        draw_type = msgLst[0]
        if draw_type == 'D':
            self.draw_pencil(msgLst)
        elif draw_type == 'R':
            self.draw_Rectangle(msgLst)
        elif draw_type == 'L':
            self.draw_line(msgLst)
        elif draw_type == 'O':
            self.draw_oval(msgLst)
        elif draw_type == 'C':
            self.draw_circle(msgLst)
        elif draw_type == 'S':
            self.draw_square(msgLst)
        elif draw_type == 'T':
            self.draw_Text(msgLst)
        elif draw_type == 'Z':
            self.delete_obj(msgLst)
        else:
            pass
    def show_window(self):
        self.myWhiteBoard.mainloop()
    def init_drawing_area(self):
        self.drawing_area = Canvas(self.myWhiteBoard,width=1000,height=700,bg='white')
        self.drawing_area.place(y=50)
    def init_whiteboard(self):
        self.myWhiteBoard = Tk()
        self.myWhiteBoard.geometry('1280x780')
    def set_drawing_tool(self,tool):
        print(tool)
        WhiteBoard.drawing_tool = tool
    def set_color(self,color):
        print(color)
        self.color = color
    def get_text_from_user(self):
        WhiteBoard.drawing_tool = 'text'
        UserDialog.get_text_from_user()
    def _init_item_button(self):
        Button(self.myWhiteBoard,text='line',height=1,width=5,bg='dark goldenrod',font='Arial',
               command=lambda: self.set_drawing_tool('line')).place(x=70,y=0)
        Button(self.myWhiteBoard, text='rect', height=1, width=5, bg='saddle brown', font='Arial',
               command=lambda: self.set_drawing_tool('rectangle')).place(x=140, y=0)
        Button(self.myWhiteBoard, text='oval', height=1, width=5, bg='NavajoWhite4', font='Arial',
               command=lambda: self.set_drawing_tool('oval')).place(x=210, y=0)
        Button(self.myWhiteBoard, text='text', height=1, width=5, bg='SteelBlue4', font='Arial',
               command=self.get_text_from_user).place(x=280, y=0)
        Button(self.myWhiteBoard, text='pencil', height=1, width=5, bg='DeepSkyBlue2', font='Arial',
               command=lambda: self.set_drawing_tool('pencil')).place(x=350, y=0)
        Button(self.myWhiteBoard, text='circle', height=1, width=5, bg='Turquoise2', font='Arial',
               command=lambda: self.set_drawing_tool('circle')).place(x=420, y=0)
        Button(self.myWhiteBoard, text='square', height=1, width=5, bg='CadetBlue1', font='Arial',
               command=lambda: self.set_drawing_tool('square')).place(x=490, y=0)
        Button(self.myWhiteBoard, text='eraser', height=1, width=5, bg='purple1', font='Arial',
               command=lambda: self.set_drawing_tool('eraser')).place(x=560, y=0)
        Button(self.myWhiteBoard, text='drag', height=1, width=5, bg='green', font='Arial',
               command=lambda: self.set_drawing_tool('drag')).place(x=630, y=0)
    def _init_color_button(self):
        Button(self.myWhiteBoard,height=1,width=5,bg='red',
               command=lambda: self.set_color('r')).place(x=1010,y=50)
        Button(self.myWhiteBoard, height=1, width=5, bg='orange',
               command=lambda: self.set_color('o')).place(x=1010, y=100)
        Button(self.myWhiteBoard, height=1, width=5, bg='yellow',
               command=lambda: self.set_color('y')).place(x=1010, y=150)
        Button(self.myWhiteBoard, height=1, width=5, bg='green',
               command=lambda: self.set_color('g')).place(x=1010, y=200)
        Button(self.myWhiteBoard, height=1, width=5, bg='cyan',
               command=lambda: self.set_color('c')).place(x=1010, y=250)
        Button(self.myWhiteBoard, height=1, width=5, bg='blue',
               command=lambda: self.set_color('b')).place(x=1010, y=300)
        Button(self.myWhiteBoard, height=1, width=5, bg='purple1',
               command=lambda: self.set_color('p')).place(x=1010, y=350)
        Button(self.myWhiteBoard, height=1, width=5, bg='black',
               command=lambda: self.set_color('d')).place(x=1010, y=400)
        Button(self.myWhiteBoard, height=1, width=5, bg='snow',
               command=lambda: self.set_color('s')).place(x=1010, y=450)
if __name__ == '__main__':
    wb = WhiteBoard()