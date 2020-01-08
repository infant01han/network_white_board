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
    _nickname = ''
    _Text = 'hello'
    @classmethod
    def get_text_from_user(cls):
        def get_text():
            temp = e1.get()
            master.destroy()
            if 'Ø' in temp:
                cls.show_error_box('Invalid character in expression')
            else:
                cls._Text = temp
        master = Tk()
        Label(master,text='What do you want to write?').grid(row=0)
        e1 = Entry(master)
        Label(master,text='Text: ').grid(row=1)
        e1.grid(row=1,column=1)

        button = Button(master,text='Set',command=get_text)
        button.grid(row=2,column=0,sticky=W,pady=4)
        master.bind('<Return>',lambda event=None:button.invoke())
        master.mainloop()
    @classmethod
    def show_error_box(cls,msg):
        master = Tk()
        Label(master,text=msg).grid(row=0)
        Button(master,text='ok',command=master.destroy).grid(row=1,pady=4)
        master.mainloop()
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
if __name__ == '__main__':
    UserDialog.get_text_from_user()
