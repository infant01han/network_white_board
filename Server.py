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
    Clients = []
    logs = {}
    def __init__(self,host,port):
        self.host = host
        self.port = port
        self.network = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.network.bind((self.host,self.port))
        self.network.listen(20)

        print(f'server listen at {self.port}')
        threading.Thread(target=self.pinger).start()
    # 心跳线程
    def pinger(self):
        while True:
            time.sleep(1)
            for client in Server.Clients:
                try:
                    msg = 'ß'.encode('ISO-8859-1')
                    # print('ß')
                    client.sock.send(msg)
                except ConnectionResetError:
                    print('ConnectionResetError')
                    client.terminate()
                    Server.Clients.remove(client)
                    pass
                except ConnectionAbortedError:
                    print('ConnectionAbortedError')
                    client.terminate()
                    Server.Clients.remove(client)
                    pass
    def start(self):
        while True:
            client_sock,client_addr = self.network.accept()
            print(f'client {client_addr} connected')

            client_sock.send('HELLO'.encode())
            time.sleep(0.1)

            msg = ' '
            for client in Server.Clients:
                msg = msg + ' ' + client.clientID
            # msg = '  zhangsan lisi'
            client_sock.send(msg.encode())

            client_thread = threading.Thread(target=self.wait_for_user_nickname,args=[client_sock])  # 这里参数传的的列表
            client_thread.start()
    def wait_for_user_nickname(self,client_sock):
        new_user_id = client_sock.recv(1024).decode('utf-8')
        print(new_user_id)
        print(Server.logs)
        for msgid in Server.logs.keys():
            msg = Server.logs[msgid]
            client_sock.sendall(msg.encode('ISO-8859-1'))
        client = Client(client_sock,new_user_id)
        Server.Clients.append(client)
        client.start()
class Client:
    msgID = 0
    def __init__(self,sock,clientID):
        self.sock = sock
        self.clientID = clientID
        self._run = True
    def terminate(self):
        self._run = False
    def start(self):
        while self._run:
            msg = ''
            while True:
                data = self.sock.recv(1).decode('ISO-8859-1')
                msg += data
                if data == 'Ø':
                    break
            Server.logs[Client.msgID] = msg
            if msg[0] == 'D':
                self.broadcast2Client(msg)
            Client.msgID += 1
            pass
    def broadcast2Client(self,msg):
        msg = msg.encode('ISO-8859-1')
        for client in Server.Clients:
            client.sock.sendall(msg)
if __name__ == '__main__':
    server = Server('0.0.0.0', 6000)
    server.start()