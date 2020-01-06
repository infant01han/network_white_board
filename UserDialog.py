# -*- coding: utf-8 -*-
# @Time    : 2020/1/6 9:40
# @Author  : Han lei
# @Email   : hanlei5012@163.com
# @File    : UserDialog.py
# @Software: PyCharm
from tkinter import *
class UserDialog:
    _Ip = ''
    _port = 0
    @classmethod
    def getUserinputIp(cls):
        def getUserIPAndPort():
            cls._Ip = e1.get()
            cls._port = int(e2.get())
            ClientWindow.destroy()

        ClientWindow = Tk()
        Label(ClientWindow,text='请输入IP').grid(row=0)
        Label(ClientWindow,text='IP').grid(row=1)
        Label(ClientWindow,text='Port').grid(row=2)

        e1 = Entry(ClientWindow)
        e2 = Entry(ClientWindow)
        e1.grid(row=1,column=1)
        e2.grid(row=2,column=1)

        button = Button(ClientWindow,text='ok',command=getUserIPAndPort)
        button.grid(row=3,column=0)

        ClientWindow.mainloop()

    @classmethod
    def getUserNickName(cls):
        def getUserNickNameInner():
            cls._nickname = e1.get()
            ClientWindow.destroy()

        ClientWindow = Tk()
        Label(ClientWindow,text='请输入昵称').grid(row=0)
        Label(ClientWindow,text='昵称').grid(row=1)

        e1 = Entry(ClientWindow)
        e1.grid(row=1,column=1)

        button = Button(ClientWindow,text='ok',command=getUserNickNameInner)
        button.grid(row=2,column=0)

        ClientWindow.mainloop()
