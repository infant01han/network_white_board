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
        UserDialog.getUserNickName()
        self.nickname = UserDialog._nickname
        self.sock.sendall((self.nickname.encode('utf-8')))
    def start(self):
        while True:
            time.sleep(0.1)
            pass
if __name__ == '__main__':
    conn = Connection()
    conn.start()
    print('start')
