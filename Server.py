# -*- coding: utf-8 -*-
# @Time    : 2020/1/3 16:10
# @Author  : Han lei
# @Email   : hanlei5012@163.com
# @File    : Server.py.py
# @Software: PyCharm
import socket
import threading
import time


class Server:
    Client = []
    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.network = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.network.bind((self.host,self.port))
        self.network.listen(20)

        print(f'server listen at {self.port}')
    def start(self):
        while True:
            client_sock,client_addr = self.network.accept()
            print(f'client {client_addr} connected')

            client_sock.send('HELLO'.encode())

            time.sleep(0.1)
            client_thread = threading.Thread(target=self.wait_for_user_nickname,args=[client_sock])  # 这里参数传的的列表
            client_thread.start()
    def wait_for_user_nickname(self,client_sock):
        new_user_id = client_sock.recv(1024).decode('utf-8')
        print(new_user_id)
        client = Client(client_sock,new_user_id)
        Server.Client.append(client)
        client.start()
class Client:
    def __init__(self,sock,clientID):
        self.connection = sock
        self.clientID = clientID
        self._run = True
    def start(self):
        while self._run:
            time.sleep(0.1)
            pass
if __name__ == '__main__':
    server = Server('0.0.0.0', 6000)
    server.start()