# -*- coding: utf-8 -*-
# @Time    : 2020/1/6 8:52
# @Author  : Han lei
# @Email   : hanlei5012@163.com
# @File    : client.py
# @Software: PyCharm
import socket
import time

from UserDialog import UserDialog


class Connection():
    def __init__(self):
        UserDialog.getUserinputIp()
        self.host = UserDialog._Ip
        self.port = UserDialog._port
        print(self.host,self.port)

        self.sock = socket.socket()
        self.sock.connect((self.host,self.port))
        data = self.sock.recv(5).decode()
        print(data)

        usernames = self.sock.recv(1024).decode()
        print(usernames)
        userList = usernames.split()

        while True:
            UserDialog.getUserNickName()
            self.nickname = UserDialog._nickname
            if self.nickname in userList:
                UserDialog.show_error_box('用户名已存在，请换一个')
            else:
                break
        self.sock.sendall((self.nickname.encode('utf-8')))
    def receive_msg(self):
        while True:
            time.sleep(0.1)
            data = self.sock.recv(1).decode('ISO-8859-1')
            if data == 'ß':
                print('ß')
                continue
            else:
                pass
if __name__ == '__main__':
    conn = Connection()
    conn.receive_msg()
    print('start')
